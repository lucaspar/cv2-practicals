#!/usr/bin/env python
from sklearn.feature_extraction import image
import numpy as np
import cv2
import os

# Folder for the generated patches.
patch_folder = 'patches'

# Image domain (and folder where source images are located).
db_folder = 'source_images'
image_domain = 'faces'
classes_folder = db_folder + os.path.sep + image_domain

# Desired scales of the filters to be generated; it must relate to the available source image patches.
patch_scales = [13]

# Seed to make patch creation deterministic
random_state = 3011

# Number of patches per image
max_patches_per_image = 30

# Check how many classes (in case of faces: subjects) we have
classes = [f.path for f in os.scandir(classes_folder) if f.is_dir()]

# How many subjects we want to use to generate patches?
train_users = 15

# Reads the image database and generates patches
for user_dir in classes[0:train_users]:
    if not user_dir.startswith('.'):
        for image_file in os.listdir(user_dir):

            # take only good-quality face images to generate patches
            if image_file.endswith("000E-00.pgm") or image_file.endswith("000E+00.pgm"):

                # for each desired filter scale...
                for scale in patch_scales:

                    im_path = user_dir + os.path.sep + image_file
                    one_image = cv2.imread(im_path)
                    patches = image.extract_patches_2d(
                        image = one_image,
                        patch_size = (scale, scale),
                        max_patches = max_patches_per_image,
                        random_state = random_state
                    )

                    # creates the output scale folder, if necessary
                    scale_path = patch_folder + os.path.sep + image_domain + os.path.sep + '{:02d}'.format(scale)
                    if not os.path.exists(scale_path):
                        os.makedirs(scale_path)

                    for idx, patch in enumerate(patches):
                        patch_patch = scale_path + os.path.sep + image_file[:-4] + '_{:06d}'.format(idx) + '.png'
                        cv2.imwrite(patch_patch, patch)

        print("Generated for images in: {}".format(user_dir))

print('*** DONE! ***')
