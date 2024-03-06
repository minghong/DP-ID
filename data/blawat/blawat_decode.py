import os
import Chamaeleo
from Chamaeleo.methods.fixed import *
import numpy as np
from PIL import Image


def decode(sequence):
    coding_scheme = Blawat()
    return coding_scheme.decode(sequence)
      
def bitstream_to_image(bitstream, image_size):
    array_length = image_size[0] * image_size[1]
    
    image_array = np.array([int(bitstream[i:i+8], 2) for i in range(0, array_length*8, 8)], dtype=np.uint8)
    image_array = image_array.reshape(image_size[1], image_size[0])
    image = Image.fromarray(image_array)
    return image

def split_string_by_length(string, length):
    result = []
    for i in range(0, len(string), length):
        result.append(string[i:i+length])
    return result

if __name__ == "__main__":
    sequence=""
    #file=open("encode_church.dna")
    file=open('decode_blawat.dna')
    for line in file.readlines():
        if(line[0]!=">"):
            sequence+=(line.split("\n")[0])
    
    split_sequence=split_string_by_length(sequence,5)
    bitstream=decode(split_sequence)
    bit=""
    for i in bitstream:
        bit+=(''.join(i))
    image_size = (256, 256)  # 图像尺寸
    image = bitstream_to_image(bit, image_size)
    image.save("decode_image.bmp")

