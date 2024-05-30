import sys
import argparse

def b_func(filein,fileout,mode,key):
    with open(filein, mode="rb") as fin:
        text = fin.read()
        output = b""
        if mode.lower() == "e":
            for i in range(len(text)):
                new_char = (int(text[i]) + int(key))%256
                output += bytes([new_char])
        elif mode.lower() == "d":
            for i in range(len(text)):
                new_char = (int(text[i]) - int(key))%256
                output += bytes([new_char])
        elif mode.lower() == "flag":
            for k in range(256):
                k_fileout = fileout + "_" + str(k)
                b_func(filein,k_fileout,"d",k)
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

#when key = 246 the flag is decrypted to a PNG image of a flag of Switzerland