import os
import Chamaeleo
from Chamaeleo.methods.fixed import *
import numpy as np
from PIL import Image

def split_string_by_length(string, length):
    result = []
    for i in range(0, len(string), length):
        result.append(string[i:i+length])
    return result


def encode(bit_segments):
    coding_scheme = Blawat()
    return coding_scheme.encode(bit_segments)
      

def image_to_bitstream(image_path):

    img = Image.open(image_path)
    img_arr = np.array(img)    
    bitstream = ''.join([f"{bin(pixel)[2:].zfill(8)}" for pixel in img_arr.flatten()])
    
    return bitstream

if __name__ == "__main__":
    
    bitstream=image_to_bitstream("fly_grey.jpg")
    split_bitstream=split_string_by_length(bitstream,8)
    DNA=encode(split_bitstream)
    
    sequence=""
    for i in DNA :
        sequence+=(''.join(i))
    
    split_sequence=split_string_by_length(sequence,150)
    out=open("encode_blawat.dna","w")
    for i in split_sequence:
        out.write(i+"\n")
    out.close()


