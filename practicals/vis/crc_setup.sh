#/usr/bin/env bash
set -e
module load conda

conda create -n cv2-vis python=3.6
conda activate cv2-vis

pip install --upgrade pip setuptools wheel
pip install tensorflow==1.15.*
pip install keras
pip install -U git+https://github.com/raghakot/keras-vis.git

echo "Good, now try running mnist_vis.py"
