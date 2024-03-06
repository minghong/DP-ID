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
 
def fspecial_gauss(size, sigma):
    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = numpy.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()
 
 
def ssim(img1, img2, cs_map=False):
    img1 = img1.astype(numpy.float64)
    img2 = img2.astype(numpy.float64)
    size = 11
    sigma = 1.5
    window = fspecial_gauss(size, sigma)
    K1 = 0.01
    K2 = 0.03
    L = 255 #bitdepth of image
    C1 = (K1*L)**2
    C2 = (K2*L)**2
    mu1 = signal.fftconvolve(window, img1, mode='valid')
    mu2 = signal.fftconvolve(window, img2, mode='valid')
    mu1_sq = mu1*mu1
    mu2_sq = mu2*mu2
    mu1_mu2 = mu1*mu2
    sigma1_sq = signal.fftconvolve(window, img1*img1, mode='valid') - mu1_sq
    sigma2_sq = signal.fftconvolve(window, img2*img2, mode='valid') - mu2_sq
    sigma12 = signal.fftconvolve(window, img1*img2, mode='valid') - mu1_mu2
    if cs_map:
        return (((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*
                    (sigma1_sq + sigma2_sq + C2)), 
                (2.0*sigma12 + C2)/(sigma1_sq + sigma2_sq + C2))
    else:
        return ((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*
                    (sigma1_sq + sigma2_sq + C2))
 
def mssim(img1, img2):
    """
    refer to https://github.com/mubeta06/python/tree/master/signal_processing/sp
    """
    level = 5
    weight = numpy.array([0.0448, 0.2856, 0.3001, 0.2363, 0.1333])
    downsample_filter = numpy.ones((2, 2))/4.0
    im1 = img1.astype(numpy.float64)
    im2 = img2.astype(numpy.float64)
    mssim = numpy.array([])
    mcs = numpy.array([])
    for l in range(level):
        ssim_map, cs_map = ssim(im1, im2, cs_map=True)
        mssim = numpy.append(mssim, ssim_map.mean())
        mcs = numpy.append(mcs, cs_map.mean())
        filtered_im1 = ndimage.filters.convolve(im1, downsample_filter, 
                                                mode='reflect')
        filtered_im2 = ndimage.filters.convolve(im2, downsample_filter, 
                                                mode='reflect')
        im1 = filtered_im1[::2, ::2]
        im2 = filtered_im2[::2, ::2]
    return (numpy.prod(mcs[0:level-1]**weight[0:level-1])*
                    (mssim[level-1]**weight[level-1]))
                    
                    
kkk="D:\\lena.bmp"                   
xxx="D:\\01_filter.bmp"

img = cv2.imread(kkk,0)

noise_img = cv2.imread(xxx,0)
 
ssim_val = ssim(img, noise_img)
mssim_val = mssim(img, noise_img)
 

print(f"mssim_val: {mssim_val}")








