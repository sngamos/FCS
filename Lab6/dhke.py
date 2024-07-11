# 50.042 FCS Lab 6 template
# Year 2021

from primes import *
import random
from present import present, present_inv



def dhke_setup(nb):
    p = 1208925819614629174706189
    a = 2
    return p,a



def gen_priv_key(p):
    a = random.randint(1, p-2)
    return a


def get_pub_key(alpha, a, p):
    A = square_multiply(alpha, a, p)
    return A


def get_shared_key(keypub, keypriv, p):
    sharedkey = square_multiply(keypub, keypriv, p)
    return sharedkey


message = "Hello, World!"



if __name__ == "__main__":
    p, alpha = dhke_setup(80)
    print("Generate P and alpha:")
    print("P:", p)
    print("alpha:", alpha)
    print()
    a = gen_priv_key(p)
    b = gen_priv_key(p)
    print("My private key is: ", a)
    print("Test other private key is: ", b)
    print()
    A = get_pub_key(alpha, a, p)
    B = get_pub_key(alpha, b, p)
    print("My public key is: ", A)
    print("Test other public key is: ", B)
    print()
    sharedKeyA = get_shared_key(B, a, p)
    sharedKeyB = get_shared_key(A, b, p)
    print("My shared key is: ", sharedKeyA)
    print("Test other shared key is: ", sharedKeyB)
    print("Length of key is %d bits." % sharedKeyA.bit_length())
    message = 123
    print("My plaintext: " , message)
    cipher = present(bin(message)[2:], bin(sharedKeyA)[2:])
    print("My Cipher text: ", cipher)
    decrypt = present_inv(bin(cipher)[2:], bin(sharedKeyB)[2:])
    print("Your decrypted message: ", decrypt)