## DP-ID: Interleaving and Denoising to Improve the Quality of DNA Storage Image
# Windows
If you in Windows system, you can run DP-ID step by step.

The codes are located in the **code** folder.The input image should be a 256\*256 grayscale image. If it is other size or color image, please modify the corresponding parameters

Step 1 : run **sanke_like.py** to obtain the image matrix
 
step 2 : run **dp-image_compression.cpp** to achieve dp-compress

step 3 : run **encode.py** to convert the image matrix to bases

step 4 : simulate DNA storage errors. If you have simulator, please use it; otherwise, you can run **simulation.py** to simulate DNA storage errors

step 5 : run **correct_length.py** to correct DNA sequence to correct length

step 6 : run **decode.py** to convert bases to the image
# Linux
If you in Linux system, you can run DP-ID in one step.

The codes are located in the **linux** folder. The input image should be a 256\*256 grayscale image. If it is other size or color image, please modify the corresponding parameters

Step : run **dp_compress_inter.py** to obtain the results

Due to copyright, we have removed lena.bmp, you can find lena 256\*256 grayscale image by your way or other 256\*256 grayscale images. You can also modify parameters to apply to grayscale and color images of other sizes. If you have any question, please contact us by e-mail or issues.

## Citation
Xu, Q., Ma, Y., Lu, Z. Bi, K. DP-ID: Interleaving and Denoising to Improve the Quality of DNA Storage Image. Interdiscip Sci Comput Life Sci (2024). https://doi.org/10.1007/s12539-024-00671-6

## Contact
If you have any questions, please contact xuqi@seu.edu.cn.

## License
This project is licensed under the MIT License.
