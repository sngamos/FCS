#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse


def doStuff(filein, fileout,mode,key):
    # open file handles to both files
    fin = open(filein, mode="r", encoding="utf-8", newline="\n")  # read mode
    fin_b = open(filein, mode="rb")  # binary read mode
    fout = open(fileout, mode="w", encoding="utf-8", newline="\n")  # write mode
    fout_b = open(fileout, mode="wb")  # binary write mode
    c = fin.read()  # read in file into c as a str
    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding="utf-8", newline="\n") as fin:
        text = fin.read()
        # do stuff
        output = ""
        for i in range(len(text)):
            if mode.lower() == "e":
                new_char = int(ord(text[i])) + int(key)
                output += chr(new_char)
            elif mode.lower() == "d":
                new_char = int(ord(text[i])) - int(key)
                output += chr(new_char)
            else:
                print("Error: Invalid input for mode, input either d/e")
                return
        # file will be closed automatically when interpreter reaches end of the block
    with open(fileout,"w",encoding="utf-8",newline="\n") as fout:
        fout.write(output)
        fout.close()
        


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-m", dest="mode", help="mode d/e")
    parser.add_argument("-k", dest="key",help = "key")

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    mode = args.mode
    key = args.key

    doStuff(filein, fileout,mode,key)

    # all done
