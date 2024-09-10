import os
import sys


# define the replacement character you can change it to any character you want, but not a existing character in the textgrid file
replacement = 'ʘ'  

def replace_replacement_in_textgrid(file_path, replacement):
    with open(file_path, 'r') as file:
        content = file.read()
    
    new_content = content.replace(replacement, '*')
    
    with open(file_path, 'w') as file:
        file.write(new_content)

def process_textgrid_files(folder_path, replacement):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.textgrid'):
                file_path = os.path.join(root, file)
                replace_replacement_in_textgrid(file_path, replacement)

def replace_replacement_in_mapping_and_dict(file_paths, replacement):
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = content.replace(replacement, '*')
        
        with open(file_path, 'w') as file:
            file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python replacement2star.py <folder_path1> <folder_path2> <mapping_file> <dict_file>")
        sys.exit(1)

    folder_path1 = sys.argv[1]
    folder_path2 = sys.argv[2]
    mapping_file = sys.argv[3]
    dict_file = sys.argv[4]
    

    process_textgrid_files(folder_path1, replacement)

    process_textgrid_files(folder_path2, replacement)

    replace_replacement_in_mapping_and_dict([mapping_file, dict_file], replacement)