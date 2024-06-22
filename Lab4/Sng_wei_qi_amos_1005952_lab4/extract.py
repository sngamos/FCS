#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

import argparse
from present import *

def getInfo(headerfile):
    with open(headerfile, 'rb') as header_content:
        header = header_content.read()
    return header

def extract(infile,outfile,headerfile):
    header = getInfo(headerfile)
    hashed_list = []
    header_block_len = len(header)
    with open(infile, 'rb') as content, open(outfile, 'wb') as output:
        content.seek(header_block_len+1) # move the file pointer past the header
        output.write(header)
        output.write(b'\n')
        while True:
            encrypted_data = content.read(8)
            if encrypted_data == b'':
                break
            elif encrypted_data not in hashed_list:
                hashed_list.append(encrypted_data)
            else:
                pass

            if encrypted_data == hashed_list[0]:
                output.write(b'00000000')
            else:
                output.write(b'11111111')

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)

            
