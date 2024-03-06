
from PIL import Image
import numpy as np


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

def direct(a):
    mat = np.array(a)
    
    b = mat.transpose()
    
    return b


#压缩：个数+比特信息
with open("D:\\1.txt", 'r') as file:   #得到图像弓形数组向量
    for line in file:
        line = line.strip()
        data = line.split(" ")

#编码
count=0
str=""
with open("D:\\result2.txt", 'r') as file:  #根据动态规划结果将图像向量转为01比特
    for line in file:
        line = line.strip()
        tmp = line.split(" ")
        for i in range(int(tmp[0])):
            binary_str = bin(int(data[count+i]))[2:]
            binary_str = '0' * (int(tmp[1]) - len(binary_str)) + binary_str
            
            str+=binary_str
        count+=int(tmp[0])

dna=dna_encode(str)
stl = split_string_by_length(dna, 150)


out=open("D:\\direct.txt","w")
for i in range(len(stl)//150):
    a=[]
    for j in range(150):
        lst = list(stl[i*150+j])#将序列转成列表
        a.append(lst)#加入总列表
    data = np.array(a) #将DNA列表转成矩阵        
    new_data=direct(data) #数据交织（转置）
    for j in range(len(new_data)): #对于每一行（转置后的每一条DNA序列）
        name_str = ''.join(x if x else "" for x in new_data[j])#将矩阵转为字符串 
        out.write(name_str+"\n")
tmp=len(stl)-len(stl)//150*150
a=[]
for i in range(tmp):
    out.write(stl[len(stl)//150*150+i]+"\n")
out.close()



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:13:25 2024

@author: 11353
"""
import random
import numpy as np

def mutate(string):
    a=b=c=0
    dna = list(string)
    for index, char in enumerate(dna):
        if (random.random() <= 0.02):
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
file=open("D:\\direct.txt")
new=open('d:\\mutation_dna.txt',"w")
for line in file.readlines():
    new.write(mutate(line.split("\n")[0])+"\n")

new.close()



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:14:04 2024

@author: 11353
"""
def dna_decode(dna):
    DNA_encoding = {"A": "00","T": "01","C": "10","G": "11"}
    bin_list = []
    for num in dna:
        for key in list(DNA_encoding.keys()):
            if num == key:
                bin_list.append(DNA_encoding.get(key))

    return "".join(bin_list)

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



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:15:39 2024

@author: 11353
"""
import numpy as np
from PIL import Image
import re
import numpy as np

import random

def direct(a):
    mat = np.array(a)
    
    b = mat.transpose()
    
    return b

file=open("D:\\process.txt")
stl=[]
for l in file.readlines():
    if(l[0]!=">"):
        stl.append(l.rstrip("\n"))
out=open("D:\\jie_direct.txt","w")
for i in range(len(stl)//150):
    a=[]
    for j in range(150):
        lst = list(stl[i*150+j])#将序列转成列表
        a.append(lst)#加入总列表 
    data = np.array(a) #将DNA列表转成矩阵        
    new_data=direct(data) #数据交织（转置）
    for j in range(len(new_data)): #对于每一行（转置后的每一条DNA序列）
        name_str = ''.join(x if x else "" for x in new_data[j])#将矩阵转为字符串 
        out.write(name_str+"\n")
tmp=len(stl)-len(stl)//150*150
a=[]
for i in range(tmp):
    out.write(stl[len(stl)//150*150+i]+"\n")
out.close()   





# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:18:21 2024

@author: 11353
"""
from PIL import Image
import numpy as np

from PIL import Image
import numpy as np

def dna_decode(dna):
    DNA_encoding = {"A": "00","T": "01","C": "10","G": "11"}
    bin_list = []
    for num in dna:
        for key in list(DNA_encoding.keys()):
            if num == key:
                bin_list.append(DNA_encoding.get(key))

    return "".join(bin_list)


file=open("D:\\jie_direct.txt")
string=""
for line in file.readlines():
    string+=line.rstrip("\n")

# 去掉空格
str=dna_decode(string)



count=0
d=[]
with open("D:\\result2.txt", 'r') as file:
    for line in file:
        line = line.strip()
        tmp = line.split(" ")
        a=int(tmp[0]);b=int(tmp[1])
        for i in range(a):
            d.append(int(str[count+i*b:count+(i+1)*b],2))
        count+=(a*b)
    
#弓形向量转为矩阵，恢复图像
col=256;row=256;kk=0
matrix = np.empty(shape=(row, col),dtype=int)
for i in range(col):
    if(i%2==0):
        for j in range(row):
            matrix[i][j]=d[kk] 
            kk+=1
    else:
        for j in range(row-1,-1,-1):
            matrix[i][j]=d[kk] 
            kk+=1
     
image = Image.fromarray(np.uint8(matrix))
image.save('D:\\01.bmp')



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:24:45 2024

@author: 11353
"""


# 示例用法：
import pywt
import numpy as np
import cv2

kkk="D:\\01.bmp"
img = cv2.imread(kkk)
median = cv2.medianBlur(img, 3)
cv2.imwrite("D:\\01_filter.bmp", median)
