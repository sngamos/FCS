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

"The computation time is:  59.40768504142761"