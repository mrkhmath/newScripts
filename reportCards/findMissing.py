import os
import shutil
import pandas as pd

# Load the exclusion list from an Excel file
def load_exclusion_list(excel_path, sheet_name=0):
    df = pd.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')
    return df['A'].astype(str).tolist()

# Define the source folder and destination folder
source_folder = input("C:\\Users\\kh_ma\\Downloads\\sorceFolder ").strip()
dest_folder = os.path.join(source_folder, 'newList')

# Specify the path to the Excel file
excel_path = input("C:\\Users\\kh_ma\\Downloads\\School Portal.xlsx ").strip()

# Load the exclusion list from the specified Excel file
exclude_list = load_exclusion_list(excel_path)

# Create the destination folder if it doesn't exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Copy files not in the exclude list
for file in os.listdir(source_folder):
    # Extract file name without extension
    file_name_without_extension = os.path.splitext(file)[0]
    
    # Check if the file is not in the exclude list
    if file_name_without_extension not in exclude_list:
        # Construct source and destination paths
        src_file_path = os.path.join(source_folder, file)
        dest_file_path = os.path.join(dest_folder, file)
        
        # Ensure we're only dealing with files
        if os.path.isfile(src_file_path):
            # Copy file
            shutil.copy(src_file_path, dest_file_path)
            print(f'Copied {file} to {dest_folder}')

print("Copying complete.")
