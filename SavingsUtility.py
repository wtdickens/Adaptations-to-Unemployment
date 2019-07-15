# -*- coding: utf-8 -*-
def SavingsUtility(Person,year,NextPeriodUtility,indexNextWealth,ipy):
    """
    This routine computes the marginal utility of the next dollar of savings
    at a certain level of savings for a given year, and current wealth and 
    permanent income states. It does this by computing the weighted average 
    of the marginal utility of consumption of posible future permanent 
    income states. 
    
    Parameters
    ----------
    Person : an instance of the class people
       This class contains all the information on the person needed. See
       Main.py where it is defined. It is Person.TransMat that is used
       here. That is a three dimensional numpy array giving the Markov
       transition matrix from the current permanent income state to the
       next permanent income state for each year of the person's working life.
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
       

    Created on Mon Jul 15 13:52:51 2019

    @author: wtdickens
    """

