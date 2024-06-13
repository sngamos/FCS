import hashlib
import itertools
import time
import argparse

def openfile(filein):
    with open(filein,'r',encoding='utf-8') as content:
        lines_list = content.readlines()
        output_clean_line_list = []
        for line in lines_list:
            output_clean_line_list.append(line[:-1])
    return output_clean_line_list

#file_content_list = openfile("hash5.txt")

def hash_string(string,algorithm = 'md5'):
    hasher = hashlib.new(algorithm)
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()

def brute_force(charset,length,hashes_list):
    iters = itertools.product(charset,repeat=length)
    hash_dict = {}
    start_time = time.time()
    print("Lets get cracking!")
    for temp in iters:
        i ="".join(temp)
        hash_i = hash_string(i)
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
"""
if __name__ == "__main__":
    CHARSET = "abcdefghijklmnopqrstuvwxyz1234567890"
    LENGTH = 5
    brute_force(CHARSET,LENGTH,file_content_list)
                  

The computation time is:  1014.2041130065918

decryted_dict = {'ddaafa5d551a582bc924d09cc8d33ee5': 'aseas', '96f6065d8f2dd1376eff88fba65d1d83': 'cance', '836626589007d7dd5304c8d22815fffc': 'di5gv', 'a74edf83748e3c4fa5f31ec10bad79db': 'dsmto', '1b31905c59f481958d2eb72158c27ac7': 'egunb', 'a8218c67a5b4e652e30a59372e07df59': 'hed4e', '81466b6bb4be5a48e2230be1338bcde6': 'lou0g', '6e313b70d12de950443527a33d802b76': 'mlhdi', '78c1b8edd1bc3ffc438432479289a9e1': 'nized', 'de952f5454fb0ee79bca249f80e9fe8f': 'ofror', 'a92b66a9802704ca8616c4b092378272': 'opmen', '644674d142ba2174a80889f833b32563': 'owso9', '1b4baba3ae3be69857b323cf6b7fcd80': 'sso55', '0d5b558d5f6744deaaf5b016c6c77a57': 'tpoin', 'd4efdba5e9725e77c9b9051fa8136f0a': 'tthel'}
"""

def write_dict_to_file(decryted_dict,hash_list_in,fileout):
    sorted_list =[None]*len(hash_list_in)
    for key,value in decryted_dict.items():
            sorted_list[hash_list_in.index(key)] = value
    with open(fileout,'w',encoding='utf-8') as content:
        for item in sorted_list:
            content.write(item+'\n')
        content.close()
    return sorted_list



if __name__ == "__main__":
    CHARSET = "abcdefghijklmnopqrstuvwxyz1234567890"
    LENGTH = 5

    parser = argparse.ArgumentParser(description='Brute force attack')
    parser.add_argument("-i",dest="filein",help="The file containing the hashes")
    parser.add_argument("-o",dest="fileout",help="The file containing the decrypted hashes")
    args = parser.parse_args()
    file_in = args.filein
    file_out = args.fileout
    if file_out == None:
        file_out = "ex2_hash.txt"

    file_content_list = openfile(file_in)
    file_content_list_copy = file_content_list.copy()
    decryted_dict =brute_force(CHARSET,LENGTH,file_content_list)
    sorted_list = write_dict_to_file(decryted_dict,file_content_list_copy,file_out)
    print("Brute force attack completed!\nOutput written to: ",file_out)
