## Requirements:
File structure like this:

Replicate_Experiment_name\
—- cc\
—----- cell#\
—-—-—- ….aligned_c1.csv\
—-—-—- ….aligned_c2.csv\
—----- cell#\
—-—-—- ….aligned_c1.csv\
—-—-—- ….aligned_c2.csv\
—----- cell#\
—-—-—- ….aligned_c1.csv\
—-—-—- ….aligned_c2.csv

## This script will change the directory into this:

Replicate_Experiment_name_Cav_aligned\
---- cell#\
-—---- ….aligned_c1.csv\
---- cell#\
-—---- ….aligned_c1.csv\
---- cell#\
-—--- ….aligned_c1.csv

Replicate_Experiment_name_PTRF_aligned\
---- cell#\
-—----- ….aligned_c2.csv\
---- cell#\
-—----- ….aligned_c2.csv\
---- cell#\
-—----- ….aligned_c2.csv

## What to do
Run 
```{bash}
cd /scratch/$USER
```

\
(OPTIONAL) You can skip this step if you just ran https://github.com/NanoscopyAI/tutorial_smlm_alignment_colocalization and did not rename the DATASET variable 
```{bash}
export DATASET="/scratch/$USER/FIXME"
```

Then, run

```{bash}
wget https://raw.githubusercontent.com/josephsoo/aligned_renaming_script/master/folder.py -O folder.py

python folder.py
```
