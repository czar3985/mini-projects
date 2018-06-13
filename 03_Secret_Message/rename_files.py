# TITLE: Secret Message Decoder
# DESCRIPTION: A secret message is in folder decodeThis.
# Running this program will rename the files to remove the numbers
# from the file names. When the files are sorted, a secret message
# will appear.
# NOTE: The translate method is different in Python 3.x.
# This was run using Python 2.7.5

import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(".\\decodeThis")
    print(file_list)

    # save the current working directory
    orig_path = os.getcwd()

    # change the current working directory
    os.chdir(".\\decodeThis")

    # for each file, rename filename
    for file_name in file_list:
        new_file_name = file_name.translate(None,"0123456789")
        os.rename(file_name, new_file_name)
        print("Old name: " + file_name + ", New name: " + new_file_name)

    # revert back to the original working directory
    os.chdir(orig_path)
    
rename_files()


