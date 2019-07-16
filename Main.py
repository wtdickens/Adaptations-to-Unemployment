"""
    Main program for Dickens, Triest and Sederberg's work on the impact of 
    income shocks on well being
   
    For now this is a test bed for testing routines
"""
# IMPORTS
import numpy as np
from Compute_Permanent_Y import CompPermY as CompPermY
from Compute_Wealth_Values import ComputeWealthValues as ComputeWealthValues

# "Global" Variables (parameters of the simulation)

Years_of_Retirement= 20   # What it says
N=2    # Number of values taken by permanent income each period
K=5    # Number of possible values for wealth in each period 
       #    Note: K can never be less than 5 for Compute_Wealth_Values to work 
RealRate = .02      # Real rate of return on savings
NumberYDraws = 3    # Number of draws for Monte Carlo integration of Income
                    #  per year per state divided by 2

# Classes

class People:
    # This class' initialization takes a person's crra, age, education, sex, 
    # work experience, most recent full time annual income, recent 
    # employment history, and wealth to computes the 
    # possible values for permanent income and wealth in each remaining
    # period of life. It also computes the Markov transition matrix
    # for the evolution of permanent income over the working life
    
    def __init__(self,crra=25,education=12,sex="m",age=18,
                 experience=-9,MonthsUnemployed=0,StartingWealth=-9
                 ,FulltimeY=-9,Y=-9,YSD=.1,RetirementAge=67):
        
        # Create attributes for each incidence of the class
        #   crra is coefficient of relative risk aversion, 
        #   education is years completed
        #   experience is years of work experience
        #   FulltimeY is the most recent full time annual income
        #   Y is income for most recent period
        #   YSD is the standard dev. of transient shocks to income in %/100
        #   others are self explanitory
        self.crra = crra
        self.education = education
        self.sex = sex
        self.age = age
        self.MonthsUnemployed = MonthsUnemployed
        self.YSD = YSD
        self.RetirementAge = RetirementAge
        
        if experience < 0:
            self.experience = age - education
        else:
            self.experience = experience
        
        if FulltimeY<0:
            # If full time incoe is missing assume that it is $60k times
            #  an adjustment for education assuming a rate of return of 
            #  .07 per year completed
            self.FulltimeY = 60000 * np.exp(.07 * (education - 12))
        else:
            self.FulltimeY = FulltimeY
            
        if Y<0:
            self.Y = 60000 * np.exp(.07 * (education - 12))
        else:
            self.Y = Y
            
        if StartingWealth < 0:
            # If no starting wealth assume constant Y and savings rate
            #  of .16 which is optimal with no risk and RealRate of 2
            #  if people work for 50 years, are retired for 20 and can
            #  purchase a fair anuity on retirement
            self.StartingWealth = (.16 * FulltimeY
                                 * (np.exp(RealRate*(age - 18)) -1)
                                 / RealRate
                                 )
        else:
            self.StartingWealth = StartingWealth

        
        # Now call function to create matrix of possible permanent income 
        #   values in each period as an Nx(Retirement_Age-Age) matrix. 
        # Same function also returns TransMat which is a 3D matrix
        # Each slice is a Markov transition matrix with rows giving probability
        # of transitioning from current state to the possible states in the
        # next period. Each slice is for a different year.
        self.PermYMat,self.TransMat = CompPermY(
                                                self.age,
                                                self.education,
                                                self.experience,
                                                self.MonthsUnemployed,
                                                self.sex,
                                                self.FulltimeY,
                                                RetirementAge
                                                )
        
        # Finally call function to compute matrix of possible values of 
        #  wealth in each remaining period of life
        self.WealthMat = ComputeWealthValues(
                                             self.PermYMat,
                                             StartingWealth,
                                             RetirementAge - age + 1,
                                             K,
                                             RealRate
                                             )
            
###############################################################
# Now test ChooseSavings.py

from ChooseSavings import ChooseSavings as ChooseSavings

person1=People()

SavingsRate,Savings,ELifetimeUtility = ChooseSavings(person1,
                                                     RealRate,
                                                     Years_of_Retirement,
                                                     NumberYDraws)

        
        
        
        
        
