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
def DCT(img2d):
    img = dct2(img2d) # dct
    maxval = max(img.min(), img.max(), key=abs)
    normimg = np.divide(img, maxval)
    print(maxval)
    cmap.graph(img)  # to  visualize any 2d array
    normimg = trun.truncate(normimg, 0.0005)  # approximate part
    finalimg = normimg*maxval
    print(np.matrix(finalimg))
    imgr2d = idct2(finalimg) # idct to reconstruct the numpy array
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