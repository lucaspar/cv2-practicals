#!/bin/bash

if [[ "$(hostname)" == *".crc.nd.edu" ]]; then
    echo "IN CRC!"
fi

exit 2

PRACTICAL_NAME=yolo
ENV_NAME=cv2-$PRACTICAL_NAME

# create environment
echo "Creating env $ENV_NAME"
conda create -n $ENV_NAME python=3.8
conda activate $ENV_NAME
conda install -y -c conda-forge opencv
