#number of cpu usage
#import the time module
import time
#import os
import os
CPU_CORE=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
#Use print to see the result
print("CPU Usage = " CPU_CORE)
#number of ram usage,disk usage
mem=str(os.popen('free -d -m').readlines())
#find the capital T
D_ind=mem.index('T')
#remove unwanted data and give as disk usage 
mem_G=mem[D_ind+14:-4]
S1_ind=mem_G.index(' ')
mem_D=mem_G[0:S1_ind]
#we should find the index of first space and than take the used memory and free memory
mem_G1=mem_G[S1_ind+8:]
S2_ind=mem_G1.index(' ')
mem_U=mem_G1[0:S2_ind]
mem_F=mem_G1[S2_ind+8:]
#to see the time 
time.time()
#use sleep funtion to see the result in every 5 sec.
for i in range (0,5)
print(i)
time.sleep(5)
#print the result
print 'Summary = ' + mem_G
print 'Disk Memory = ' + mem_D +' MB'
print 'Used Memory = ' + mem_U +' MB'
print 'Free Memory = ' + mem_F +' MB'

