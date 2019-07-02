# -*- coding: utf-8 -*-
def Period_T_Utility(Person)
    """
    
    This routine computes final period utility for each possible state
    of wealth in the last period
    
    Parameters
    ----------
    Person : An element of the class People 
           Specifically, this program uses the attributes: 
               coefficient of relative risk aversion  (crra)
               Kx1 np matrix of possible wealth values in period T (WinT)
   
    Returns
    -------
    Utility_Vector : an NP matrix
            The matrix contains a utility value corresponding to each 
            possible state of wealth in the last period. 
            
    Created on Tue Jul  2 12:17:27 2019

    @author: wtdickens
    """
    # Create matrix to store utility values for each final wealth state
    Utility_Vector=np.matrix(np.zeros((Person.WinT.size[0],1))
    
   
    for i in range(Person.WinT.size[0]):
        Utility_Vector[i,1]= Years_of_Retirement*((Person.WinT[i,1]
                            /Years_of_retirement)**(1-Person.crra)-1)
                            /(1-Person.crra)
    
    return(Utility_Vector)
        
    