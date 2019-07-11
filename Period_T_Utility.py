# -*- coding: utf-8 -*-
import numpy as np
def Period_T_Utility(Person,Years_of_Retirement):
    """
    This routine computes final period utility for each possible state
    of wealth in the last period
    
    Parameters
    ----------
    Person : An instance of the class People 
           See Main.py for definition of the class
           Specifically, this program uses the attributes: 
               coefficient of relative risk aversion  (crra)
               Kx1 np matrix of possible wealth values in period T (WinT)
    Years_Of_Retirement : integer
           The number of years for which the person will be retired which
           is assumed known.
   
    Returns
    -------
    Utility_Vector : an NP matrix
            The matrix contains a utility value corresponding to each 
            possible state of wealth in the last period. 
            
    Created on Tue Jul  2 12:17:27 2019

    @author: wtdickens
    """
    # Create matrix to store utility values for each final wealth state
    Utility_Vector=np.matrix(np.zeros((Person.WealthMat.shape[0],1)))

    for i in range(Person.WealthMat.shape[0]):
        Utility_Vector[i,0]= (Years_of_Retirement*((Person.WealthMat[i,-1]
                            /Years_of_Retirement)**(1-Person.crra)-1)
                            /(1-Person.crra))
    np.set_printoptions(precision=5)
    return(Utility_Vector)
        
    