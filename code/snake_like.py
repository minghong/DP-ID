import numpy as np
from PIL import Image
import re
import numpy as np

import random



def image_to_bitstream(image_path):


    img = Image.open(image_path)
    img_arr = np.array(img)
    
    
    return img_arr

bitstream=image_to_bitstream("D:\\lena.bmp")
out=open("D:\\1.txt","w")

for i in range(len(bitstream)):
    if(i%2==0):
        for j in range(len(bitstream[0])):
            out.write(str(bitstream[i][j])+" ")
    else:
        for j in range(len(bitstream[0])-1,-1,-1):
            out.write(str(bitstream[i][j])+" ")
out.close()
