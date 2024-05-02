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

    remove_columns(parent_directory)

def get_name(filename):
    name = os.path.basename(filename)
    core = name.rsplit(".", 1)[0]
    core = core + ".csv"  # Modify to ".txt" if conversion happens before, or keep as ".csv" and convert after.
    return core

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
