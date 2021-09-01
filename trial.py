import random
TRIALS = 20
resultlist = []
for i in range(TRIALS):
	if random.randint(1,100) >= 72:
		resultlist.append(0)
	elif random.randint(1,100) >= 72:
		resultlist.append(1)
	else:
		resultlist.append(2)

print(sum(resultlist)/TRIALS)