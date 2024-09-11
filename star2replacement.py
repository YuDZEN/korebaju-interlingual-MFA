# author YuDZEN

import os
import sys

# define the replacement character you can change it to any character you want, but not a existing character in the textgrid file
replacement = 'ɕ'

def replace_star_in_textgrid(file_path, replacement):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('*', replacement)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_textgrid_files(folder_path, replacement):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.TextGrid'):
                file_path = os.path.join(root, file)
                replace_star_in_textgrid(file_path, replacement)

def replace_star_in_mapping_and_dict(file_paths, replacement):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = content.replace('*', replacement)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python star2replacement.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    mapping_file = sys.argv[2]
    dict_file = sys.argv[3]
    
    process_textgrid_files(folder_path, replacement)
    replace_star_in_mapping_and_dict([mapping_file, dict_file], replacement)
