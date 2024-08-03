# ex3.py
from Crypto.PublicKey import RSA
from primes import *

def encrypt(message, e, n):
    m = int.from_bytes(message.encode('utf-8'), byteorder='big')
    return square_multiply(m, e, n)

def decrypt(ciphertext, d, n):
    return square_multiply(ciphertext, d, n)

def rsa_protocol_attack(encrypted_int, s, e, n, d):
    # Encrypt s
    encrypted_s = square_multiply(s, e, n)
    # Multiply encrypted integer with encrypted s
    modified_encrypted_int = (encrypted_int * encrypted_s) % n
    # Decrypt the modified ciphertext
    decrypted_modified_int = square_multiply(modified_encrypted_int, d, n)
    return modified_encrypted_int, decrypted_modified_int

if __name__ == "__main__":
    # Import public key
    with open('mykey.pem.pub', 'r') as f:
        public_key = RSA.import_key(f.read())
    
    n = public_key.n
    e = public_key.e

    # Import private key
    with open('mykey.pem.priv', 'r') as f:
        private_key = RSA.import_key(f.read())
    
    d = private_key.d

    # Part II - Encrypting an integer (e.g. 100)
    plaintext_int = 100
    plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big')
    encrypted_int = square_multiply(plaintext_int, e, n)
    print(f"Encrypting: {plaintext_int}")
    print(f"Result:\n{encrypted_int}")

    # RSA Encryption Protocol Attack
    s = 2
    modified_encrypted_int, decrypted_modified_int = rsa_protocol_attack(encrypted_int, s, e, n, d)
    print(f"Modified to:\n{modified_encrypted_int}")
    print(f"Decrypted: {decrypted_modified_int}")
