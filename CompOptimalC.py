# -*- coding: utf-8 -*-
def CompOptimalC(Person,RealRate,RandomY,NextPeriodUtility,YearFlag):
    """
    The routine takes the utility by state matrix for the next year, and for 
    a specific level of resources available in the year being analyzed 
    computes the optimal value for consumption. It then computes the
    value of utility from that consumption, adds it to the expected
    future utility based on the current state and the likely future states
    and returns that in all but the current year. For the current year it
    reports the value of consumption as well as the total lifetime expected
    utility.
    
    Parameters
    ----------
    person : an instance of the class people
       This class contains all the information on the person needed. See
       Main.py where it is defined
    RealRate : floating point
       The real rate of return on savings during the person's life. If no 
       credit constraints this is also the expected interest on money 
       borrowed
   NextPeriodUtility : Numpy Matrix
       A Matrix containing the expected utility values associated with 
       each possible end state for the period being analyzed. When analyzing
       the final working year this is a numpy vector containing the utility 
       values associated with each final level of wealth.
   YearFlag : Integer
       This flat is equal to:  1 if it is the last working year that is being
                                   evaluated, 
                              -1 if it is the current year that is being
                                   evaluated, and
                               0 otherwise
  
    Returns
    -------
    UtilityMatrix : numpy matrix
        If the YearFlag is 1 or 0 this is the only return. It is a matrix
        containing the expected utility associated with each possible state
        of permanent income and wealth. 
    LEU : floating point
       If the YearFlag is -1 this is reported. It is the Lifetime Expected 
       Utiliity given optimal savings in most recent period 
   OptimalConsumpton : floating point
       Only reported whe YearFlag = -1. It is the optimal level of consumption 
       for the current year for the person being analyzed
       
       Created on Fri Jul 12 10:46:25 2019

    @author: wtdickens
    """

