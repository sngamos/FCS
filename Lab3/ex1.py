import hashlib

plaintext = "Pancakes"
result = hashlib.md5(plaintext.encode())
print(result.hexdigest())
