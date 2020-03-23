#!/usr/bin/env python
import numpy as np
import cv2
import os
from sklearn.decomposition import FastICA  # to instal: pip3 install sklearn

# Image domain
image_domain = 'faces'
# image_domain = 'human_iris'

# Number of filters in each generated filter set.
filter_count = [12]

# Desired scales of the filters to be generated; it must relate to the available source image patches.
patch_scales = [13]

# Folder containing the source image patches. For each image domain, it must have one subfolder for each desired filter scale.
patch_folder = 'patches'

# Output folder, where generated filters will be saved.
output_folder = 'generated_filters'

# for each desired filter scale...
for scale in patch_scales:
    # creates the output scale folder, if necessary
    scale_folder = output_folder + os.path.sep + image_domain + os.path.sep + '{:02d}'.format(scale)
    if not os.path.exists(scale_folder):
        os.makedirs(scale_folder)

    # reads the image patches related to the current scale, in the proper format for fast ICA
    patches = []
    patch_file_list = []
    patch_folder_scale = patch_folder + os.path.sep + image_domain + os.path.sep + '{:02d}'.format(scale) + os.path.sep
    for file in os.listdir(patch_folder_scale):
        if file.endswith(".png"):
            patch_file_list.append(patch_folder_scale + file)

    for patchFilepath in patch_file_list:
        patch = cv2.imread(patchFilepath.strip(), cv2.IMREAD_GRAYSCALE)
        if len(patches) == 0:
            patches = patch.reshape((patch.shape[0] * patch.shape[1], 1))
        else:
            patches = np.c_[patches, patch.reshape((patch.shape[0] * patch.shape[1], 1))]

    # for each desired number of filters
    for count in filter_count:
        # creates the output filter #number subfolder, if necessary
        filter_folder = scale_folder + os.path.sep + '{:02d}'.format(count)
        if not os.path.exists(filter_folder):
            os.makedirs(filter_folder)

        # applies fast ICA
        ica = FastICA(n_components=count, max_iter=10000)
        filter_arrays = ica.fit_transform(patches)
        filters = filter_arrays.reshape(scale, scale, count)

        # saves the obtained filters as:
        # 1. numpy file
        np.save(filter_folder + os.path.sep + 'filters.npy', filters)

        # 2. images (useful for visualization)
        filters = filter_arrays.reshape(scale, scale, count)
        for i in range(count):
            filter = filters[:, :, i]
            cv2.normalize(filter, filter, 0, 255, cv2.NORM_MINMAX).astype(np.int)

            filter_path = filter_folder + os.path.sep + 'filter_' + '{:02d}'.format(i) + '.png'
            cv2.imwrite(filter_path, filter)

        print("Generated for scale: {}, filter count: {}".format(scale,count))

print('*** DONE! ***')
