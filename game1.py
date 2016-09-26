import msvcrt
import time

f1=10
f2=20
f3=30

count=0
count1=10
count2=20
print"press enter key to proceed!!"

raw_input()
s_time=time.time()

while(1):
		key=msvcrt.getch()
		if key=='d':
					count=count+1
					print"-->",
					if count==f1:
								print"turn down"
								break
					else:
								print"u lost"
while(1):
		key1=msvcrt.getch()
		if key1=='s':
						count1=count1+1
						print"                                   "
						print"                                      |"
						if count1==f2:
									print"                            turn right"
									print"                                       ",
									break
						else:
									print"u lost"
while(1):
		key2=msvcrt.getch()
		if key2=='d':

						count2=count2+1
						print "-->",

						if count2==f3:
									break
						else:
									print"u lost"
time_elapsed=time.time()-s_time
print"u have completed the game"
print"the time taken is"+str(time_elapsed)

