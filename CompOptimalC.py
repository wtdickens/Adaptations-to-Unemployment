# -*- coding: utf-8 -*-
def CompOptimalC(Person,ipy,iw,year,RealRate,RandomY,NextPeriodUtility):
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
   NextPeriodUtility : numpy matrix
       A Matrix containing the expected utility values associated with 
       each possible end state for the period being analyzed. When analyzing
       the final working year this is a numpy vector containing the utility 
       values associated with each final level of wealth.
  
    Returns
    -------
    UtilityMatrix : numpy matrix
        If the Year is greater than 0 this is the only return. It is a matrix
        containing the expected utility associated with each possible state
        of permanent income and wealth. 
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
    
    #Useful constants
    NPY=person.WealthMat.shape[0]  #Number of wealth states
    
    # Code for years other than the current period and the last working year
    if YearFlag == 0:
        # Loop over the possible permanent income states
        for iPY in range(NPY):
            
    
    
    

