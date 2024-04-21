import random
import numpy as np

#mutation_dna.txt is simulate DNA storage errors result 

out=open("D:\\process.txt","w")
file=open("D:\\mutation_dna.txt")
for l in file.readlines():
    l=''.join(l.split())
    l=l.rstrip("\n")
    length=len(l)
    if(length==150):
        out.write(l+"\n")
    elif(length>150):
        while(length>150):
            l = l[:75] + l[76:]
            length-=1
        out.write(l+"\n")
    else:
        while(length<150):
            l = l[:75] +"C" +l[75:]
            length+=1
        out.write(l+"\n")

out.close()
