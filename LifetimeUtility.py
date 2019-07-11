"""
    This set of routines takes as input a function that relates current wealth 
    and permanent income to savings in each year of life and returns total  
    discounted lifetime utility. It calls a function IncomeProcess that is 
    defined outside the program that gives actual income in each period of 
    life as a function ofstarting permanent income and age. 


    (Input) StartAge  -- Starting age of person in years
            Discount  -- The discount rate to be used  to compute utility
            StartPY   -- Starting permanent income
            StartW    -- Starting wealth
            FinalPD   -- Discount rate to use on final year (will be >1)

    (Calls) IncomeProcess   -- This function takes inputs StartAge and StartPY
                                and returns income in each year of life
            Savings         -- This function takes inputs Income, Wealth,
                                Age, and Discount and returns a savings rate

    (Returns)   LifetimeUtil     -- Total discounted lifetime utility
"""

def LiftimeUtility(StartAge,Discount,StartPY,StartW,FinalPD,
                   IncomeProcess,Savings):






