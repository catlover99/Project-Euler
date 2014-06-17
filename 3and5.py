#Project Euler #1: Multiples of 3 and 5
#Find the sum of all the multiples of 3 or 5 below 1000.

lsThree = [0] #List of multiples of 3 below 1000
lsFive = [0] #List of multiples of 5 below 1000

#Calculates multiples of 3 below 1000
def mults3():
	global lsThree
	a = 1
	while 1:
		b = 3*a
		if (b >= 1000):
			break
		else:
			lsThree.append(b)
			a += 1

#Calculates multiples of 5 below 1000
def mults5():
	global lsFive
	a = 1
	while 1:
		b = 5*a
		if (b >= 1000):
			break
		else:
			lsFive.append(b)
			a += 1

mults3() 
mults5()
#Sum the results of the multiple calculations and remove recurring results
print sum(lsThree + list(set(lsFive) - set(lsThree)))


