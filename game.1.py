import mvcrt
import time

f1=5
f2=10
f3=5

count=0
count1=0
count2=0
print"press enter key to proceed!!"

raw_input()
s_time=time.time()

while(1)
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print"-->",
		if count=f1:
			print"turn down"
			break
		else:
			print"u lost the game"
			exit(1)
while(1):
	key1=msvcrt.getch()
		if key1=='s' :
			count1=count1+1
			print"         |",
			print"         |",
			print"         ^",
			if count1=f2:
				print"turn right"
				break
			else:
				print"u lost the game"	
				exit(1)
while(1):
	key2=msvcrt.getch()
		if key2=='d':
			count2=count2+1
			print"-->",
			if count2=f3:
				print"u won thw game"
				break
			time_elapsed=time.time()-s_time
			print"u have completed the game"
			print"the time taken is"+str(time_elapsed)

