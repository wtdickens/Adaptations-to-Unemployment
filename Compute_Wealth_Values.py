# -*- coding: utf-8 -*-
def Compute_Wealth_Values(IncomeMatrix, StartingWealth, YearsLeft):
    """
    This routine takes a person's starting wealth and their income matrix
    and computes possible values for wealth in each remaining year of their
    working life. 
    
    Parameters
    ----------
    IncomeMatrix : numpy matrix
        A matrix where each column is the possible income values for each 
        year of the person's working life
    StattingWealth: integer
        The value of the persons wealth at the start of the first period
    YearsLeft: integer
        Years left in person's working life
        
    Returns
    -------
    WealthMat : numpy matrix
        A matrix with one column for each remaining year of the person's
        working life. Each element in the column is a value that could be
        taken by a person's wealth in the corresponding year.

    Created on Tue Jul  2 13:29:48 2019

    @author: wtdickens
    """
    
    # For now this computes the optimal path assuming a constant income  
    # Equal to the median income for the entire lifetime. It assigns that 
    # value in each period to the median and then computes the  the other
    # values as an exponential function centered at the median value
    
    if IncomeMatrix.size[0] % 2 == 1:
        MedIndex = IncomeMatrix.size[0] / 2 + .5
        MeanInc = np.mean(IncomeMatrix[MedIndex,:])
    else:
        MedIndex=IncomeMatrix.size[0] / 2 
        MeanInc=np.mean(IncomeMatrix[MedIndex:MedIndex+1,:])
   
    # Create numpy matrix to store results (K is a global variable)    
    WealthMat=np.matrix(np.zeros(K,YearsLeft))
    
    # Compute the index of the row(s) to place the optimal value in
    if K % 2 == 1:
        OptIndex = K / 2 + .5
    else:
        OptIndex = K / 2
    
    # Loop over years left in life
    for year in range(YearsLeft): 
        # Compute wealth assuming a savings rate of .16 RealRate is global
        OptW = MeanInc * .16 * (np.exp(RealRate * year) - 1) / RealRate
        
        for j in range(K):
            Increment = OptW / (OptIndex - 2)
            WealthMat[i,year] = (i - 1) * increment 
        
    return(WealthMat)
            
        
        
    
    
    

