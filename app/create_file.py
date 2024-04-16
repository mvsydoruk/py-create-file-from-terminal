import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        file.write(f'{datetime.now().strftime("%y-%m-%d %H:%M:%S")}\n')
        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1
        file.write("\n")


def create_directory(directory_list: list) -> None:
    dir_path = os.path.join(*directory_list)
    os.makedirs(dir_path, exist_ok=True)


args = sys.argv[1:]
dir_list = []
file_name = ""
if "-d" in args:
    for arg in args[1:]:
        if arg == "-f":
            break
        dir_list.append(arg)
if "-f" in args:
    file_name = args[-1]

if dir_list and file_name:
    create_directory(dir_list)
    file_path = os.path.join(*dir_list, file_name)
    create_file(file_path)
elif not dir_list and file_name:
    create_file(file_name)
elif dir_list and not file_name:
    create_directory(dir_list)
