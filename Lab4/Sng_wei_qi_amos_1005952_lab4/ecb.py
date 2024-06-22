#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

from present import *
import argparse

nokeybits=80
blocksize=64


def ecb(infile, outfile, key, mode):
    with open(infile, 'rb') as content:
        with open(outfile, 'wb') as content_out:
            while True:
                block = content.read(blocksize // 8)  # Read 8 bytes (64 bits)
                if len(block) == 0:
                    print("{modes} completed".format(modes = mode))
                    break
                elif len(block) < blocksize // 8:
                    # Padding the last block if it's less than 64 bits
                    block += b'\x00' * (blocksize // 8 - len(block))
                
                block_int = int.from_bytes(block, byteorder='big')
                
                if mode == 'encrypt':
                    processed_block = present(block_int, key)
                elif mode == 'decrypt':
                    processed_block = present_inv(block_int, key)
                else:
                    raise ValueError("Mode should be either 'encrypt' or 'decrypt'")
                
                content_out.write(processed_block.to_bytes(blocksize // 8, byteorder='big'))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode

    with open(keyfile, 'r') as kf:
        key = int(kf.read(), 16)  # Read the key as a hexadecimal string and convert to integer

    ecb(infile, outfile, key, mode)

