#!/usr/bin/env bash

# enable cluster anaconda
module load conda

# prepare shell for anaconda
conda init $(ps -o comm= -p $$)
source ~/.bashrc

# create conda environment
conda create -n cv python=3.6
conda activate cv

# install packages required (this will take a while)
conda install -y jupyter matplotlib
conda install -y -c conda-forge opencv
conda install -y tensorflow-gpu scikit-learn
conda install -y pytorch torchvision cudatoolkit=10.1 -c pytorch
