import os

#gets the prefix
def get_prefix(directory_path):
    dir_strip = directory_path.rstrip("/\\").split(os.sep)
    dir_strip = [x for x in dir_strip if x not in main_strip]
    return dir_strip[0]

#add prefix to all files
def prefix_files_in_folder(folder_path):
    folder_name = str(get_prefix(folder_path))
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Skip if already prefixed
        if filename.startswith(folder_name + "_") or filename.startswith("IGN_"): #ignore tag IGN_
            continue
        #rename files
        new_name = f"{folder_name}_{filename}" 
        new_path = os.path.join(folder_path, new_name)
        if not os.path.exists(new_path):
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
        else:
            print("duplicate file names detected")
            
#loop through current folder
def rename_the_files(dir_path, file_list):
    for file in file_list:
        current_file_path = os.path.join(dir_path, file)
        
        if file.startswith("IGN_"):
            continue
        
        if os.path.isdir(current_file_path):
            rename_the_files(current_file_path, os.listdir(current_file_path)) #recursively loop through all the folders in the current folder
            prefix_files_in_folder(current_file_path)
        


main_dir = r""# type your main directory in the quotes
main_strip = main_dir.rstrip("/\\").split(os.sep)
file_list = os.listdir(main_dir)

rename_the_files(main_dir, file_list)

