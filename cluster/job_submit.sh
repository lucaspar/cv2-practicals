#!/usr/bin/env bash
#  -M <YOUR_NET_ID>@nd.edu 	# Email to be notified (also put $ in front of this line)
#$ -m abe                   # Send mail when job begins, ends and aborts
#$ -q gpu@@czajka	        # Specify job queue
#$ -l gpu_card=1            # Specify number of GPU cards to use - 1 to 4, be polite :)
#$ -N my_job                # Specify a job name

echo " >> Running on $(uname -n)"

# enable cluster anaconda
module load conda

# prepare shell for conda
conda init `ps -o comm= -p $$`
source ~/.bashrc

# activate conda environment
conda activate cv

# run your custom script
python test.py
