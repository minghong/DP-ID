import numpy as np
import random


def dna_decode(dna):
    DNA_encoding = {"A": "00","T": "01","C": "10","G": "11"}
    bin_list = []
    for num in dna:
        bin_list.append(DNA_encoding.get(num))

    return "".join(bin_list)


file=open("D:\\process.txt")
stl=""
for l in file.readlines():
    if(l[0]!=">"):
        stl+=(l.rstrip("\n"))
        

out=open("D:\\jie_direct.txt","w")
numbers = list(range(0, len(stl)))
random.seed(10)
random.shuffle(numbers)
dna_new=list(range(0, len(stl)))
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





from skimage.metrics import peak_signal_noise_ratio as psnr
from PIL import Image
import numpy as np
 
 


 
import sys
import numpy
from scipy import signal
from scipy import ndimage
import cv2

                    
                    
kkk="D:\\lena.bmp"                   
xxx="D:\\01_filter.bmp"

img = cv2.imread(kkk,0)

noise_img = cv2.imread(xxx,0)
 
psnr_val = psnr(img, noise_img)

 

print(f"psnr: {psnr_val}")








