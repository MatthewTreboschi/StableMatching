# StableMatchingAnalysis
The file was named stable marriage analysis before we moved on to hospitals and residents.
The Stable Marriage problem is a subset of the hospitals and residents problem where the amount of hospitals and residents are equal and every hospital only has 1 slot and every doctor/hospital ranks all others

Project by Matthew Treboschi and Dan Ksel
This code was designed to test the efficiency of the Gale Shapely algorithm
at creating a stable solution to the Hospital/Residency Problem with 
minimal regret where regret is defined as the average rank of the pick that
each participant recieved minus the best rank they could have gotten.

# Requires:
pip install names

# Run instructions
Run the SMP.py with 3 arguments:
  the number of doctors for your simulation,
  the number of hospitals,
  and the number of iterations you want the program to run

An example might look like this:

python SMP.py 6 4 1
