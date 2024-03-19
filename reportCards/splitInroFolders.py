import os
import shutil

def split_files_equally(source_folder, dest_base_path, max_files_per_folder=90):
    # Get a list of all files in the source folder
    files = [file for file in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file))]
    total_files = len(files)
    
    # Calculate the number of required folders
    required_folders = total_files // max_files_per_folder + (1 if total_files % max_files_per_folder else 0)
    
    # Create and populate folders
    for folder_number in range(required_folders):
        folder_path = os.path.join(dest_base_path, f'Folder_{folder_number+1}')
        os.makedirs(folder_path, exist_ok=True)
        
        # Determine files to move to the current folder
        start_index = folder_number * max_files_per_folder
        end_index = start_index + max_files_per_folder
        files_to_move = files[start_index:end_index]
        
        # Move files
        for file_name in files_to_move:
            shutil.copy(os.path.join(source_folder, file_name), os.path.join(folder_path, file_name))
        
        print(f'Created {folder_path} and moved {len(files_to_move)} files.')

if __name__ == '__main__':
    source_folder = input("Enter the path to the source folder: ").strip()
    dest_base_path = input("Enter the base path for the new folders: ").strip()
    
    split_files_equally(source_folder, dest_base_path)
