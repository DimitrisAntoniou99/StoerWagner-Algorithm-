
import os 

with open("BenchmarkNetwork.txt", "r+") as f:
	with open("input83_774.txt", 'w+') as f1:
		for line in f:
			line=line.rstrip("\n") + ' ' + '1\n' 
			f1.write(line)

#for i in range(y-1):
	#f.append("1")