## Requirements:
File structure like this:

Replicate_Experiment_name
—- cc
—----- cell#
—-—-—- ….aligned_c1.csv
—-—-—- ….aligned_c2.csv
—----- cell#
—-—-—- ….aligned_c1.csv
—-—-—- ….aligned_c2.csv
—----- cell#
—-—-—- ….aligned_c1.csv
—-—-—- ….aligned_c2.csv

## This script will change the directory into something like this:

Replicate_Experiment_name_Cav_aligned
---- cell#
-—- ….aligned_c1.csv
---- cell#
-—- ….aligned_c1.csv
---- cell#
-—- ….aligned_c1.csv

Replicate_Experiment_name_PTRF_aligned
---- cell#
-—- ….aligned_c2.csv
---- cell#
-—- ….aligned_c2.csv
---- cell#
-—- ….aligned_c2.csv

Instructions for use:

Run 
```{bash}
cd /scratch/$USER
```

```{bash}
export DATASET="/scratch/$USER/FIXME"
```
(If this has already been run, (for example you just ran https://github.com/NanoscopyAI/tutorial_smlm_alignment_colocalization), and you did not change the DATASET environment variable to something else (run export DATASET to a new directory, you do not have to change it)

Then, run

```{bash}
wget https://raw.githubusercontent.com/josephsoo/aligned_renaming_script/master/folder.py -O folder.py

python folder.py
```
