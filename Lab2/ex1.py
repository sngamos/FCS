import argparse


def open_textfile(file_name):
    with open(file_name,"r",encoding="utf-8") as content:
        text =content.read()
        return text

text = open_textfile("story_cipher.txt")
#print(text)
def count_letter_frequency(string_text):
    letter_dict = {}
    count = 0
    for i in string_text:
        if i not in [" ", '.',',']:
            count+=1
            if i not in letter_dict.keys():
                letter_dict[i] =1
            else:
                letter_dict[i] +=1
    letter_count_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1],reverse=True))
    letter_count_freq_dict = {}
    for k in letter_count_dict.keys():
        letter_count_freq_dict[k] = round(letter_count_dict[k]/count,ndigits=6)
    return letter_count_freq_dict

#letter_freq_dict = count_letter_frequency(text)
#print(letter_freq_dict)
#original_dict = {'U': 0.11159, 'J': 0.09623, 'Y': 0.083790, 'Q': 0.077936, 'E': 0.075375, 'D': 0.075009, 'I': 0.072447, 'X': 0.058543, 'H': 0.047932, 'B': 0.037321, 'T': 0.035858, 'W': 0.025978, 'C': 0.025612, 'S': 0.022319, 'O': 0.021222, 'K': 0.018660, 'M': 0.018294, 'V': 0.018294, 'F': 0.015733, '.': 0.014270, ',': 0.014270, 'R': 0.012806, 'L': 0.010611, 'A': 0.007317, 'N': 0.001097, 'Z': 0.001097, 'P': 0.000365}
#original_dict2 = {'U': 0.114878, 'J': 0.099058, 'Y': 0.086252, 'Q': 0.080226, 'E': 0.077589, 'D': 0.077213, 'I': 0.074576, 'X': 0.060264, 'H': 0.049341, 'B': 0.038418, 'T': 0.036911, 'W': 0.026742, 'C': 0.026365, 'S': 0.022976, 'O': 0.021846, 'K': 0.019209, 'M': 0.018832, 'V': 0.018832, 'F': 0.016196, 'R': 0.013183, 'L': 0.010923, 'A': 0.007533, 'N': 0.00113, 'Z': 0.00113, 'P': 0.000377}
#ref_dict = {'E':0.111607,'A':0.084966,'R':0.075809,'I':0.075448,'O':0.071635,'T':0.069509,'N':0.066544,'S':0.057351,'L':0.054893,'C':0.045388,'U':0.036308,'D':0.033844,'P':0.031671,'M':0.030129,'H':0.030034,'G':0.024705,'B':0.020720,'F':0.018121,'Y':0.017779,'W':0.012899,'K':0.011016,'V':0.010074,'X':0.002902,'Z':0.002722,'J':0.001965,'Q':0.001962}

def create_replacement_letters(frequency_dict,reference_dict):
    replacement_dict = {}
    max_len = min(len(frequency_dict),len(reference_dict))
    for i in range(max_len):
        replacement_dict[list(frequency_dict.keys())[i]] = list(reference_dict.keys())[i]
    return replacement_dict
#replacement_dict = create_replacement_letters(original_dict2,ref_dict)
#print(replacement_dict)


replacement_dict = {'U': 'E', 'J': 'A', 'Y': 'R', 'Q': 'I', 'E': 'O', 'D': 'T', 'I': 'N', 'X': 'S', 'H': 'L', 'B': 'C', 'T': 'U', 'W': 'D', 'C': 'P', 'S': 'M', 'O': 'H', 'K': 'G', 'M': 'B', 'V': 'F', 'F': 'Y', 
'R': 'W', 'L': 'K', 'A': 'V', 'N': 'X', 'Z': 'Z', 'P': 'J'}

def replace_letters(plain_text,replacement_dict):
    new_text=''
    for char in plain_text:
        if char != ' ' and char in replacement_dict.keys():
            new_text += replacement_dict[char]
        elif char == ' ':
            new_text += ' '
        elif char not in replacement_dict.keys():
            new_text += char
    return new_text

#decrypt_text = replace_letters(text,replacement_dict)
#print(decrypt_text)

def doStuff(filein,fileout=None):
    #reading the input file
    with open(filein,"r",encoding="utf-8") as content:
       plain_text =content.read()
    #monogram
    replacement_dict = {'U': 'E',
                     'J': 'T',
                       'Y': 'I',
                         'Q': 'A',
                           'E': 'O',
                             'D': 'N',
                               'I': 'S',
                                 'X': 'H',
                                   'H': 'R',
                                     'B': 'L',
                                       'T': 'D',
                                         'W': 'G',
                                           'C': 'M',
                                             'S': 'C',
                                               'O': 'Y',
                                                 'K': 'U',
                                                   'M': 'W',
                                                     'V': 'F',
                                                       'F': 'P',
                                                         'R': 'B',
                                                           'L': 'V',
                                                             'A': 'K',
                                                               'N': 'X',
                                                                 'Z': 'Z',
                                                                   'P': 'J'}
    #replace letters
    new_text=''
    for char in plain_text:
        if char != ' ' and char in replacement_dict.keys():
            new_text += replacement_dict[char]
        elif char == ' ':
            new_text += ' '
        elif char not in replacement_dict.keys():
            new_text += char
    if fileout == None:
        with open('decrypted_'+filein,'w',encoding='utf-8')as fout:
            fout.write(new_text)
            fout.close()
    else:
        with open(fileout,'w',encoding='utf-8')as fout:
            fout.write(new_text)
            fout.close()



    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i",dest = "filein",help= "input file")
    parser.add_argument('-o',dest= 'fileout',help = 'output file')
    args = parser.parse_args()
    filein= args.filein
    fileout = args.fileout
    doStuff(filein,fileout)
