# -*- coding: utf-8 -*-
def CompOptimalC(Person,ipy,iw,year,RealRate,RandomY,NextPeriodUtility):
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
    year : integer
       Index of the year in the working life being analyzed. A -1 indicates
       the last year before retimrement
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
    # Savings Utility is a routine that takes the year, the matrix of next 
    # periods utility, the index of the level of wealth being considered for 
    # next period, and the index of the permanent income value being 
    # considered, and reports the expected marginal utility of saving
    # of the next dollar of savings.
    from SavingsUtility import SavingsUtility as SavingsUtility
    
    # Define routine to compute marginal utility of given consumption
    def CompMarginalUtilityC(C,Eta):
        return(c ** -Eta)
    
    # Useful Constants
    NWealthStates = Person.WealthMat.shape[0] # Number of wealth states
    NPY = Person.PermYMat.shape[0]            # Numer of pemanent Y states
    
    # Compute resources available for consumption:
    #   Wealth + investment earnings
    #   + transient income shock
    #   + Permanent income    
    CurrentWealth = Person.WealthMat[iw,year] * (1 + RealRate)
    Resources = CurrentWealth + np.exp(RandomY) + Person.PermYMat[ipy,year]
    
    #######  Part I #######
    # The first part of this routime computes the optimal level of savings.
    # Part II computes the expected utiliy associate with that choice.
    # Instead of starting the search for the optimal level of savings in the
    # middle of possible sates we could have started it at one end or the
    # other. Starting close to the current level of savings should save
    # us many function evaluations as the optimal level of wealth is very
    # likely to be close to the current level. 
    
    # Find point where marginal utility of savings is less than marginal
    # utility of consumption. Start with first level of savings above
    # current wealth.   
    indexNextWealth=np.argmax(Person.Wealth[:,year] > CurrentWealth)
    
    # Determine which direction to search for Expected Utility max by
    # comparing marginal utility of consumption vs. marginal utility
    # of savings at indexNextWealth
    Consumption = Resources - Person.Wealth[indexNextWealth,year]
    MarginalUofSavings = SavingsUtility(Person
                                        ,year
                                        ,NextPeriodUtility
                                        ,indexNextWealth
                                        ,ipy):
    if CompMarginalUtility(Consumption,Person.crra) < MarginalUofSavings:
        # If true search forward to higher levels of savings and lower levels
        # of consumption
        MaxFlag = False   # Set flag that indicates utility max not found
        # Loop over wealth states greater than starting value
        while MaxFlag == False and indexNextWealth < NWealthStates:
            
            LastMarginalUofSavings = MarginalUofSavings
            indexNextWealth += 1
            Consumption = Resources - Person.Wealth[indexNextWealth,year]
            MarginalUofSavings = SavingsUtility(Person
                                                ,year
                                                ,NextPeriodUtility
                                                ,indexNextWealth
                                                ,ipy)):
            if (CompMarginalUtilityC(Consumption,Person.crra)
                       >= MarginalUofSavings):
                # If true, the maximum value of savings is at this level 
                # or is a mixture of this and next lower level of savings. 
                # Determine which here.
                if (CompMarginalUtilityC(Consumption,Person.crra)
                    >= LastMarginalUofSavings):
                    # In this case the optimum is a mixture of this level
                    # of wealth and the last level of wealth. Now compute
                    # that mixture
                    Savings = Resources 
                              - LastMarginalUtilityofSavings 
                              ** (-1 / Person.crra)
                    # ProbLower is he probability that the next periods savings
                    # will be the lower of the two adjacent values. The notion
                    # is that the person is buying a fair lottery between
                    # the two possible values of wealth
                    ProbLower = ((Savings 
                                - Person.WealthMat[indexNextWealth - 1, year])
                                / (Person.WealthMat[indexNextWealth, year]
                                - Person.WealthMat[indexNextWealth - 1, year]))
                else:
                    # In this case Person will choose savings level 
                    # indexNextWealth
                    Savings = Person.WealthMat[indexNextWealth, year]
                    ProbLower = 0
            
                MaxFlag = True  # Since optimum was found set MaxFlag to True
                                # and end the loop
                                
            # If Marginal utility of consumption is still less than Marginal
            # Utility of Savings continue loop
            
        ####  end While Loop ####
        
        if MaxFlag == False:
            # In this case marginal utillity of consumption is still less than
            # Expected MU of savings. Set savings equal to maximum value
            Savings = Person.WealthMat[-1, year]
            ProbLower = 0
        
    else:
        # If marginl utility of consumption is greater than or equal to 
        # expected marginal utility of saving then savings is at this level
        # or lower. 
        MaxFlag = False   # Set flag that indicates utility max not found
        # Loop over wealth states less than starting value
        while MaxFlag == False and indexNextWealth >= 1:
            MarginalUofLowerSavings = SavingsUtility(Person
                                                     ,year
                                                     ,NextPeriodUtility
                                                     ,indexNextWealth-1
                                                     ,ipy)):
            if (ComputeMarginalUtilityC(Consumption,Persno.crra)
                < MarginalUofLowerSavings):
                # If Utility of consumption is less than marginal utility of 
                # next lower value of savings then savings is set at this level
                Savings=Person.WealthMat[indexNextWealth,year]
                ProbLower=0
            else:
                #Otherwise we consider next lower wealth catagory
                LastMarginalUofSavings = MarginalUofSavings
                indexNextWealth -= 1
                Consumption = Resources - Person.Wealth[indexNextWealth,year]
                MarginalUofSavings = SavingsUtility(Person
                                                    ,year
                                                    ,NextPeriodUtility
                                                    ,indexNextWealth
                                                    ,ipy
                                                    )
                if (CompMarginalUtility(Consumption,Person.crra)
                       < MarginalUofSavings):
                    # If true, the maximum value of savings is at this level 
                    # or is a mixture of this and next higher level of savings. 
                    # Determine which here.
                    if (CompMarginalUtility(Consumption,Person.crra)
                        < LastMarginalUofSavings):
                        # In this case the optimum is a mixture of this and
                        # the next higher level of savings
                        Savings = Resources 
                                  - LastMarginalUtilityofSavings 
                                  ** (-1 / Person.crra)
                        # ProbLower is he probability that the next periods savings
                        # will be the lower of the two adjacent values. The notion
                        # is that the person is buying a fair lottery between
                        # the two possible values of wealth
                        ProbLower = ((Savings 
                                - Person.WealthMat[indexNextWealth - 1, year])
                                / (Person.WealthMat[indexNextWealth, year]
                                - Person.WealthMat[indexNextWealth - 1, year]))
                        else:
                            # In this case Person will choose savings level 
                            # indexNextWealth
                            Savings = Person.WealthMat[indexNextWealth, year]
                            ProbLower = 0
            
                        MaxFlag = True  # Since optimum was found set MaxFlag 
                                        # to True and end the loop
                                
            # If Marginal utility of consumption is still greater than Marginal
            # Utility of Savings continue loop
        ####  end While Loop ####
        
        if MaxFlag == False:
            # In this case marginal utillity of consumption is still greater
            # than Expected MU of savings. Set savings equal to minimum value
            Savings = Person.WealthMat[0, year]
            ProbLower = 0
     
    ####### Part II #######
    # Having found the optimal level of savings the next step is to compute 
    # the expected utility associated with that savings and to return the 
    # result.
    # First compute the Utility of consumption in the current year
    Utility = (Consumption ** (1 - Person.crra) - 1) / ( 1 - Person.crra)
    # Now add in the expected utililty associated with each possible 
    # value for permanent income in the next period weighted by the 
    # probability of transition to that value
    for i in range NPY
                   
        
    
    
                    
                

        
    
            
    
    
    

