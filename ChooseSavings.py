# -*- coding: utf-8 -*-
def ChooseSavings(Person,RetirementAge,RealRate,Years_of_Retirement):
"""
    This routine takes the information on a person and computes the optimal
    savings rate for the most recent year of that person's life as a function
    of their current wealth, their current permanent income, and 
    characteristics that might affect their future earnings and utility of
    income. 
    
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
       
    Returns
    -------
    SavingsRate: floating point
       The optimal savings rate for this person in the most recent year
    Savings: floating point
       The optimal dolar value of savings
    LEU: floating point
       Lifetime Expected Utiliity given optimal savings in most recent period 
    
Created on Thu Jul 11 12:00:49 2019

@author: wtdickens
"""
    from Period_T_Utililty import Period_T_Utility as Period_T_Utility
    from Backward_Optimize import Backward_Optimize as Backward_Optimize

    # Call routine to compute the utility consumption in retirement 
    #  corresponding to each possible level of wealth going into retirement
    FinalPeriodUtilityVector=Period_T_Utility(Person,Years_of_Retirement)

    
    # Loop over age backwards from Retirement age to the person's current age
    for Year in range(RetirementAge-1,-1,-1):
        
    
    

