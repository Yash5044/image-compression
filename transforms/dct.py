import sys
sys.path.insert(1, '../')
import loader
import pywt
import truncate as trun
import colormap as cmap
import numpy as np
from scipy.fftpack import dct, idct
import matplotlib.pylab as plt
import tkinter
import math
from zigzag import *
path = "../images/cat.png"
#wave = sys.argv[2] # eg : haar, mexh
#threshold = int(sys.argv[1])  # a number 
#e.g. python wavelets.py 50 haar

# Quantization Matrix 
QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56 ],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')   

# img = loader.load_image(path)
# # loader.show_image(img)
# for i in range(3):   # i=0->R ; i=1->G ; i=2->B
#     img[:,:,i] = wavelet(img[:,:,i])
# # loader.show_image(img)



# def DCT(img2d):
#     img = dct2(img2d) # dct
#     h1=len(img)
#     w1=len(img[0])
#     new_img = C

#     for i in range(h1): 
#         for j in range(w1): 
#             new_img[i][j]= round(img[i][j]/QUANTIZATION_MAT[i%8][j%8])
#     print(new_img)
#     truncated_img = trun.truncate(new_img, 0)  # approximate part

#     for i in range(h1): 
#         for j in range(w1): 
#             truncated_img[i][j]= truncated_img[i][j]*QUANTIZATION_MAT[i%8][j%8]
#     print(truncated_img)
#     imgr2d = idct2(truncated_img) # idct to reconstruct the numpy array
#     h,w = imgr2d.shape
#     return imgr2d[:h,:] 

def DCT(img2d):
    block_size = 8
    h1=len(img2d)
    w1=len(img2d[0])
    height = h1
    width = w1

    nbh = math.ceil(h1/block_size)

    nbw = math.ceil(w1/block_size)
    # height of padded image
    H =  block_size * nbh

    # width of padded image
    W =  block_size * nbw

    # create a numpy zero matrix with size of H,W
    padded_img = np.zeros((H,W))
    padded_img[0:height,0:width] = img2d[0:height,0:width]



    for i in range(nbh):
        
        # Compute start and end row index of the block
        row_ind_1 = i*block_size                
        row_ind_2 = row_ind_1+block_size
        
        for j in range(nbw):
            
            # Compute start & end column index of the block
            col_ind_1 = j*block_size                       
            col_ind_2 = col_ind_1+block_size
                        
            block = padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ]
                    
            # apply 2D discrete cosine transform to the selected block                       
            DCT_matrix = dct2(block)            
            DCT_normalized = np.round(np.divide(DCT_matrix,QUANTIZATION_MAT))

            truncated_img8 = trun.truncate(DCT_normalized, 0)  # approximate part
            DCT_normalized8 = np.multiply(truncated_img8,QUANTIZATION_MAT)
            IDCT_normalized = idct2(DCT_normalized8)

            # reorder DCT coefficients in zig zag order by calling zigzag function
            # it will give you a one dimentional array
            reordered = zigzag(IDCT_normalized)

            # reshape the reorderd array back to (block size by block size) (here: 8-by-8)
            reshaped= np.reshape(reordered, (block_size, block_size)) 
            
            # copy reshaped matrix into padded_img on current block corresponding indices
            padded_img[row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2] = reshaped                        

    idct_truncated = np.zeros((h1,w1))
    for i in range(h1): 
        for j in range(w1): 
            idct_truncated[i][j]= padded_img[i][j]
    

    print(idct_truncated)

    imgr2d = idct2(idct_truncated) # idct to reconstruct the numpy array
    h,w = imgr2d.shape
    return imgr2d[:h,:] 




# imF = dct2(img)
# im1 = idct2(imF)
# print(imF.shape)
# plt.plot(im1)
# plt.savefig("f.png")
# plt.subplot(121), plt.imshow(img), plt.axis('off'), plt.title('original image', size=20)
# plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=20)
# plt.show()
# def wavelet(img2d):
#     # loader.show_image(img2d)
#     (wA, (wH, wV, wD)) = pywt.dwt2(img2d, wave) # dwt
#     cmap.graph(wA)  # to  visualize any 2d array
#     wA = trun.truncate(wA, threshold)  # approximate part
#     wH = trun.truncate(wH, threshold)  # horizontally detailed part
#     wV = trun.truncate(wV, threshold)  # vertically detailed part
#     wD = trun.truncate(wD, threshold)  # diagonally detailed part
#     imgr2d = pywt.idwt2((wA, (wH, wV, wD)), wave) # idwt to reconstruct the numpy array
#     h,w = imgr2d.shape
#     return imgr2d[:h-1,:] 

def main():
    img = loader.load_image(path)
    # loader.show_image(img)
    for i in range(3):   # i=0->R ; i=1->G ; i=2->B
        img[:,:,i] = DCT(img[:,:,i])
    loader.show_image(img)


if __name__ == "__main__":
    main()