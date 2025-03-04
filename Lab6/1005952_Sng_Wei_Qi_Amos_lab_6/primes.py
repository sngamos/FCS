# 50.042 FCS Lab 6 template
# Year 2021

import random
def square_multiply(a,x,n):
    y =1
    n_b = bin(x)[2:]
    for i in range(len(n_b)):
        y=(y**2)%n
        if n_b[i]=='1':
            y=(y*a)%n
    return y

def miller_rabin(n, a):
    pass

def gen_prime_nbits(n):
    pass
"""
if __name__=="__main__":
    print('Is 561 a prime?')
    print(miller_rabin(561,2))
    print('Is 27 a prime?'
    print(miller_rabin(27,2))
    print('Is 61 a prime?'
    print(miller_rabin(61,2))

    print('Random number (100 bits):')
    print(gen_prime_nbits(100))
    print('Random number (80 bits):')
    print(gen_prime_nbits(80))
"""
print(square_multiply(2,33,5))
