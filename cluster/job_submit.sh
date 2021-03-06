#!/bin/bash
#  -M <YOUR_NET_ID>@nd.edu 	# Email to be notified (put #$ in front of this line and the one below to enable it)
# -m abe                    # Send mail when job begins, ends and aborts
#$ -q gpu	                # Specify job queue
#$ -l gpu=1                 # Specify number of GPU cards to use - 1 to 4, be polite :)
#$ -N my_job                # Specify a job name

echo " >> Running on $(uname -n)"

# activate conda environment
conda activate cv

# run your custom script
python test.py
