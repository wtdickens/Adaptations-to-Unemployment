# -*- coding: utf-8 -*-
def Compute_Permanent_Y(age,ed,experience,unemployment,sex,Y):
    """
    Takes age, years of education, years of job experience, months of 
    unemployment, sex and Fulltime income to compute a matrix of possible
    values for permanent income in each remaining year in person's
    working life.

    Parameters
    ----------
    age : integer
        person's age
    ed : integer
        years of education completed
    experience : integer
        full years of job experience
    unemployment : integer 
        months of unemployment in previous 12 months
    sex : character
        m for male, f for female
    Y : integer
        Fulltime equivalent annual income

    Returns
    -------
    PYMat : numpy matrix
        Each colulmn of the matrix contains the possible values for permanent 
        income in each remaining year of the person's working life

    Created on Tue Jul  2 18:43:22 2019

    @author: wtdickens
    """
    
    # For now this progrm creates a 2x(67-age) matrix with $60,000 in the upper
    # row and 0 in the lower row
    
    PYMat=np.mat(np.zeros((2,67-age)))
    for i in range(67-age):
        PYMat[0,i]=60000
        PYMat[1,i]=0
    
    return(PYMat)
        

