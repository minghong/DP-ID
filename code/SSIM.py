denoise_img = "D:\\01_filter.bmp"
kkk="D:\\baboon_grey.jpg"   
noise_img="D:\\01.bmp"


import numpy as np
import random
from skimage.metrics import peak_signal_noise_ratio as psnr
from PIL import Image
import numpy as np 
import sys
import numpy
from scipy import signal
from scipy import ndimage
import cv2
 



from skimage.metrics import structural_similarity as ssim
import numpy as np
from PIL import Image
import cv2

img1 = cv2.imread(kkk,cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(denoise_img,cv2.IMREAD_GRAYSCALE)
img3= cv2.imread(noise_img,cv2.IMREAD_GRAYSCALE)
print(ssim(img1, img3, multichannel=True))
print(ssim(img1, img2, multichannel=True))
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


img = cv2.imread(kkk,0)
noise_img_1 = cv2.imread(noise_img,0)
denoise_img_1 = cv2.imread(denoise_img,0)

mssim_val_1 = mssim(img, noise_img_1)
mssim_val_2 = mssim(img, denoise_img_1)


print(f"mssim_val: {mssim_val_1}")
print(f"mssim_val: {mssim_val_2}")




