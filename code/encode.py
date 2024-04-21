import numpy as np
import random
def dna_encode(binary):
    
    
    DNA_encoding = {"00": "A","01": "T","10": "C","11": "G"}
    binary_list = [binary[i: i+2] for i in range(0, len(binary), 2)]
    
    DNA_list = []
    for num in binary_list:
        for key in list(DNA_encoding.keys()):
            if num == key:
                DNA_list.append(DNA_encoding.get(key))

    return "".join(DNA_list)

def split_string_by_length(string, length):
    result = []
    for i in range(0, len(string), length):
        result.append(string[i:i+length])
    return result

#compress
with open("D:\\1.txt", 'r') as file: 
    for line in file:
        line = line.strip()
        data = line.split(" ")

#dp-encode 01 bits
count=0
str=""
with open("D:\\result2.txt", 'r') as file:  
    for line in file:
        line = line.strip()
        tmp = line.split(" ")
        for i in range(int(tmp[0])):
            binary_str = bin(int(data[count+i]))[2:]
            binary_str = '0' * (int(tmp[1]) - len(binary_str)) + binary_str
            
            str+=binary_str
        count+=int(tmp[0])

dna=dna_encode(str)

dna+="A"*(150-(len(dna)-len(dna)//150*150))  #adjust last sequence to 150 nt
numbers = list(range(0, len(dna)))
random.seed(10)
random.shuffle(numbers)
new=""
for i in range(len(numbers)):
    new+=dna[numbers[i]]

stl = split_string_by_length(new, 150)
out=open("D:\\direct_2.txt",'w')
for k in stl:
    out.write(k+"\n")
out.close()


