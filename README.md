# aligned_renaming_script
This script renames and organizes files so that they can be processed by SuperResNet Batch
## Requirements:
This script requires a folder processed by the [alignment pipeline for drift correction](https://github.com/NanoscopyAI/tutorial_smlm_alignment_colocalization)

**An example file structure may look like this:**
Replicate_name\
—- cc\
—----- cell#\
—-—-—- …aligned_c1.csv\
—-—-—- …aligned_c2.csv\
—----- cell#\
—-—-—- …aligned_c1.csv\
—-—-—- …aligned_c2.csv\
—----- cell#\
—-—-—- …aligned_c1.csv\
—-—-—- …aligned_c2.csv

## This script will add the following directories with the following structures:

Replicate_name_647\
---- cell#\
-—---- ….aligned_c1.txt\
---- cell#\
-—---- ….aligned_c1.txt\
---- cell#\
-—--- ….aligned_c1.txt

Replicate_name_568\
---- cell#\
-—----- ….aligned_c2.txt\
---- cell#\
-—----- ….aligned_c2.txt\
---- cell#\
-—----- ….aligned_c2.txt

Within each event list, it will also remove the "original file" column, so that it can be processed by SuperResNet Batch

## What to do
Run to change the directory to scratch
```{bash}
cd /scratch/$USER
```

\
(OPTIONAL) You can skip this step if you just ran https://github.com/NanoscopyAI/tutorial_smlm_alignment_colocalization and did not rename the DATASET variable 
```{bash}
export DATASET="/scratch/$USER/FIXME"
```

Run this to download and run the script

```{bash}
wget https://raw.githubusercontent.com/josephsoo/aligned_renaming_script/master/folder.py -O folder.py

python folder.py
```
