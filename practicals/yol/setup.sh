#!/bin/bash -li
set -e

# params
PRACTICAL_NAME=$(basename "$PWD")
ENV_NAME="cv2-$PRACTICAL_NAME"

# crc execution
if [[ "$(hostname)" == *".crc.nd.edu" ]]; then
    echo " >>> Running on CRC, loading modules"
    module load conda
    conda init bash
    source "$HOME/.bashrc"
fi

# create environment
if ! $(conda env list | grep -qE "$ENV_NAME[[:space:]]"); then
    echo " >>> Creating env: $ENV_NAME"
    conda create -y -n "$ENV_NAME" python=3.8
else
    echo " >>> Env $ENV_NAME exists, activating..."
fi
conda activate "$ENV_NAME"

# install dependencies
echo " >>> Installing deps..."
# conda install -y -c conda-forge opencv

# run the checking script
echo " >>> Running system check..."
if python check.py; then
    echo " >>> It works!"
fi
