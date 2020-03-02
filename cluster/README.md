# CV Cluster Wiki

## Common Tasks

### Connect to front-end node

```sh
# from your local machine, connect to a CRC fron-end node
NETID=<your Notre Dame NetID>
ssh -CY $NETID@crcfe02.crc.nd.edu
```

### Installing Dependencies

Your file system is mounted on the machine to where you will submit the jobs, so you can prepare your environment on the front-end node (e.g. `crcfe02.crc.nd.edu`) and later submit the job to our cluster `qa-rtx6k-017.crc.nd.edu` (a.k.a. `gpu@@czajka`).

Take a look at `prep_env.sh`. You can run this script to create and prepare a conda environment that you will later use to run your program. You only need to run it once (unless you add more dependencies to your project).

```sh
# from a front-end node, run the preparation script
./prep_env.sh
```

### Interactive Shell

From a front-end node you can spawn an interactive shell inside our cluster, so you can quickly experiment code with the GPUs.

> Do not train through an interactive shell, use it only for prototyping!

> Train by submitting a job to the queue (see below).

```sh
# login to the GPU cluster
qrsh -q gpu@@czajka -l gpu_card=1

# your file system is now mounted in the new machine; you can
# navigate through the files, find and run your program:

conda activate cv
python test.py
```

### Submitting Jobs

You can use `job_submit.sh` as a base script to create your own. Let's use it as an example.

```sh
qsub job_submit.sh
```

### Checking Job Status

```sh
qstat -u <your_nd_net_id>
```

### Execution Results

When you submit your job, you will see a file named like `my_job.o772071` with the outputs of your execution. If this file is empty, wait until your execution is finished.

The outputs of `qsub job_submit.sh` should look like this:

```sh
(cv) crcfe01:/…vate/demos/cv2 » more my_job.o772071

 >> Running on qa-rtx6k-017.crc.nd.edu
/opt/sge/crc/spool/qa-rtx6k-017/job_scripts/772071: line 16: module: command not found
/opt/sge/crc/spool/qa-rtx6k-017/job_scripts/772071: line 19: conda: command not found
 >> Python version:	     3.6.10 |Anaconda, Inc.| (default, Jan  7 2020, 21:14:29)
[GCC 7.3.0]
 >> Tensorflow version:	 2.1.0
 >> PyTorch version:	 1.4.0
 >> OpenCV version:	     3.4.2

 >> CUDA available?	True
	GPU 0: Quadro RTX 6000
Sleeping 20s...
Finished execution!
```

## Other Tasks

### Check disk storage

```sh
quota
# Quota for /afs/crc.nd.edu/user/n/netid
# Volume Name                   Quota      Used %Used   Partition
# u.netid                     1500 GB     15 GB    1%         30%
```

### Mounting CRC drive locally

To transfer files back and forth between your local machine and CRC, you might want to mount the remote drive:

```sh
# create variables
NETID=<your_notre_dame_net_id>
MOUNTPOINT=/mnt/crc
initial="$(echo $NETID | head -c 1)"

# create dir
mkdir -p $MOUNTPOINT

# mount file system
sshfs -C $NETID@crcfe02.crc.nd.edu:/ $MOUNTPOINT

# navigate to user home
cd $MOUNTPOINT/afs/crc.nd.edu/user/$initial/$NETID/
```

### Version Control

Upon mounting, you can easily do things like Git version control:

```sh
# from your local machine, mount the CRC drive and run:
cd $MOUNTPOINT/afs/crc.nd.edu/user/$initial/$NETID/Private/
git clone git@github.com:username/project.git my_project

# then you can open the repository with your
# text editor / IDE of choice (e.g. VS Code):
code my_project

```

Now code changes are visible to CRC machines in real time.
