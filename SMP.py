import random
import names
import sys

n = int(sys.argv[1]) #number of each boys and girls

boysrate = [] # boys and girls with ratings of the others
girlsrate = []

boys = [] # simple lists of the boys and girls to copy to temp 
girls = []

tempboys = [] # list that the ratings will pick from and destroy
tempgirls = []

#generate initial list of boys and girls
for i in range(n):
	boyName = names.get_first_name(gender='male')
	girlName = names.get_first_name(gender='female')

	boysrate.append([boyName])
	girlsrate.append([girlName])

	boys.append(boyName)
	girls.append(girlName)

#generate ratings
for j in range(n):
	tempboys = boys.copy()
	tempgirls = girls.copy()
	for k in range(n):
		r = random.randint(0,n-1-k)
		print(n-1-k)
		boysrate[j].append(tempgirls[r])
		tempgirls.pop(r)

		r = random.randint(0,n-1-k)
		girlsrate[j].append(tempboys[r])
		tempboys.pop(r)

for i in range(n):
	print (*boysrate[i], sep = "\t")

print()

for i in range(n):
	print (*girlsrate[i], sep = "\t")





