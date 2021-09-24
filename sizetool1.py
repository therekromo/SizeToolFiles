#1 take argparse argument for directory/path (maybe use sysargv instead, no need to unit test this)
#2 create function to get the size of that directory and subfolders/files in it (make sure this only needs to take in the argparse input)
#3 create a function for the conversion portion (do this with the code on the pc and make sure it only takes in one argument
#4 create a function that uses all outputs of the previous 2 functions and puts them into 1 print statement instead

#Argparse argument here
import argparse

import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Directory',  nargs='+', help = "Input directories you would like to check seperated by a space")
    args = parser.parse_args()

    for singledirectory in args.Directory:
        #print (singledirectory)
        get_path_size(singledirectory)

    #here, if the argparser takes in multiple paths into a list, this is where it will happen
    #in list of argparse, in list of list of argparse, find path etc.


def get_path_size(singledirectory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(singledirectory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            total_size += os.path.getsize(fp)

    print(conversion(singledirectory, total_size))
    return total_size

    #here, find the size of the individual path which was extracted from the above function

def conversion(singledirectory, total_size):
    byte_tag = ['Bytes', 'KB', 'MB', 'GB']
    for i in range(len(byte_tag)-1,-1,-1):
        if total_size // (1040 ** i) > 1:
            return singledirectory+' ' +str(total_size//(1040 ** i)) + byte_tag[i]
    if total_size == 0:
        return 0


if __name__ == '__main__':
    main()
