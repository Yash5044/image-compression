import sys
sys.path.insert(1, '../')
import loader
import pywt
import truncate as trun
import colormap as cmap
import numpy as np
path = "../images/baboon.png"
wave = sys.argv[2] # eg : haar, mexh
threshold = float(sys.argv[1])  # a number 
#e.g. python wavelets.py 50 haar



def wavelet(img2d):
    # loader.show_image(img2d)
    (wA, (wH, wV, wD)) = pywt.dwt2(img2d, wave) # dwt
    cmap.graph(wV)  # to  visualize any 2d array
    mval = max(np.max(wA),-np.min(wA))
    wA = trun.truncate(wA, threshold, mval)  # approximate part
    wH = trun.truncate(wH, threshold, mval)  # horizontally detailed part
    wV = trun.truncate(wV, threshold, mval)  # vertically detailed part
    wD = trun.truncate(wD, threshold, mval)  # diagonally detailed part
    # cmap.graph(wV)
    imgr2d = pywt.idwt2((wA, (wH, wV, wD)), wave) # idwt to reconstruct the numpy array
    h,w = imgr2d.shape
    return imgr2d[:h-1,:] 

def main():
    img = loader.load_image(path)[:,:,0]
    loader.show_image(img)
    # for i in range(3):   # i=0->R ; i=1->G ; i=2->B
    img = wavelet(img)
    loader.show_image(img)


if __name__ == "__main__":
    main()