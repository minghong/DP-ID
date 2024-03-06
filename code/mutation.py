import random
import numpy as np

def mutate(string):
    a=b=c=0
    dna = list(string)
    for index, char in enumerate(dna):
        if (random.random() <= 0.01):
            h=random.random()
            if(h<1/3):
                a+=1
                dna[index]=sub(dna[index])
            elif(h<2/3):
                b+=1
                dna[index]=""
            else:
                c+=1
                dna[index]+=insert()
    return "".join(dna)



def sub(base):
    suiji=random.randint(0,8)
    if(base=="A"):    
        if(suiji<3): return 'T'
        if(suiji<6): return 'C'
        if(suiji<9): return 'G'
    if(base=="G"):
        if(suiji<3): return 'T'
        if(suiji<6): return 'C'
        if(suiji<9): return 'A'
    if(base=="C"):
        if(suiji<3): return 'T'
        if(suiji<6): return 'G'
        if(suiji<9): return 'A'
    if(base=="T"):
        if(suiji<3): return 'G'
        if(suiji<6): return 'C'
        if(suiji<9): return 'A'

    
def insert():
    suiji=random.randint(0,3)
    if(suiji==1): return 'T'
    if(suiji==2): return 'C'
    if(suiji==3): return 'G'
    if(suiji==0): return 'A'


s=0
d=0
ins=0
file=open("D:\\jie_direct.txt")
new=open('d:\\mutation_dna.txt',"w")
for line in file.readlines():
    new.write(mutate(line.split("\n")[0])+"\n")

new.close()

