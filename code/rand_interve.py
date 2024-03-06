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
numbers = list(range(0, len(dna)))
random.seed(10)
random.shuffle(numbers)
new=""
for i in range(len(numbers)):
    new+=dna[numbers[i]]

stl = split_string_by_length(new, 150)
out=open("D:\\direct.txt",'w')
for k in stl:
    out.write(k+"\n")
out.close()




def mutate(string):
    a=b=c=0
    dna = list(string)
    for index, char in enumerate(dna):
        if (random.random() <= 0.005):
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


random.seed()
file=open("D:\\direct.txt")
new=open('D:\\mutation_dna.txt',"w")
for line in file.readlines():
    new.write(mutate(line.split("\n")[0])+"\n")

new.close()


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



file=open("D:\\process.txt")
stl=""
for l in file.readlines():
    if(l[0]!=">"):
        stl+=(l.rstrip("\n"))
out=open("D:\\jie_direct.txt","w")
random.seed(10)
dna_new=list(range(0, len(dna)))
for i in range(len(numbers)):

    dna_new[numbers[i]]=stl[i]

out.write("".join(dna_new))
out.close()   


from PIL import Image



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


import cv2
import numpy as np
 
kkk="D:\\01.bmp"
img = cv2.imread(kkk)
median = cv2.medianBlur(img, 3)
cv2.imwrite("D:\\01_filter.bmp", median)
