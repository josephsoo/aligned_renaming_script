import os
import glob
import shutil
import csv

kept_columns = ['x [nm]', 'y [nm]', 'z [nm]', "xnm", "ynm", "znm"]
keyword = ""  # Make sure this is set if you want to filter files based on some keyword.

def main():
    parent_directory = os.environ['DATASET']

    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)

    destination_parent_directory_c1 = parent_directory + "_647"
    destination_parent_directory_c2 = parent_directory + "_568"
    os.makedirs(destination_parent_directory_c1, exist_ok=True)
    os.makedirs(destination_parent_directory_c2, exist_ok=True)

    move_files(parent_directory, destination_parent_directory_c1, destination_parent_directory_c2)
    remove_columns(destination_parent_directory_c1)
    remove_columns(destination_parent_directory_c2)

def get_name(filename):
    name = os.path.basename(filename)
    core = name.rsplit(".", 1)[0]
    core = core + ".txt"  # Modify to ".txt" if conversion happens before, or keep as ".csv" and convert after.
    return core

def move_files(source_directory, c1_directory, c2_directory):
    for file in glob.glob(os.path.join(source_directory, "**", "*.csv"), recursive=True):  # Use recursive glob to find all CSV files.
        if "aligned_c1.csv" in file:
            # Determine new directory based on file path.
            relative_path = os.path.relpath(os.path.dirname(file), source_directory)
            new_c1_directory = os.path.join(c1_directory, relative_path)
            os.makedirs(new_c1_directory, exist_ok=True)
            shutil.move(file, os.path.join(new_c1_directory, get_name(file)))
        elif "aligned_c2.csv" in file:
            relative_path = os.path.relpath(os.path.dirname(file), source_directory)
            new_c2_directory = os.path.join(c2_directory, relative_path)
            os.makedirs(new_c2_directory, exist_ok=True)
            shutil.move(file, os.path.join(new_c2_directory, get_name(file)))

def remove_columns(parent_directory):
    for item in glob.glob(os.path.join(parent_directory, "**", "*.csv"), recursive=True):  # Ensure this matches the files you want to edit.
        if keyword in item:
            with open(item, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

                remove_columns_indexes = [rows[0].index(header) for header in rows[0] if header not in kept_columns]

                # Remove columns not in kept_columns.
                for i in reversed(remove_columns_indexes):
                    for row in rows:
                        del row[i]

            with open(item, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

if __name__ == "__main__":
    main()
