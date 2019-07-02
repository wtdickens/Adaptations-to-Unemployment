"""
    Main program for Dickens, Triest and Sederberg's work on the impact of income shocks on well being
   
    For now this is a test bed for testing routines
"""
# IMPORTS
import numpy as np
import Compute_Permanent_Y.py
import Compute_Wealth_Values.py

# Global Variables

Years_of_Retirement= 20
N=2    # Number of values taken by permanent income each period
K=5    # Number of possible values for wealth in each period
Retirement_Age=67 # Assumed retirement age for all individuals

# Classes

class People:
    # This class' initialization takes a persons crra, age, education, sex, 
    # work experience, and recent employment history, to computes the 
    # possible values for permanent income and wealth in each remaining
    # period of life.
    
    def __init__(self,crra=.9,education=12,sex="m",age=18,
                 experience=-9,MonthsUnemployed=0,StartingWealth=-9):
        
        # Create attributes for each incidence of the class
        #   crra is coefficient of relative risk aversion, 
        #   education is years completed
        #   experience is years of work experience
        #   others are self explanitory
        self.crra=crra
        self.age=age
        if experience < 0:
            self.experience=age-education
        else:
            self.experince=experience
        self.MonthsUnemployed=MonthsUnemployed
        if StartingWealth < 0:
            StartingWealth=(age-18)*
        
        # Now call function to create matrix of possible permanent income 
        #   values in each period as an Nx(Retirement_Age-Age) matrix
        self.PermYMat=Compute_Permanent_Y(self.age,self.crra,self.experience,
                                          self.MonthsUnemployed)
        
        # Finally call function to compute matrix of possible values of 
        #  wealth in each remaining period of life
        self.WealthMat=Compute_Wealth_Values(self.PermYmat)
        
        
###############################################################
# Now test Period_T_Utility.py

import Period_T_Utility.py

person1=People()

Period_T_Utility(person1)

        
        
        
        
        
