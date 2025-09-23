import os

#add prefix to all files
def prefix_files_in_folder(folder_path):
    folder_name = folder_path.rstrip("/\\").split(os.sep)[folder_path.rstrip("/\\").split(os.sep).index("Master") + 1]
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Skip if already prefixed
        if filename.startswith(folder_name + "_"):
            continue
        #rename files
        else:
            new_name = f"{folder_name}_{filename}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
            
#loop through the folder
def rename_the_files(dir_path, file_list):
    for file in file_list:
        current_file_path = os.path.join(dir_path, file)
        
        if os.path.isdir(current_file_path) and os.path.basename(current_file_path) != "folder_scripts":
            rename_the_files(current_file_path, os.listdir(current_file_path))
            prefix_files_in_folder(current_file_path)
        
        
main_dir = r"C:\Users\tobyt\OneDrive\ETH OneDrive_Personal\Master"
file_list = os.listdir(main_dir)

rename_the_files(main_dir, file_list)

