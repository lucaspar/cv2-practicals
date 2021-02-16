# Computer Vision 2 | Practical assignments

+ CSE 40536/60536, University of Notre Dame
+ [Computer Vision Research Lab (CVRL @ Notre Dame)](https://cvrl.nd.edu/)

_ | _
 -------------------- | --------------------
Instructor            | Adam Czajka
Teaching Assistant    | Lucas Parzianello

---

## Directory structure:

Location                        | Description
 ------------------------------ | ----------
`practicals/<PRACTICAL_ID>`     | Activities
`cluster`                       | Example scripts and readme to run jobs in the CRC cluster.


## Environment management

It's better to create a different virtual environment for each practical to avoid version conflicts. The file structure helps you remember the environment name:

```bash
# set the practical ID, which is the directory name (e.g. yol)
PRACTICAL_ID=yol
VENV=cv2-$PRACTICAL_ID

# set the virtual environment name
cd practicals/$PRACTICAL_ID

# create environment (python version might be differ, use 3.8 as default)
conda create $VENV python=3.8
conda activate $VENV

# the envs prefixed with "cv2-" are the ones for this course
conda env list
```

Alternatively, you can set up an alias to automatically activate the environment of your working directory.

```bash
# add it to your `~/.bashrc`:
alias cacv='conda activate cv-`basename \$PWD`'
```

Then, assuming the environment exists, navigate to the practical directory and run `cacv`.
