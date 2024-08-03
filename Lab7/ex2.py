from Crypto.PublicKey import RSA
from primes import *
from Crypto.Hash import SHA256


def encrypt(message, e ,n):

    m = int.from_bytes(message.encode('utf'), 'big')
    return square_multiply(m, e, n)


def decrypt(cipher, d ,n):
    return square_multiply(cipher, d, n)

def sign(message, d, n):
    #Hash the message using SHA256
    h = SHA256.new(message.encode('utf'))
    #exponentiate digest
    m = int.from_bytes(h.digest(), 'big')
    return square_multiply(m, d, n)

def verify_signature(signature, message, e, n):
    #Hash the message using SHA256
    hash_obj = SHA256.new(message.encode('utf-8'))
    hash_int = int.from_bytes(hash_obj.digest(), byteorder='big')
    verified_hash = square_multiply(signature, e, n)
    return hash_int == verified_hash

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

    # Encrypt message
    with open('message.txt', 'r') as f:
        message = f.read()
    
    ciphertext = encrypt(message, e, n)
    print("Encrypted message:", ciphertext)

    # Decrypt message
    decrypted_message = decrypt(ciphertext, d, n)
    decrypted_message_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')
    print("Decrypted message:", decrypted_message_bytes.decode('utf-8'))

    # Create signature
    signature = sign(message, d, n)
    print("Signature:", signature)

    # Verify signature
    is_valid = verify_signature(signature, message, e, n)
    print("Signature valid:", is_valid)