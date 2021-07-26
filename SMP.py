# main program

import random
import names
import sys
import bisect
from SMPhelper import *

nDocs = int(sys.argv[1]) #number of doctors
nHosp = int(sys.argv[2]) #number of hospitals 
n = int(sys.argv[3]) #number of iterations


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
