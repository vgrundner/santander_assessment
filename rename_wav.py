#!/usr/bin/env python3
# Author: Verena Grundner
# Created: 19.11.2021

# imports
import sys
import os
import time

# functions
def rename_input_files(folder):
    """
    :param folder: Input folder
    """
    # wav file counter
    cnt = 0

    # loop over all files of given input folder
    for entry in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, entry)):
            # select wav-files only
            if entry.endswith('.wav'):
                cnt += 1
                # create zero padded string out of counter
                z_cnt = (str(cnt).zfill(3))
                try:
                    # get creation date of .wav-file
                    file_date=time.strftime('%Y-%m-%d',time.gmtime(os.path.getmtime(folder + entry)))
                    # rename wav files only
                    renamed_file='audiofile_' + file_date + '_' + z_cnt + '.wav'
                    os.rename((folder+entry),folder+renamed_file)
                    print("Renamed %s to %s" % (entry, renamed_file))

                except Exception as ex:
                    # if an exception occurs, show type of it
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
                    exit(1)


# main 
def main():

    print("This is the given input folder:", sys. argv[1])
    rename_input_files(sys. argv[1])
    print("Renaming of wav files finished")

if __name__ == "__main__":
    main()


