import numpy as np
import scipy.signal as sg
from skimage.color import rgb2gray
from scipy.spatial import distance
import cv2

def generateHistogram(image,filters,patch_scale):

    filter_count = filters.shape[2]

    codeBinary = np.zeros((image.shape[0] - patch_scale + 1, image.shape[1] - patch_scale + 1, filter_count))
    for i in range(1,filter_count+1):
        ci = sg.convolve2d(image, np.rot90(filters[:,:,filter_count-i],2), mode='valid')
        codeBinary[:,:,i-1] = ci>0

    codeImg = np.ones((codeBinary.shape[0], codeBinary.shape[1]), np.int64)
    for row in range(codeImg.shape[0]):
        for col in range(codeImg.shape[1]):
            for b in range(filter_count):
                if codeBinary[row,col,b]:
                    codeImg[row,col] += 2**b

    hist = np.asarray(np.histogram(codeImg.flatten(), bins=2**filter_count))
    hist_norm = hist[0] / np.linalg.norm(hist[0])

    return hist_norm, codeBinary

def matchHistograms(h1,h2):
    return 0.5 * np.sum((h1 - h2)**2/( h1 + h2 + 1e-6 ))

def matchCodes(code1,code2):
    scoreC = np.zeros(code1.shape[2])
    for b in range(code1.shape[2]):
        xorCodes = np.logical_xor(code1[:,:,b], code2[:,:,b])
        scoreC[b] = np.sum(xorCodes) / (code1.shape[0]*code1.shape[1])
        
    return np.mean(scoreC)