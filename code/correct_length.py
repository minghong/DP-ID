# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:58:00 2024

@author: 11353
"""
import random
import numpy as np

file=open("new.txt")
new=open('mutation_dna.txt',"w")
for line in file.readlines():
    if(line[0]!=">"):
        new.write(mutate(line.split("\n")[0])+"\n")

new.close()

out=open("new.txt","w")
file=open("mutation_dna.txt")
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


'''
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:58:00 2024

@author: 11353
"""
import random
import numpy as np



out=open("D:\\process.txt","w")
file=open("D:\\mutation.txt")
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
'''
