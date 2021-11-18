#!/usr/bin/env python3

# imports
import sys
import os

def get_input_files(folder):
    """
    :param folder: Input folder
    :return
    """
    try:
        for entry in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, entry)):
                print("%s" % (entry))
    except:
        exit(1)


# main #
def main():

    print("This is the name of the script:", sys. argv[0])
    print("This is the name of the input file:", sys. argv[1])

    folder=get_input_files(sys. argv[1])

if __name__ == "__main__":
    main()


