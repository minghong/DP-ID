
import sys
from math import *
import time
from collections import Counter
from reedsolo import RSCodec

import subprocess
import math

import random
import numpy as np
from PIL import Image
import re
import os
from scipy import signal
from scipy import ndimage
import cv2


 

def mutate(string,rate):
    ins=0;dele=0;subi=0
    dna = list(string)
    random.seed(None)
    for index, char in enumerate(dna):
        if (random.random() <= rate):
            h=random.random()
            if(h<=1/3):
                subi+=1
                dna[index]=sub(dna[index])
            elif(h<=2/3):
                dele+=1
                dna[index]=""
            else:
                ins+=1
                dna[index]+=insert()
    return "".join(dna),subi,dele,ins



def sub(base):
    random.seed(None)
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

def sequence_error(sequence,rate):
    h=[];s=0;d=0;i=0
    for each in sequence:
        temp,subi,dele,ins=mutate(each, rate)
        s+=subi;d+=dele;i+=ins
        h.append(temp)
    return h


def dna_encode(binary):
    
    
    DNA_encoding = {"00": "A","01": "T","10": "C","11": "G"}
    binary_list = [binary[i: i+2] for i in range(0, len(binary), 2)]
    
    DNA_list = []
    for num in binary_list:
        for key in list(DNA_encoding.keys()):
            if num == key:
                DNA_list.append(DNA_encoding.get(key))

    return "".join(DNA_list)






def bitstream_to_image(bitstream, image_size):
    array_length = image_size[0] * image_size[1]
    
    image_array = np.array([int(bitstream[i:i+8], 2) for i in range(0, array_length*8, 8)], dtype=np.uint8)
    image_array = image_array.reshape(image_size[1], image_size[0])
    image = Image.fromarray(image_array)
    return image


def direct(a):
    mat = np.array(a)
    
    b = mat.transpose()
    
    return b

def correct_length(group_sequence):
    correct_length_sequence=[]
    for l in group_sequence:
        length=len(l)
        if(length>152):
            while(length>152):
                l = l[:76] + l[77:]
                length-=1
        else:
            while(length<152):
                l = l[:76] +"C" +l[76:]
                length+=1
        correct_length_sequence.append(l)
    return correct_length_sequence
from decimal import Decimal

def rs_encode_bitstream(binary_code): #add rs
    binary_code=binary_code.replace('A','00').replace('T','01').replace('C','10').replace('G','11')
   
    
    rsc = RSCodec(4)
    bytes_msg=bytes(int(binary_code[i:i+8],2)for i in range(0,len(binary_code),8))
    array_msg=bytearray(bytes_msg)
    array_msg=rsc.encode(array_msg)

    binary_code=''.join(format(x,'08b') for x in array_msg)
    
    return dna_encode(binary_code)
def image_to_bitstream(image_path):


    img = Image.open(image_path)
    img_arr = np.array(img)
    
    
    return img_arr



from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr                
import numpy as np
import random
from PIL import Image
def dna_encode(binary):
    
    
    DNA_encoding = {"00": "A","01": "T","10": "C","11": "G"}
    binary_list = [binary[i: i+2] for i in range(0, len(binary), 2)]
    
    DNA_list = []
    for num in binary_list:
        for key in list(DNA_encoding.keys()):
            if num == key:
                DNA_list.append(DNA_encoding.get(key))

    return "".join(DNA_list)
def dna_decode(dna):
    DNA_encoding = {"A": "00","T": "01","C": "10","G": "11"}
    bin_list = []
    for num in dna:
        bin_list.append(DNA_encoding.get(num))

    return "".join(bin_list)
def split_string_by_length(string, length):
    result = []
    for i in range(0, len(string), length):
        result.append(string[i:i+length])
    return result

def rs_decode_bitstream(binary_code):
    
    binary_code=binary_code.replace('A','00').replace('T','01').replace('C','10').replace('G','11')
    
    
    rsc = RSCodec(4)
    #convert a string like ACTCA to an array of ints like [10, 2, 4]
    
    bytes_msg=bytes(int(binary_code[i:i+8],2)for i in range(0,len(binary_code),8))
    array_msg=bytearray(bytes_msg)
      
    data=rsc.decode(array_msg)
    binary_code=''.join(format(x,'08b') for x in data[0]) #转二进制
    
    return ''.join(str(int(binary_code[t:t+2],2)) for t in range(0, len(binary_code),2)).replace('0','A').replace('1','T').replace('2','C').replace('3','G')



                
if __name__ == "__main__":

    image_matrix=image_to_bitstream("lena.bmp")
    out=open("matrix.txt","w")

    for i in range(len(image_matrix)):  #image matrix
        if(i%2==0):
            for j in range(len(image_matrix[0])):
                out.write(str(image_matrix[i][j])+"\t")
        else:
            for j in range(len(image_matrix[0])-1,-1,-1):
                out.write(str(image_matrix[i][j])+"\t")
    out.close()

    
    subprocess.run(["g++", "dp-compress.cpp", "-o", "test"], capture_output=True, text=True) #dp-compress
    result=subprocess.run(["./test"],capture_output=True, text=True)
    
    with open("matrix.txt", 'r') as file:   
        for line in file:
            line = line.strip()
            image_matrix = line.split("\t")

    count=0
    bits_pixel="";bits_signal=""
    with open("signal_pixel.txt", 'r') as file:  #covert matrix to bitstream(after dp-compressed) 
        for line in file:
            line = line.strip()
            tmp = line.split(" ")
            number_of_bits=bin(int(tmp[1])-1)[2:].zfill(3)  #number_of_bits-1, such as 255 using 7bits (8-1), because 0 bit is meaningless
            count_temp=bin(int(tmp[0])-1)[2:].zfill(8)      #count-1
            #4-bits(number_of_bits)+8-bits(count)+dynamic-bits(pixel)
            bits_signal=bits_signal+number_of_bits+count_temp
            
            for i in range(int(tmp[0])):
                binary_str = bin(int(image_matrix[count+i]))[2:]
                binary_str = '0' * (int(tmp[1]) - len(binary_str)) + binary_str  
                
                bits_pixel+=binary_str    
            count+=int(tmp[0])
    base=["A","C","G","T"]
    pixel_dna=dna_encode(bits_pixel) #pixel sequence
    while(len(pixel_dna)%152!=0):#complement length to 152
        
        pixel_dna += random.choice(base)
        
    
    #Because of the RS code, we assume that signal is error-free and therefore do not handle signal in the simulation error    
    signal_dna=dna_encode(bits_signal)#signal sequence
    
    while(len(signal_dna)%56!=0):#complement length to 56
        signal_dna+=random.choice(base)
    
    numbers = list(range(0, len(pixel_dna)))
    random.seed(10)
    random.shuffle(numbers)  #interleaving matrix, use random(seed)
    pixel_interleaving_dna=""
    for i in range(len(numbers)):
        pixel_interleaving_dna+=pixel_dna[numbers[i]]#
    file_name="lena.txt"

    signal_sequence = split_string_by_length(signal_dna, 56)

        
    pixel_sequence = split_string_by_length(pixel_interleaving_dna, 152)
    test=0
    
    
    #simulation and decode
    while(test<1):
        print(test)
        test+=1
        for error in [0.005,0.01,0.02,0.03,0.04,0.05]:
            muta_dna=sequence_error(pixel_sequence,error)
                       
            correct_dna=correct_length(muta_dna)   #convert length to 152
                  
            pixel_dna_2=""

            for line in correct_dna:
                
                pixel_dna_2+=line

            
            
            numbers = list(range(0, len(pixel_dna_2)))
            random.seed(10)
            random.shuffle(numbers)
            dna_new=list(range(0, len(pixel_dna_2)))
            for i in range(len(numbers)):#de-interleacing

                dna_new[numbers[i]]=pixel_dna_2[i]
            pixel_dna_3="".join(dna_new)

            bits_pixel_decode=dna_decode(pixel_dna_3)
            
            
            
            d=[];count=0  ;bits_signal_count=0   
            
            while(count<len(bits_pixel)): #decompress
                
                number_of_bits=int(bits_signal[bits_signal_count:bits_signal_count+3],2)+1;count_temp=int(bits_signal[bits_signal_count+3:bits_signal_count+11],2)+1
                #print(number_of_bits,count_temp)
                for i in range(count_temp):
                    d.append((int(bits_pixel_decode[count+i*number_of_bits:count+(i+1)*number_of_bits],2)))
                count+=(number_of_bits*count_temp)
                
                bits_signal_count+=11
                
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
            image.save('dp_inter_'+str(error*100)+'%.bmp')

            img = cv2.imread('dp_inter_'+str(error*100)+'%.bmp',cv2.IMREAD_GRAYSCALE)
            median = cv2.medianBlur(img, 3)
            cv2.imwrite('dp_inter_'+str(error*100)+'%_median.bmp', median)
            
            img1 = cv2.imread("lena.bmp",cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread('dp_inter_'+str(error*100)+'%.bmp',cv2.IMREAD_GRAYSCALE)
            img3= cv2.imread('dp_inter_'+str(error*100)+'%_median.bmp',cv2.IMREAD_GRAYSCALE)
            
            print(str(ssim(img1, img2))+"\t"+str(ssim(img1, img3))+"\t")
            print(str(psnr(img1, img2))+"\t"+str(psnr(img1, img3))+"\n")



