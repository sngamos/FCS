import argparse
import random
import hashlib
import itertools
import time
def load_hashes(filein):
    with open(filein,'r',encoding='utf-8') as content:
        lines_list = content.readlines()
        output_clean_line_list = []
        for line in lines_list:
            output_clean_line_list.append(line[:-1])
    return output_clean_line_list

def salting(string_list,charset):
    salted_list = []
    for string in string_list:
        salt = random.choice(charset)
        salted_string = string + salt
        salted_list.append((salted_string))
    return salted_list

def hash_list(string_list):
    hash_list = []
    for string in string_list:
        hash_list.append(hashlib.md5(string.encode('utf-8')).hexdigest())
    return hash_list

def storing_salted_hashes(fileout_hash,fileout_plaintext,old_plaintext_list):
    with open(fileout_hash,'w',encoding='utf-8') as content:
        CHARSET = 'abcdefghijklmnopqrstuvwxyz'
        print("Salting the hashbrowns")
        salted_list = salting(old_plaintext_list,CHARSET)
        print("Hashing the salted hashbrowns")
        hashed_list = hash_list(salted_list)
        if len(salted_list) != len(hashed_list):
            return "Error not same length of hash and salted list"
        else:
            print("Storing the salted hashbrowns")
            for i in range(len(salted_list)):
                content.write(hashed_list[i]+'\t'+salted_list[i][1]+'\n')
            content.close()
    print("Storing the salted plaintexts")
    with open(fileout_plaintext,'w',encoding='utf-8') as content:
        content.write('\n'.join(salted_list))
        content.close()
    return hashed_list


def brute_force_salted(charset,length,hashes_list):
    iters = itertools.product(charset,repeat=length)
    hash_dict = {}
    start_time = time.time()
    print("Starting salty hashbrown cracker!")
    for temp in iters:
        i ="".join(temp)
        hash_i = hashlib.md5(i.encode('utf-8')).hexdigest()
        #print(hash_i)
        #print("Cracked hashes: ",len(hash_dict), "Remaining hashes: ",len(hashes_list))
        if hash_i in hashes_list:
            print("Found a match: ",hash_i," for the string: ",i)
            hash_dict[hash_i] = i
            hashes_list.remove(hash_i)
            print("Cracked hashes: ",len(hash_dict), "Remaining hashes: ",len(hashes_list))
            if len(hashes_list) == 0:
                break
    end_time = time.time()  
    computation_time = end_time - start_time
    print("The computation time is: ",computation_time)
    #print(hash_dict)
    return hash_dict

def write_dict_to_file(decryted_dict,hash_list_in,fileout):
    sorted_list =[None]*len(hash_list_in)
    for key,value in decryted_dict.items():
            sorted_list[hash_list_in.index(key)] = value
    with open(fileout,'w',encoding='utf-8') as content:
        for item in sorted_list:
            content.write(item+'\n')
        content.close()
    return sorted_list

def store_hashes(fileout,hash_list):
    with open(fileout,'w',encoding='utf-8') as content:
        for item in hash_list:
            content.write(item+'\n')
        content.close()

if __name__ == "__main__": 

    parser =argparse.ArgumentParser(description='Salt and crack strings')
    parser.add_argument("-i",dest="filein",help="The file containing the plaintexts to salt")
    parser.add_argument("-o",dest="fileout",help="The file containing the cracked salted plaintexts")
    args = parser.parse_args()
    filein = args.filein
    fileout=args.fileout
    if fileout == None:
        fileout = "ex3_hash.txt"
    CHARSET = "abcdefghijklmnopqrstuvwxyz1234567890"
    SALT = "abcdefghijklmnopqrstuvwxyz"
    LENGTH = 6

    print("Loading the hashbrowns")
    file_content_list = load_hashes(args.filein)
    salted_hash_list =storing_salted_hashes("salted6.txt","plain6.txt",file_content_list)
    salted_hash_list_copy = salted_hash_list.copy()
    hash_dict = brute_force_salted(CHARSET,LENGTH,salted_hash_list)
    sorted_list = write_dict_to_file(hash_dict,salted_hash_list_copy,fileout)
    print("Completed cracking salted hashbrowns!")

"The computation time is:  2158.5144486427307"