from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import random
import base64

# Generate RSA keys
def generate_RSA(bits=1024):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)
    return private_key, public_key

# Encrypt a message using the public key
def encrypt_RSA(public_key_file, message):
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()

# Decrypt a message using the private key
def decrypt_RSA(private_key_file, ciphertext):
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return plaintext.decode()

# Sign data using the private key
def sign_data(private_key_file, data):
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    h = SHA256.new(data.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return base64.b64encode(signature).decode()

# Verify the signature of data using the public key
def verify_sign(public_key_file, sign, data):
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    h = SHA256.new(data.encode())
    try:
        pkcs1_15.new(public_key).verify(h, base64.b64decode(sign))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    # Generate RSA keys
    generate_RSA()

    # Read the content of mydata.txt
    with open('mydata.txt', 'r') as f:
        message = f.read()

    # Encrypt mydata.txt using the public key
    ciphertext = encrypt_RSA('public_key.pem', message)
    with open('mydata_encrypted.txt', 'w') as f:
        f.write(ciphertext)

    # Decrypt mydata.txt using the private key
    decrypted_message = decrypt_RSA('private_key.pem', ciphertext)
    with open('mydata_decrypted.txt', 'w') as f:
        f.write(decrypted_message)

    # Sign the text mydata.txt using the private key
    signature = sign_data('private_key.pem', message)
    with open('mydata_signature.txt', 'w') as f:
        f.write(signature)

    # Verify the signature
    is_valid = verify_sign('public_key.pem', signature, message)
    with open('signature_verification.txt', 'w') as f:
        f.write(f'Signature valid: {is_valid}')

    # Redo the protocol attack with the new RSA implementation
    with open('public_key.pem', 'r') as f:
        public_key = RSA.import_key(f.read())

    n = public_key.n
    e = public_key.e

    # Alice's part
    s = random.getrandbits(1024)
    cipher = PKCS1_OAEP.new(public_key)
    try:
        x = cipher.encrypt(s.to_bytes(128, 'big'))  # Properly padded encrypted message
    except ValueError:
        print("Message is too large for encryption, as expected due to padding.")
        x = None

    print("Alice's part:")
    if x:
        print(f"Message (x): {base64.b64encode(x).decode()}")
    else:
        print(f"Failed to encrypt s due to padding restrictions.")
    print(f"Signature (s): {s}")

    # Bob's part
    if x:
        try:
            x_prime = cipher.decrypt(x)  # Attempt to decrypt, which should fail or result in incorrect data
            is_valid_signature = (s.to_bytes(128, 'big') == x_prime)
        except ValueError:
            x_prime = None
            is_valid_signature = False
    else:
        x_prime = None
        is_valid_signature = False

    print("\nBob's part:")
    if x_prime:
        print(f"Computed message (x'): {base64.b64encode(x_prime).decode()}")
    else:
        print(f"Failed to decrypt x due to padding restrictions.")
    print(f"Signature valid: {is_valid_signature}")

    # Report the result of the attack
    print(f'Attack success: {is_valid_signature}')
