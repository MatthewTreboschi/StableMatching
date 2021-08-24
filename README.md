# StableMatchingAnalysis

Project by Matthew Treboschi and Dan Ksel

We noticed that the Gale Shapely Algorithm, while it always produces a stable result, doesnt produce the most satisfactory result. 
There exists a simple example case when trying to match 4 heteroromantic couples. If each of the boys has a different first choice 
girl who has that boy as their last choice and each of the girls has a different first choice boy who has that girl as their last 
choice then the 2 stable solutions given by the Gale Shapely Algorithm are to give 1 gender all of their first picks and give the 
other gender all of their last picks, so this algorithm can totally screw over 1 side and tank the overall match satisfaction. In 
the same circumstances there could exist a solution where everybody gets their 2nd choice which is both a far more fair and an 
overall more satisfying match

This code was designed to test the efficiency of the Gale Shapely algorithm
in terms of optimizing the satisfaction when creating stable solutions to the Hospital/Residency Problem. 
This is done by quantifying that satisfaction with a "regret" factor.
Regret is defined as the average rank of the pick that
each participant recieved minus the best rank they could have gotten 
(there are circumstances where its first choice might not be possible).
For example: getting your first choice has a regret of `1 - 1 = 0` and getting your second choice has a regret of `2 - 1 = 1`, 
so the further down your choices you get, the higher your regret.

# Requires:
pip install names

# Run instructions
Run the SMP.py with 3 arguments:
  the number of doctors for your simulation,
  the number of hospitals,
  and the number of iterations you want the program to run

An example might look like this:

python SMP.py 6 4 1
