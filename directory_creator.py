 #!/usr/bin/env python

 ##############################################################################
 #    directory_creator.py
 #
 #    This File will take a directory and create a set of subfolders
 #    in the current working directory. I use this file for creating
 #    a set of sub folders for my photograph organization.
 #
##############################################################################

import os
import sys


"""

main()
The main execution point for this command-line tool. This should
be run within the folder you wish to create the month folders.

"""

def main():
    '''
    The data will be stored as a list and then
    '''


    print("Folder creation tool.")
    months = ["01_Jan",
              "02_Feb",
              "03_Mar",
              "04_Apr",
              "05_May",
              "06_Jun",
              "07_Jul",
              "08_Aug",
              "09_Sep",
              "10_Oct",
              "11_Nov",
              "12_Dec"
              ]
    print("Print the current working Directory to ensure correct location.\n")
    path = os.getcwd()
    print(path)

    for month in months:
        tar_dir = os.path.join(path, month)
        print("Creating folder: " + tar_dir)
        os.mkdir(tar_dir)
    print("Now Show the list of new directories created")
    directories = os.listdir(os.getcwd())
    for dir in directories:
        print(str(dir))


if __name__ == '__main__': main()