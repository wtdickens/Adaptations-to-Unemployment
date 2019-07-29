# -*- coding: utf-8 -*-
def SavingsMUtility(Person,year,NextPeriodUtility,indexNextWealth,ipy):
    """
    This routine computes the marginal utility of the next dollar of savings
    at a certain level of savings for a given year, and current wealth and 
    permanent income states. It does this by computing the weighted average 
    of the marginal utility of consumption over posible future permanent 
    income states. 
    
    Parameters
    ----------
    Person : an instance of the class people
       This class contains all the information on the person needed. See
       Main.py where it is defined. The attributes used in this routine are
       Person.TransMat : 3D Numpy array
           Each slice of this is a Markov transition matrix from all
           permanent income states for one year to all permanent income states
           in the next year.
       Person.WealthMat : numpy matrix
           Each column lists the discrete value that wealth passed to the next
           period can take in ascending order. Each column contains the values
           for one year of the subjecs working life.
       Person.PermYMat : numpy matrix
           Each column lists possible values for permanent annual income
           in asssending order. Each column corresponds to a different year
           in the person's working life.
       Person.RetirementAge : integer
           Age of retirement for this person
       Person.Age : integer
           Person's age in years
    year : integer
       Index of the year in the working life being analyzed. A -1 indicates
       the last year before retimrement
    NextPeriodUtility : numpy matrix
       A Matrix containing the expected utility values associated with 
       each possible end state for the period being analyzed. When analyzing
       the final working year this is a numpy vector containing the utility 
       values associated with each final level of wealth.
    indexNextWealth : integer
       The index of the wealth state for which the maringal utility is being
       computed. 
    ipy : integer
       Index for the current permanent income state
       
    Returns
    -------
    MarginalUtility : floating point
       The expecred marginal utility of an extra dollar in savings in the 
       year being analyzed
       
    Created on Mon Jul 15 13:52:51 2019

    @author: wtdickens
    """
    # The marginal dollar of savings simply increases the probability of 
    # obtaining the next highes savings state the marginal utility gain from
    # a dollar spent on savings is the difference in the total utility between
    # the lower and higher level divided by the dollar difference between
    # savings at those two levels. Thus we first compute the dollar difference
    # in savings which is the same for all the different permanent income
    # states. Then we compute the average marginal utility for each 
    # permanent income state weighted by the probability of transitioning
    # to that state. Finally we divide the average by the dollar difference.
    
    DollarDif = (Person.WealthMat[indexNextWealth + 1,year]
                - Person.WealthMat[indexNextWealth,year])
    
    # If computation is for other than last year of working life 
    # NextPeriodUility will be a matrix rather than a vector
    if NextPeriodUtility.shape[1] > 1: 
        # Computations for other than last year of working life
        
        # Loop over possible values for permanent income in next period
        # to sum up weighed values of marginal utility at different levels
        # of permanent income
        MUSum = 0
        for i in range(Person.PermYMat.shape[0]):
            MUSum += (Person.TransMat[ipy,i,year] 
                    * (NextPeriodUtility[ipy,indexNextWealth + 1]
                    - NextPeriodUtility[ipy,indexNextWealth]))
        MarginalUtility = MUSum / DollarDif
        
    else: 
        # Computation for marginal utility during last working year where
        # future permanent income no longer matters so no need to loop
        MarginalUtility = (NextPeriodUtility[indexNextWealth +1 ]
                          - NextPeriodUtility[indexNextWealth])/DollarDif
        
    return(MarginalUtility)
        
            
            
            
    
    
