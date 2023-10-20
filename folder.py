import os
import glob
import shutil

def main():
# gets the parent directory path
    parent_directory = os.environ['DATASET']

# Check if the parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)
    # Create a destination directory for all the renamed files to go
    destination_parent_directory_c1 = parent_directory + "_647" 
    destination_parent_directory_c2 = parent_directory + "_568" 
    os.makedirs(destination_parent_directory_c1, exist_ok=True)
    os.makedirs(destination_parent_directory_c2, exist_ok=True)

    move_files(parent_directory, destination_parent_directory_c1, destination_parent_directory_c2)
    remove_last_column(destination_parent_directory_c1)
    remove_last_column(destination_parent_directory_c2)

# given a path that ends in .csv, returns the base file name that ends in .txt
def get_name(filename):
    name = os.path.basename(filename)
    core = name.rsplit(".", 1)[0]
    core = core + ".txt"
    return core

def move_files(source_directory, c1_directory, c2_directory):
    for file in glob.glob(os.path.join(source_directory, "*")):
        if os.path.isdir(file):
            folder_name = os.path.basename(file)
            new_c1_directory = os.path.join(c1_directory, folder_name)
            os.makedirs(new_c1_directory, exist_ok=True)
            new_c2_directory = os.path.join(c2_directory, folder_name)
            os.makedirs(new_c2_directory, exist_ok=True)
            
            move_files(file, new_c1_directory, new_c2_directory)
        else:
            if ("aligned_c1.csv" in file):
                shutil.move(file, os.path.join(c1_directory, get_name(file)))
            if ("aligned_c2.csv" in file):
                shutil.move(file, os.path.join(c2_directory, get_name(file)))

def remove_last_column(parent_directory):
    parent_directory = os.environ['DATASET']
# Check if the parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)

    for folder in glob.glob(os.path.join(parent_directory, "*")):


        if not os.path.isdir(folder):
            continue


        for textfile in glob.glob(os.path.join(folder, "*")):
            with open(textfile, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

# Get the value of the upper right cell
            upper_right_cell = rows[0][-1]

# Check if it equals 'originalfile'
            if upper_right_cell == 'originalfile':
                print(f"deleting last column for {textfile}")
    # Remove the last column
                for row in rows:
                    del row[-1]

# Write the modified data back to the CSV file
            with open(textfile, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)


if __name__=="__main__":
   main()
