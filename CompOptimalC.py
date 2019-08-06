# -*- coding: utf-8 -*-
def CompOptimalC(Person,ipy,iw,WorkYear,RealRate,RandomY,NextPeriodUtility):
    """
    The routine takes the utility by state matrix for the next year, and for 
    a specific level of resources available in the year being analyzed and
    computes the optimal value for consumption. It then computes the
    value of utility from that consumption, adds it to the expected
    future utility based on the current state and the likely future states
    and returns that in all but the current year. For the current year it
    reports the value of consumption as well as the total lifetime expected
    utility.
    
    Parameters
    ----------
    Person : an instance of the class people
       This class contains all the information on the person needed. See
       Main.py where it is defined
    ipy : integer
       Index for the permanent income state to use in computing available
       resources
    iw : integer
       Index for the wealth state to use in computing available resources
    WorkYear : integer
       Index of the year in the working life being analyzed. 
    RealRate : floating point
       The real rate of return on savings during the person's life. If no 
       credit constraints this is also the expected interest on money 
       borrowed
   RandomY : floating point
       The natural log of the transient component of income used to compute
       available resources
   NextPeriodUtility : numpy matrix
       A Matrix containing the expected utility values associated with 
       each possible end state for the period being analyzed. When analyzing
       the final working year this is a numpy vector containing the utility 
       values associated with each final level of wealth.
  
    Returns
    -------
    Utility : floating point
        If the Year is greater than 0 this is the only return. It is the value
        of Expected Utility given an optimal consumption choice in this
        period given available resources as specified by inputs
    LEU : floating point
       If the Year is 0 this is reported. It is the Lifetime Expected 
       Utiliity given optimal savings in most recent period 
    OptimalConsumpton : floating point
       When the Year is 0 this is reported. It is the optimal level of 
       consumption for the current year for the person being analyzed
         
       Created on Fri Jul 12 10:46:25 2019

    @author: wtdickens
    """
    import numpy as np
    import math as m
    # Savings Utility is a routine that takes the year, the matrix of next 
    # periods utility, the index of the level of wealth being considered for 
    # next period, and the index of the permanent income value being 
    # considered, and reports the expected marginal utility of saving
    # of the next dollar of savings.
    from SavingsUtility import SavingsMUtility as SavingsMUtility
    
    # Define routine to compute marginal utility of given consumption
    def MarginalUtilityC(C,Eta):
        if C <= 0:
            return(float("inf"))
        else:
            return(1/m.pow(C,Eta))
    
    # Useful Constants
    NWealthStates = Person.WealthMat.shape[0] # Number of wealth states
    NPY = Person.PermYMat.shape[0]            # Numer of pemanent Y states
    
    # Compute resources available for consumption:
    #   Wealth + investment earnings
    #   + Permanent income (1 + transient shock)   
    if WorkYear == 0:
        CurrentWealth = Person.StartingWealth
        Resources = CurrentWealth + Person.Y
    else:
        CurrentWealth = Person.WealthMat[iw,WorkYear] * (1 + RealRate)
        Resources = (CurrentWealth + Person.PermYMat[ipy,WorkYear] 
        * (1 + RandomY))
    
    #######  Part I #######
    # The first part of this routime computes the optimal level of savings.
    # Part II computes the expected utiliy associate with that choice.
    # Instead of starting the search for the optimal level of savings near
    # that given by iw we could have started it at one end or the
    # other. Starting close to the "current" level of savings should save
    # us many function evaluations as the optimal level of wealth is very
    # likely to be close to the current level. 
    
    # Find next period wealth category just above current wealth
    indexNextWealth=np.argmax(Person.WealthMat[:,WorkYear] > CurrentWealth) + 1
    # If it is the last category step index back one
    if indexNextWealth >= Person.WealthMat.shape[0] - 1:
        indexNextWealth =  Person.WealthMat.shape[0] - 2
    # If it is the first category set it equal to the second
    if indexNextWealth == 0:
        indexNextWealth = 1
    
    # Determine which direction to search for Expected Utility max by
    # comparing marginal utility of consumption vs. marginal utility
    # of savings at indexNextWealth
    TestConsumption = Resources - Person.WealthMat[indexNextWealth,WorkYear]
    print(TestConsumption)           ########################################
    MarginalUofSavings = SavingsMUtility(Person
                                        ,WorkYear
                                        ,NextPeriodUtility
                                        ,indexNextWealth
                                        ,ipy)
    if MarginalUtilityC(TestConsumption,Person.crra) < MarginalUofSavings:
        # If true search forward to higher levels of savings and lower levels
        # of consumption. Person.crra is coef of relative risk aversion.
        
        # First compute Marginal utility of savings at next lower level of
        # savings
        MarginalUofSavings = SavingsMUtility(Person
                                             ,WorkYear
                                             ,NextPeriodUtility
                                             ,indexNextWealth - 1
                                             ,ipy)
        MaxFlag = False   # Set flag that indicates utility max not found
        # Loop over wealth states greater than starting value

        print("MargUC < MargUofS",TestConsumption,MarginalUtilityC(
                TestConsumption,Person.crra)) #############################################
        while MaxFlag == False and indexNextWealth < NWealthStates - 1:
            LastMarginalUofSavings = MarginalUofSavings
            TestConsumption = (Resources 
                               - Person.WealthMat[indexNextWealth, WorkYear])
            MarginalUofSavings = SavingsMUtility(Person
                                                ,WorkYear
                                                ,NextPeriodUtility
                                                ,indexNextWealth
                                                ,ipy)
            print(MarginalUtilityC(TestConsumption, Person.crra),
                  MarginalUofSavings,TestConsumption)#########################################
            if (MarginalUtilityC(TestConsumption, Person.crra)
                       >= MarginalUofSavings):
                # If true, the maximum value of savings is at this level 
                # or is a mixture of this and next lower level of savings. 
                # Determine which here.
                if (MarginalUtilityC(TestConsumption, Person.crra)
                    >= LastMarginalUofSavings):
                    # In this case the optimum is a mixture of this level
                    # of wealth and the last level of wealth. Now compute
                    # that mixture
                    # Compue savings by setting MU of last savings level to
                    # MU of consumption
                    Savings = (Resources
                               - 1 / m.pow(LastMarginalUofSavings,
                               (1 / Person.crra)))
                    # ProbLower is the probability that the next period's 
                    # savings will be the lower of the two adjacent values. 
                    # The notion is that the person is buying a fair lottery 
                    # between the two possible values of wealth.
                    ProbLower = (1 - (Savings 
                                - Person.WealthMat[indexNextWealth - 1, 
                                                   WorkYear])
                                / (Person.WealthMat[indexNextWealth, WorkYear]
                                - Person.WealthMat[indexNextWealth - 1, 
                                                   WorkYear]))
                else:
                    # In this case Person will choose savings level at
                    # indexNextWealth
                    Savings = Person.WealthMat[indexNextWealth, WorkYear]
                    ProbLower = 0
            
                MaxFlag = True  # Since optimum was found set MaxFlag to True
                                # and end the loop

            indexNextWealth += 1                              
            # If Marginal utility of consumption is still less than Marginal
            # Utility of Savings continue loop
            
        ####  end While Loop ####
        
        if MaxFlag == False:
            # In this case savings is either at its highest level or between 
            # the highest and next highes level
            TestConsumption = (Resources 
                               - Person.WealthMat[indexNextWealth, WorkYear])
            if  0 <= MarginalUtilityC(TestConsumption, Person.crra):
                # Compue savings by setting MU of last savings level to
                # MU of consumption
                Savings = (Resources - 1 / m.pow(MarginalUofSavings,
                               (1 / Person.crra)))
                # ProbLower is the probability that the next period's 
                # savings will be the lower of the two adjacent values. 
                # The notion is that the person is buying a fair lottery 
                # between the two possible values of wealth.
                ProbLower = (1 - (Savings 
                               - Person.WealthMat[indexNextWealth - 1, 
                                                         WorkYear])
                                / (Person.WealthMat[indexNextWealth, WorkYear]
                                - Person.WealthMat[indexNextWealth - 1, 
                                                   WorkYear]))
            else:
                # In this case marginal utility of consumption is less than
                # last marginal utility of savings so set savings to max
                Savings = Person.WealthMat[-1, WorkYear]
                ProbLower = 0         
            
        
    else:
        # If marginl utility of consumption is greater than or equal to 
        # expected marginal utility of saving then savings is at this level
        # or lower. 
        
        print("MargUC >= MargUofS") #############################################
        MaxFlag = False   # Set flag that indicates utility max not found
        # Loop over wealth states less than starting value
        while MaxFlag == False and indexNextWealth >= 1:
            MarginalUofLowerSavings = SavingsMUtility(Person
                                                     ,WorkYear
                                                     ,NextPeriodUtility
                                                     ,indexNextWealth - 1
                                                     ,ipy)
            if (MarginalUtilityC(TestConsumption,Person.crra)
                < MarginalUofLowerSavings):
                # If M Utility of consumption is less than marginal utility of 
                # next lower value of savings then savings is set at this level
                Savings = Person.WealthMat[indexNextWealth,WorkYear]
                ProbLower = 0
                MaxFlag = True
            else:
                #Otherwise we consider next lower wealth catagory
                LastMarginalUofSavings = MarginalUofSavings
                indexNextWealth -= 1
                TestConsumption = (Resources 
                                   - Person.WealthMat[indexNextWealth,
                                                      WorkYear])
                MarginalUofSavings = MarginalUofLowerSavings
                if (MarginalUtilityC(TestConsumption,Person.crra)
                       < MarginalUofSavings):
                    # If true, the maximum value of savings is a mixture of 
                    # this and next higher level of savings. 
                    Savings = (Resources 
                                 - 1 / m.pow(LastMarginalUofSavings, 
                                 (1 / Person.crra)))
                    # ProbLower is he probability that the next periods 
                    # savings will be the lower of the two adjacent values. 
                    # The notion is that the person is buying a fair 
                    # lottery between the two possible values of wealth
                    ProbLower = ((Savings 
                                - Person.WealthMat[indexNextWealth - 1, 
                                                   WorkYear])
                                / (Person.WealthMat[indexNextWealth, WorkYear]
                                - Person.WealthMat[indexNextWealth - 1, 
                                                   WorkYear]))
                    MaxFlag = True
                                
            # If Marginal utility of consumption is still greater than Marginal
            # Utility of Savings (MaxFlag = False) continue loop
        ####  end While Loop ####
        
        if MaxFlag == False:
            # In this case marginal utillity of consumption is still greater
            # than Expected MU of savings at minimum value of savings 
            # In that case set savings equal to minimum value
            Savings = Person.WealthMat[0, WorkYear]
            ProbLower = 0
     
    ####### Part II #######
    # Having found the optimal level of savings the next step is to compute 
    # the expected utility associated with that savings and to return the 
    # result.
    # First compute the Utility of consumption in the current year
    Consumption = Resources - Savings
    Utility = ((1 / m.pow(Consumption, (Person.crra - 1)) - 1)
               / (1 - Person.crra))

    # Now add in the expected utililty associated with each possible
    # value for permanent income in the next period weighted by the
    # probability of transition to that value for the one or two possible
    # values of savings
    if NextPeriodUtility.shape[1] > 1:
        for i in range(NPY):
            Utility += (NextPeriodUtility[i, indexNextWealth]
                        * Person.TransMat[ipy, i, WorkYear]
                        * (1 - ProbLower))
            if ProbLower > 0:
                Utility += (NextPeriodUtility[i, indexNextWealth-1]
                            * Person.TransMat[ipy, i, WorkYear]
                            * ProbLower)
    else:
        # If last period of working life then Permanent Income doesn't matter.
        # In that case add utility considering wealth state only.
        Utility += (NextPeriodUtility[indexNextWealth]
                    * (1 - ProbLower))
        if ProbLower > 0:
                Utility += (NextPeriodUtility[indexNextWealth-1]
                            * ProbLower)

    # If period is other than zero report Expected utility for state and end
    print("Consumption in Year ", WorkYear, " is ", Consumption, "Out of ",
          Resources, " With Random =", RandomY)  # #########################
    if Consumption < 0:
        print(ipy, iw, Savings, Utility, np.where(Person.WealthMat == Savings))
        print(Person.WealthMat[4, WorkYear])
        raise Exception("negative consumption")

    if WorkYear > 0:
        return(Utility)
    # Otherwise return consumption and utility
    else:
        return(Consumption, Utility)
