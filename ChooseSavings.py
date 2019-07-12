# -*- coding: utf-8 -*-
def ChooseSavings(Person,RetirementAge,RealRate,Years_of_Retirement,
                  NumberYDraws):
"""
    This routine takes the information on a person and computes the optimal
    savings rate for the most recent year of that person's life as a function
    of their current wealth, their current permanent income, and 
    characteristics that might affect their future earnings and utility of
    income. It solves the lifetime utility maximization problem by backward
    induction computing the optimal behavior for each state and then 
    
    Parameters
    ----------
    person : an instance of the class people
       This class contains all the information on the person needed. See
       Main.py where it is defined
    RetirementAge : Integer
       Expected age of retirement (assumed to be known)
    RealRate : floating point
       The real rate of return on savings during the person's life. If no 
       credit constraints this is also the expected interest on money 
       borrowed
    Years_Of_Retirement : integer
       The number of years for which the person will be retired which
       is assumed known.
    NumberYDraws : integer
       The number of draws for Monte Carlo integration of earnings 
       distribution divided by 2 (using reflection accelerator)
       
    Returns
    -------
    SavingsRate: floating point
       The optimal fraction of available resources "saved"
    Savings: floating point
       The optimal dolar value of savings
    LEU: floating point
       Lifetime Expected Utiliity given optimal savings in most recent period 
    
Created on Thu Jul 11 12:00:49 2019

@author: wtdickens
"""
    import numpy as np
    from Period_T_Utililty import Period_T_Utility as Period_T_Utility
    from Backward_Optimize import Backward_Optimize as Backward_Optimize

    # Call routine to compute the utility consumption in retirement 
    #  corresponding to each possible level of wealth going into retirement
    FinalPeriodUtilityVector=Period_T_Utility(Person,Years_of_Retirement)
    
    # Now create current period utility matrix for final year of work
    # as a matrix with dimensions equal to the number of permanent income
    # catagorie by the number of wealth catagories
    NPY=Person.PermYMat.shape[0]  # Number of permanent income states
    NW=Person.WealthMat.shape][0] # Number of wealth states
    CurrentPeriodUtility=np.matrix(np.zeros((NPY,NW)))
    
    # Loop over states (PermY x Wealth) and perform Monte Carlo Integration
    # of income innovations to fill in utility(state) matrix
    for ipy in range(NPY):
        for iw in range(NW):
            # Draw random terms for integration over income innovation
            RandomY=np.random.normal(size=NumberYDraws)
            UtilSum=0
            for ir in range(NumberYDraws):
                # Reflect each random draw to the opposite side of the mean
                # for M-C integration accelerator
                ####### {NOTE: May not need to do M-C integration here. If we 
                # specify C(Y) function we may be able to integrate using
                # simple multi-point quadrature as there are small values
                # that work well for exponential type distributions}
                for sign in [-1,1]:
                    YearFlag=1  # Setting for final year of work
                    # Compute optimal consumption given state
                    OptC,LastPeriodUtility=ComputeOptimalC(
                                          Person.WealthMat[iw,RetirementAge-1],
                                          Person.PermYMat[ipy,RetirementAge-1],
                                          RandomY[ir]*sign,
                                          FinalPeriodUtilityVector,
                                          YearFlag)
                    ######### (NOTE: This needs to be augmented with the
                    # Utility from the likely states in next period)
                    UtilSum+=(OptC**(1-Person.crra)-1)/(1-Person.crra)
            # Average Utility over all Monte-Carlo draws (2*NumberYDraws)
            # and store in CPU matrix
            CurrentPeriodUtility[ipy,iw]=.5*UtilSum/NumberYDraws
            
    # Now loop backwards over lifetime to get to current period
    for year in range(RetirementAge-2,Person.Age,-1):
        for ipy in range(NPY):
            for iw in range(NW):
                # Draw random terms for integration over income innovation
                RandomY=np.random.normal(size=NumberYDraws)
                UtilSum=0
                for ir in range(NumberYDraws):
                    # Reflect each random draw to the opposite side of the mean
                    # for M-C integration accelerator
                    # {NOTE: May not need to do M-C integration here. If we 
                    # specify C(Y) function we may be able to integrate using
                    # simple multi-point quadrature as there are small values
                    # that work well for exponential type distributions}
                    for sign in [-1,1]:
                        # Set year flag to the value for years between first
                        # and last 
                        YearFlag=0
                        # Compute optimal consumption given state
                        OptC,LastPeriodUtilityMatrix=ComputeOptimalC(
                                          Person.WealthMat[iw,RetirementAge-1],
                                          Person.PermYMat[ipy,RetirementAge-1],
                                          RandomY[ir]*sign,
                                          LastPeriodUtilityMatrix,
                                          YearFlag)
                        
                        UtilSum+=(OptC**(1-Person.crra)-1)/(1-Person.crra)
                # Average Utility over all Monte-Carlo draws (2^NumberYDraws)
                # and store in CPU matrix
                CurrentPeriodUtility[ipy,iw]=.5*UtilSum/NumberYDraws
                
    # Now compute consumption for current year
    YearFlag=-1 # Set year flag to indicate computation for current year
    OptC,LEU=ComputeOptimalC(Person.StartingWealth,
                             Person.Y,
                             0,
                             LastPeriodUtilityMatrix,
                             YearFlag)

    Resources=Person.StartingWealth+Person.Y  # Total available resources
    Savings=Resources-OptC              
    SavingsRate=1-OptC/Resources
    
    return(Savings,SavingsRate,LEU)
    
    
    
        
    
    

