import hashlib
import itertools

def openfile(filein):
    with open(filein,'r',encoding='utf-8') as content:
        lines_list = content.readlines()
        output_clean_line_list = []
        for line in lines_list:
            output_clean_line_list.append(line[:-1])
    return output_clean_line_list

file_content_list = openfile("hash5.txt")

def hash_string(string,algorithm = 'md5'):
    hasher = hashlib.new(algorithm)
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()

def generate_strings(charset,length):
    iters = itertools.product(charset,repeat=length)
    for temp in iters:
        i =''.join(temp)
        print(i)


generate_strings("abc",2)
