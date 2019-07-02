# Adaptations-to-Unemployment
This repository holds programs and notes for Dickens, Triest and Sederberg's 
work on savings and consumption when faced with an income shock

The programs solve for optimal behavior in a period zero where the agent
has T more periods to live. It is assumed that total income is equal to an 
i.i.d. period specific value plus permanent income which takes one of N
values. The possible values change each period and are different across 
individuals to accomodate likely lifetime income paths. It is assumed that 
movement between the different states is determined by a Markov process. 
     In period zero the person must decide how much to save to maximize
total lifetime expected utility. It is assumed that wealth takes one of K
values where, again, these values vary across people and across time 
periods. Doing this allows us to accomodate likely life paths while minimizing
the number of states that must be considered in computing lifetime 
expected utiliy. Rather than choosing a specific level of wealth to carry into 
the next period the agent chooses to buy a lottery ticket that gives a 
probability in ending up in one of two adjacent wealth states where the 
probability is equal to the excess of saving over the lower wealth state
divided by the gap between the two states (the lottery is a fair bet). 
     The model is solved backwards from period T. Consumption in that period 
is simply equal to the wealth brought into the period. Utility values for
each wealth levels are computed. Those utility values are then used to compute
the optimal consumption in period T-1 for each of the NK possible states in
period T-1. These values, in turn, are used to compute the optimal choice
in period T-2 and so on back to period 0. 