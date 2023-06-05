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
    
# Create and make a destination directory for all the renamed files to go
    destination_parent_directory = parent_directory + "_renamed"
    os.makedirs(destination_parent_directory, exist_ok=True)


# Iterate over subfolders
    for folder in glob.glob(os.path.join(parent_directory, "*")):
        if not os.path.isdir(folder):
            continue
    
        folder_name = os.path.basename(folder)
    
        # Create a new directory within each subfolder
        new_directory = os.path.join(destination_parent_directory, folder_name)
        os.makedirs(new_directory, exist_ok=True)

        # Get the names of the files that end in .CC
        files = glob.glob(os.path.join(folder, "*CC.csv"))

        # Check there are a correct number of files
        if len(files) != 2:
                print(f"Unexpected number of files that end in CC in {folder}")
                exit(1)
    
        # Move and rename the aligned_c1.csv file
        c1_file = os.path.join(folder, "aligned_c1.csv")
        c1_new_name = get_name(files[0])
        shutil.move(c1_file, os.path.join(new_directory, c1_new_name))
    
        # Move and rename the aligned_c2.csv file
        c1_file = os.path.join(folder, "aligned_c2.csv")
        c1_new_name = get_name(files[1])
        shutil.move(c1_file, os.path.join(new_directory, c1_new_name))

# Returns the cell line, replicate #, protein, channel, and cell #, and aligned in the correct format
# i.e 1C8PTRF_1_Cav_568_4_aligned.csv
def get_name(filename):
    directories = filename.split(os.sep)
    name = directories[-1]
    core = name.rsplit("_", 1)[0]
    core = core + "_aligned.csv"
    return core

if __name__=="__main__":
   main()