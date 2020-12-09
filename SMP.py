"""Project by Matthew Treboschi and Dan Ksel
This code was designed to test the efficiency of the Gale Shapely algorithm
at creating a stable solution to the Hospital/Residency Problem with 
minimal regret where regret is defined as the average rank of the pick that
each participant recieved minus the best rank they could have gotten.

This code may require "pip install names"
"""


import random
import names
import sys
import bisect
from SMPhelper import *

nDocs = int(sys.argv[1]) #number of doctors
nHosp = int(sys.argv[2]) #number of hospitals 
n = int(sys.argv[3])


docRegret = 0
hospRegret = 0


for i in range(n):
	docsRate = [] # docs and hosp with ratings of the others
	hospRate = []

	docs = [] # simple lists of the docs and hosp to copy to temp 
	hosp = []

	tempDocs = [] # list that the ratings will pick from and destroy
	tempHosp = []

	openSlots = []

	generateInitalLists(nDocs, nHosp, docsRate, docs, hospRate, hosp)
	generateDocsNHosp(tempHosp, tempDocs, docsRate, hospRate, hosp, docs, openSlots)
	printRatings(docsRate, hospRate, openSlots)
	regret = StableMatch(docs, docsRate, hospRate, openSlots)
	docRegret += regret[0]
	hospRegret += regret[1]
docRegret = docRegret/n
hospRegret = hospRegret/n
print("Final Doctor Regret: "+str(docRegret))
print("Final Hospital Regret: "+str(hospRegret))
