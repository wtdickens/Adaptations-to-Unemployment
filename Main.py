"""
    Main program for Dickens, Triest and Sederberg's work on the impact of income shocks on well being
   
    For now this is a test bed for testing routines
"""
# IMPORTS
import numpy as np
import Compute_Permanent_Y as CPY
import Compute_Wealth_Values as CWV

# "Global" Variables (parameters of the simulation)

Years_of_Retirement= 20   # What it says
N=2    # Number of values taken by permanent income each period
K=5    # Number of possible values for wealth in each period 
       #    Note: K can never be less than 5 for Compute_Wealth_Values to work 
RetirementAge=67 # Assumed retirement age for all individuals
RealRate=.02      # Real rate of return on savings
NumberYDraws =    # Number of draws for Monte Carlo integration of Income
                  #  per year per state divided by 2

# Classes

class People:
    # This class' initialization takes a person's crra, age, education, sex, 
    # work experience, most recent full time annual income and recent 
    # employment history, to computes the 
    # possible values for permanent income and wealth in each remaining
    # period of life.
    
    def __init__(self,crra=25,education=12,sex="m",age=18,
                 experience=-9,MonthsUnemployed=0,StartingWealth=-9
                 ,FulltimeY=-9,Y=-9):
        
        # Create attributes for each incidence of the class
        #   crra is coefficient of relative risk aversion, 
        #   education is years completed
        #   experience is years of work experience
        #   FulltimeY is the most recent full time annual income
        #   Y is income for most recent period
        #   others are self explanitory
        self.crra = crra
        self.education = education
        self.sex = sex
        self.age = age
        self.MonthsUnemployed = MonthsUnemployed
        
        if experience < 0:
            self.experience=age-education
        else:
            self.experience=experience
        
        if FulltimeY<0:
            # If full time incoe is missing assume that it is $60k times
            #  an adjustment for education assuming a rate of return of 
            #  .07 per year completed
            self.FulltimeY=60000*np.exp(.07*(education-12))
        else:
            self.FulltimeY=FulltimeY
            
        if Y<0:
            self.Y=60000*np.exp(.07*(education-12))
        else:
            self.Y=Y
            
        if StartingWealth < 0:
            # If no starting wealth assume constant Y and savings rate
            #  of .16 which is optimal with no risk and RealRate of 2
            #  if people work for 50 years, are retired for 20 and can
            #  purchase a fair anuity on retirement
            self.StartingWealth=(.16*FulltimeY*(np.exp(RealRate*(age-18))-1)
                                 /RealRate)
        else:
            self.StartingWealth=StartingWealth
        
        # Now call function to create matrix of possible permanent income 
        #   values in each period as an Nx(Retirement_Age-Age) matrix
        self.PermYMat=CPY.Compute_Permanent_Y(self.age,
                                          self.education,
                                          self.experience,
                                          self.MonthsUnemployed,
                                          self.sex,
                                          self.FulltimeY,
                                          RetirementAge)
        
        # Finally call function to compute matrix of possible values of 
        #  wealth in each remaining period of life
        self.WealthMat=CWV.Compute_Wealth_Values(self.PermYMat,
                                             StartingWealth,
                                             RetirementAge-age,
                                             K,
                                             RealRate)
        
        self.PYTransMatrix=CompTransMat(self,self.age,self.education,
                                        RetirementAge)
        
        
###############################################################
# Now test ChooseSavings.py

from ChooseSavings import ChooseSavings as ChooseSavings

person1=People()

SavingsRate,Savings,ELifetimeUtility=ChooseSavings(Person1,
                                                   RetirementAge,
                                                   RealRate,
                                                   Years_of_Retirement,
                                                   NumberYDraws)

        
        
        
        
        
