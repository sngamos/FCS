import sys
import argparse

def b_func(filein,fileout,mode,key):
    with open(filein, mode="rb") as fin:
        text = fin.read()
        output = b""
        for i in range(len(text)):
            if mode.lower() == "e":
                new_char = int(text[i]) + int(key)
                output += bytes([new_char])
            elif mode.lower() == "d":
                new_char = int(text[i]) - int(key)
                output += bytes([new_char])
            else:
                print("Error: Invalid input for mode, input either d/e")
                return
    with open(fileout,"wb") as fout:
        fout.write(output)
        fout.close()

if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-m", dest="mode", help="mode d/e")
    parser.add_argument("-k", dest="key",help = "key")

    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    mode = args.mode
    key = args.key

    b_func(filein, fileout,mode,key)

