import os
import glob
import csv

kept_columns = ['x [nm]', 'y [nm]', 'z [nm]', "xnm", "ynm", "znm"]
keyword = ""  # Set this if you want to filter files based on some keyword.

def main():
    parent_directory = os.environ.get('DATASET')

    if not os.path.isdir(parent_directory):
        print(f"Error: The parent directory '{parent_directory}' does not exist.")
        exit(1)
    
    print(f"Parent directory: {parent_directory}")
    confirmation = input("Is this the correct directory to apply changes? (yes/cancel): ").strip().lower()
    if confirmation == "yes":
        remove_columns(parent_directory)
    elif confirmation == "cancel":
        print("Operation cancelled.")
    else:
        print("Invalid response. Operation cancelled.")

def remove_columns(parent_directory):
    for item in glob.glob(os.path.join(parent_directory, "**", "*.csv"), recursive=True):
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
            print(f"Updated file: {item}")

if __name__ == "__main__":
    main()
