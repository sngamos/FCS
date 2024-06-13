import argparse
import random


def load_hashes(filein):
    with open(filein,'r',encoding='utf-8') as content:
        lines_list = content.readlines()
        output_clean_line_list = []
        for line in lines_list:
            output_clean_line_list.append(line[:-1])
    return output_clean_line_list

