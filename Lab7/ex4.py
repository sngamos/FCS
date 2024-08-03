from Crypto.PublicKey import RSA
import random
from primes import *


if __name__ == "__main__":
    # Import public key
    with open('mykey.pem.pub', 'r') as f:
        public_key = RSA.import_key(f.read())
    
    n = public_key.n
    e = public_key.e

    # Alice's part
    # Choose a 1024-bit integer s
    s = random.getrandbits(1024)

    # Compute the new message x using the public key: x ≡ s^e mod n
    x = square_multiply(s, e, n)

    # On behalf of Alice, send the signature s and the message x to Bob
    print("Alice's part:")
    print(f"Message (x): {x}")
    print(f"Signature (s): {s}")

    # Bob's part
    # Verify the signature using Alice's public key
    # Using the public key, Bob gets a new digest x': x' ≡ s^e mod n
    x_prime = square_multiply(s, e, n)

    # Bob checks whether x' == x is true
    is_valid_signature = (x == x_prime)

    print("\nBob's part:")
    print(f"Computed message (x'): {x_prime}")
    print(f"Signature valid: {is_valid_signature}")
