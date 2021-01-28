import sys
sys.path.insert(1, '../')
import loader
import pywt
import truncate as trun
import colormap as cmap
import numpy as np
path = "../images/frymire.png"
wave = sys.argv[2] # eg : haar, mexh
threshold = int(sys.argv[1])  # a number 
#e.g. python wavelets.py 50 haar



def wavelet(img2d):
    # loader.show_image(img2d)
    (wA, (wH, wV, wD)) = pywt.dwt2(img2d, wave) # dwt
    cmap.graph(wA)  # to  visualize any 2d array
    wA = trun.truncate(wA, threshold)  # approximate part
    wH = trun.truncate(wH, threshold)  # horizontally detailed part
    wV = trun.truncate(wV, threshold)  # vertically detailed part
    wD = trun.truncate(wD, threshold)  # diagonally detailed part
    imgr2d = pywt.idwt2((wA, (wH, wV, wD)), wave) # idwt to reconstruct the numpy array
    h,w = imgr2d.shape
    return imgr2d[:h-1,:] 

def main():
    img = loader.load_image(path)
    # loader.show_image(img)
    for i in range(3):   # i=0->R ; i=1->G ; i=2->B
        img[:,:,i] = wavelet(img[:,:,i])
    # loader.show_image(img)


if __name__ == "__main__":
    main()