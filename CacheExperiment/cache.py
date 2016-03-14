import numpy as np
for i in range(42, 48):
	values = []
	with open("CacheDataPrepend.txt") as f:
		for k in range(0, i):
			line = f.readline() #skip
		for k in range(0, 7):
			line = np.array(list(map(int, f.readline().strip().split(","))))
			values.append(line)
			#print(line)
			for l in range(0, 5):			
				line = f.readline()
	for i in range(3, 7):
		values[2] += values[i]
	values[2] = values[2]/5
	myFormattedList = [ '%.2f' % elem for elem in values[2] ]
	for x in myFormattedList:
		print(x, end=",")
	print()
