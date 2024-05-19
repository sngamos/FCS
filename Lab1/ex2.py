import sys
import argparse

def function(filein,fileout,mode,key):
    with open(filein, mode="rb", encoding="utf-8", newline="\n") as fin:
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
    with open(fileout,"wb",encoding="utf-8",newline="\n") as fout:
        fout.write(output)
        fout.close()

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

    function(filein, fileout,mode,key)

    # all done