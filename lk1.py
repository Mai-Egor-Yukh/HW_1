from random import randint
from array import *
import time
from statistics import mean

#start1=time.time()
#если данная строка находится в цикле, общее время работы увеличивается в 4,5 раза
a=[randint(0,1500) for i in range(1000000)] 
b=[0 for i in range(10)]
Itime=[0 for f in range(100)]
for t in range(0, len(Itime)):
    
    #a=[randint(0,1500) for i in range(1000000)]

    start=time.time()

    for i in range(0, (len(a))):
        if (a[i]-899) > 0:
            b[9]+=1
        else:
            b[a[i]//100]+=1
        
    end = time.time()
    Itime[t]=end-start

print("Max time is ", max(Itime))
print("Min time is ", min(Itime))
print("Average time is ", mean(Itime))

#end1=time.time()

#print("Общее время работы ", end1-start1)
