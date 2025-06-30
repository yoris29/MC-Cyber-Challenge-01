import hashlib

def md5(input_string):
    encoded = input_string.encode()
    md5_hash = hashlib.md5(encoded).hexdigest()
    return md5_hash

def sha1(input_string):
    encoded = input_string.encode()
    sha1_hash = hashlib.sha1(encoded).hexdigest()
    return sha1_hash

def sha256(input_string):
    encoded = input_string.encode()
    sha256_hash = hashlib.sha256(encoded).hexdigest()
    return sha256_hash


if __name__ == "__main__":
    text = input("Enter a string to hash: ")
    
    print(sha256(text))