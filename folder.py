import os
import glob
import shutil

def main():
# gets the parent directory path from bash
    parent_directory = os.environ['DATASET']

# Check if the parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)
    # Create a destination directory for all the renamed files to go
    destination_parent_directory_647 = parent_directory + "_aligned_c1" 
    destination_parent_directory_568 = parent_directory + "_aligned_c2" 
    os.makedirs(destination_parent_directory_647, exist_ok=True)
    os.makedirs(destination_parent_directory_568, exist_ok=True)

# Iterate over subfolders
    cc = parent_directory + os.sep + "cc"

    # iterates over subfolders, i.e. 1, 2, 3
    for folder in glob.glob(os.path.join(cc, "*")):

        if not os.path.isdir(folder):
            continue
    
        folder_name = os.path.basename(folder)
    
        # Create a folder for the Cav files to go
        new_directory_c1 = os.path.join(destination_parent_directory_647, folder_name)
        os.makedirs(new_directory_c1, exist_ok=True)

        # Create a folder for the PTRF files to go
        new_directory_c2 = os.path.join(destination_parent_directory_568, folder_name)
        os.makedirs(new_directory_c2, exist_ok=True)

        # moves aligned_c1 and aligned_c2 to the appropriate folders
        for file in glob.glob(os.path.join(folder, "*")):
            if not os.path.isfile(file):
                continue
            if ("aligned_c1" in file):
               shutil.move(file, os.path.join(new_directory_c1, get_name(file)))
            if ("aligned_c2" in file):
                shutil.move(file, os.path.join(new_directory_c2, get_name(file)))
  

# given a path that ends in .csv, returns the base file name that ends in .txt
def get_name(filename):
    directories = filename.split(os.sep)
    name = directories[-1]
    core = name.rsplit(".", 1)[0]
    core = core + ".txt"
    return core

if __name__=="__main__":
   main()
