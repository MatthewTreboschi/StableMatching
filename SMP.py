import random
import names
import sys
import bisect

nDocs = int(sys.argv[1]) #number of doctors
nHosp = int(sys.argv[2]) #number of hospitals 

docsRate = [] # docs and hosp with ratings of the others
hospRate = []

docs = [] # simple lists of the docs and hosp to copy to temp 
hosp = []

tempDocs = [] # list that the ratings will pick from and destroy
tempHosp = []

openSlots = []

#generate initial list of docs
for i in range(nDocs):
	docName = names.get_first_name()
	docsRate.append([docName])
	docs.append(docName)

#generate initial list of hospitals
for i in range(nHosp):
	hospName = str(i)
	hospRate.append([hospName])
	hosp.append(hospName)


#generate doctors' ratings
for j in range(nDocs):
	tempHosp = hosp.copy()

	#docs should have 2-5 hospitals ranked. If 2 or less exist, they rank all.	
	nRanks = random.randint(2,5)
	if nHosp >=5:
		nRanks = random.randint(2,5)
	elif nHosp >2:
		nRanks = random.randint(2,nHosp)
	
	
	#docs rank hospitals
	for k in range(nRanks):
		if len(tempHosp)>0:
			r = random.randint(0,nHosp-1-k)
			docsRate[j].append(tempHosp[r])
			tempHosp.pop(r)

#generate hospitals' ratings
for j in range(nHosp):
	tempDocs = docs.copy()	
	
	#hospitals should have 
	hospRankn = (int(nDocs/nHosp)+1) * 2
	nRanks = random.randint(hospRankn-2,hospRankn+1)
	openSlots.append(int(nRanks/2))

	
	#hospitals rank docs
	for k in range(nRanks):
		if len(tempDocs)>0:
			r = random.randint(0,nDocs-1-k)
			hospRate[j].append(tempDocs[r])
			tempDocs.pop(r)

print()
print("Doctor's ratings")
for i in range(nDocs):
	print (*docsRate[i], sep = "\t\t")

print()
print("Hospital's ratings")
for i in range(nHosp):
	print (*hospRate[i], sep = "\t\t")

print()
print("Open slots per Hospital")
print(*openSlots, sep = "\t")

def regretCalc(hApplicants):
	regret = 0
	selectCount = 0
	for i in range(len(hApplicants)-1):
		for j in range(len(hApplicants[i])):
			regret += hApplicants[i][j]-j-1
			selectCount-=-1
	regret = regret/selectCount
	return regret

def printMatch(hApplicants, hospRate):
	print()
	print("Results:")
	for i in range(len(hApplicants)-1):
		for j in range(len(hApplicants[i])):
			if hApplicants[i][j]<len(hospRate[i])-1:
				hApplicants[i][j] = hospRate[i][hApplicants[i][j]]
			else:
				hApplicants[i][j] = "Nobody"
	for i in range(len(hApplicants)):
		print(str(i), *hApplicants[i], sep = "\t\t")
	



def StableMatch(docs, docsRate, hospRate, openSlots):
	hApplicants = [] # list of the top applicant for each hospital
	noMatch = docsRate.copy() # list of the mattchless doctors
	matched = []
	bumpCount = 0

	# fill hApplicants with below lowest rank doctors
	for slot in range(len(openSlots)):
		hApplicants.append([])
		for i in range(openSlots[slot]):
			hApplicants[slot].append(len(hospRate[slot]))
	hApplicants.append([])
	#apply
	while len(noMatch) > 0:
		doc = noMatch[0].copy()
		matched.append(doc)
		noMatch.pop(0)
		choiceHosp = int(doc[1])
		
		#check
		try:
			rateDoc = hospRate[choiceHosp].index(doc[0])	
		except:
			rateDoc = len(hospRate[choiceHosp]) + 1
		bisect.insort(hApplicants[choiceHosp], rateDoc)
		#bump
		bump = hApplicants[choiceHosp].pop()
		if len(hospRate[choiceHosp]) != bump: # if the person bumped wasn't nobody
			bumpCount-=-1
			if len(hospRate[choiceHosp]) > bump: # if 
				bump = docs.index(hospRate[choiceHosp][bump]) 
				bumped = docsRate[bump]
			else:
				bumped = doc
			bumped.pop(1)
			if len(bumped)==1: # if the person bumped has no options left
				hApplicants[-1].append(bumped)
			else:
				noMatch.append(bumped)
	print("Average regret per selection for Doctors: " + str(bumpCount/len(docsRate)))
	print("Average regret per selection for hospitals: " + str(regretCalc(hApplicants)))
	
	printMatch(hApplicants, hospRate)



StableMatch(docs, docsRate, hospRate, openSlots)



