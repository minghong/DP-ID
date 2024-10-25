## DP-ID 
# Windows
If you in Windows system, you can run DP-ID step by step.

The codes are located in the **code** folder, lena.bmp (256*256) is an example

Step 1 : run **sanke_like.py** to obtain the image matrix
 
step 2 : run **dp-image_compression.cpp** to achieve dp-compress

step 3 ：run **encode.py** to convert the image matrix to bases

step 4 ：simulate DNA storage errors. If you have simulator, please use it; otherwise, you can run **simulation.py** to simulate DNA storage errors

step 5 : run **correct_length.py** to correct DNA sequence to correct length

step 6 ：run **decode.py** to convert bases to the image
# Linux
If you in Linux system, you can run DP-ID in one step.

The codes are located in the **linux** folder, lena.bmp (256*256) is an example

Step : run **dp_compress_inter.py** to obtain the results

## Citation
A related paper has been accepted for publication in XXX.

## Contact
If you have any questions, please contact corresponding author (bik@seu.edu.cn) and first author (xuqi@seu.edu.cn).
