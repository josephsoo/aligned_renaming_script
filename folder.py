import os
import glob
import shutil

def main():
# Prompt the user to enter the parent directory path
    parent_directory = input("Enter the path to the parent directory: ")

# Check if the parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)
    
# Create a destination directory for all the renamed files to go
    destination_parent_directory_cav = parent_directory + "_Cav_aligned"
    destination_parent_directory_ptrf = parent_directory + "_PTRF_aligned"
    os.makedirs(destination_parent_directory_cav, exist_ok=True)
    os.makedirs(destination_parent_directory_ptrf, exist_ok=True)

# Iterate over subfolders
    for folder in glob.glob(os.path.join(parent_directory, "*")):
        if not os.path.isdir(folder):
            continue
    
        folder_name = os.path.basename(folder)
    
        # Create a folder for the Cav files to go
        new_directory_cav = os.path.join(destination_parent_directory_cav, folder_name)
        os.makedirs(new_directory_cav, exist_ok=True)

        # Create a folder for the PTRF files to go
        new_directory_ptrf = os.path.join(destination_parent_directory_ptrf, folder_name)
        os.makedirs(new_directory_ptrf, exist_ok=True)

        # moves aligned_c1 and aligned_c2 to the appropriate folders
        for file in glob.glob(os.path.join(folder, "*")):
            if not os.path.isfile(folder):
                continue
            if ("aligned_c1" in file):
                shutil.move(file, os.path.join(new_directory_cav, get_name(file)))
            if ("aligned_c2" in file):
                shutil.move(file, os.path.join(new_directory_cav, get_name(file)))
  

# given a path that ends in .csv, returns the base file name that ends in .txt
def get_name(filename):
    directories = filename.split(os.sep)
    name = directories[-1]
    core = name.rsplit(".", 1)[0]
    core = core + ".txt"
    return core

if __name__=="__main__":
   main()