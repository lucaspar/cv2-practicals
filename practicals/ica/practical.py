import bsif
import numpy as np
import os
import cv2
import scipy.signal as sg
from skimage.color import rgb2gray

# *** Task 1 ***
# Use 'generate_patches.py' to generate face-specific image patches (image_domain = 'faces').
# Image patches for human iris domain are already generated.


# *** Task 2 ***
# Use 'generate_bsif_filters.py' to generate face-specific BSIF kernels (image_domain = 'faces').
# Switch to iris domain (image_domain = 'human_iris'). Generate iris-specific BSIF kernels. Choose one scale, e.g., 27.


# *** Task 3 ***
# Choose one 'filter_count', for instance 8 (i.e., 8 filters for a given scale). Compare visualy 
# iris-specific and face-specific filters. Do you see anyt diferrences? How would you describe these 
# differences (in two/three senteces)? For instance, would these filters be sensitive to different 
# image features? 


# *** Task 4 ***
# For the remaining subjects in our face dataset (i.e., not used in training):
#
#       classes = [f.path for f in os.scandir(classes_folder) if f.is_dir()]
#       train_users = 15
#       for user_dir in classes[train_users:]:
#           ...
#
# generate within-class (between the same faces) and between-class comparisons. Use 'generateHistogram'
# and 'matchCodes' from bsif.py, i.e.:
#
#       import bsif
#       ...
#       hist1, code1 = bsif.generateHistogram(...)
#       hist2, code2 = bsif.generateHistogram(...)
#       bsif.matchCodes(code1,code2)
#
# Use im1 = rgb2gray(cv2.imread(...)) to read images and convert them to grayscale. To speed up things, consider doing 
# just one within-class comparison and one between-class comparison for randomly two different subjects.
#
# Consider using only well lit face images:
#
#       for image_file in os.listdir(subject_dir):
#           if image_file.endswith("000E-00.pgm") or image_file.endswith("000E+00.pgm"):
#               ...
# 
# Question: which face recognition system is better? The one that uses face-specific BSIF filters, or the one that uses 
# iris-specific filters? Why?


# Image domain:
#image_domain = 'faces'
image_domain = 'human_iris'

# BSIF filters to be used (you can try different combinations, as well):
patch_scale = '13'
filter_count = '12'
filters = np.load('generated_filters' + os.path.sep + image_domain + os.path.sep + patch_scale + os.path.sep + filter_count + os.path.sep + 'filters.npy')

impostor_scores = []
genuine_scores = []

# Here write your code to calculate genuine and impostor scores, given the image domain
# impostor_scores.append(...)
# genuine_scores.append(...)

# For comparison of genuine and impostor distributions, you can calculate d'. The higher d', the better the system.
d_prime = np.absolute(np.mean(impostor_scores)-np.mean(genuine_scores)) / np.sqrt( (0.5 * (np.var(impostor_scores) + np.var(genuine_scores))) )
