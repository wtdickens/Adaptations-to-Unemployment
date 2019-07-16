# -*- coding: utf-8 -*-
import numpy as np
def CompPermY(age,ed,experience,unemployment,sex,Y,RetirementAge):
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
    RetirementAge : integer
        Retirement age in years

    Returns
    -------
    PYMat : numpy matrix
        Each colulmn of the matrix contains the possible values for permanent 
        income in each remaining year of the person's working life
    PYTransMat : numpy 3 dimensional array
        This array has dimensions: 
        # permanent Y States x # permanent Y States x YearsLeft in Working Life
        Each 2D slice of this array is the transition matrix between states
        for that year. 
        ##########(NOTE: We are going to have to simplify the transition
        matrix if we are going to avoid having yet another big loop in the 
        middle of what is already a deep nesting of loops)

    Created on Tue Jul  2 18:43:22 2019

    @author: wtdickens
    """
    
    # For now this progrm creates a 2x(67-age) matrix with $60,000 in the upper
    # row and 0 in the lower row
    
    PYMat=np.mat(np.zeros((2,RetirementAge - age)))
    for i in range(RetirementAge - age):
        PYMat[1,i]=60000
        PYMat[0,i]=0
    
    # This creates teh transi
    TransMat=np.zeros((2,2,RetirementAge - age))
    for i in range(RetirementAge - age):
        TransMat[0,0,i]=.1
        TransMat[0,1,i]=.9
        TransMat[1,0,i]=.9
        TransMat[1,1,i]=.1        
    
    return(PYMat,TransMat)
        

