from Crypto.Cipher import AES
from secrets import token_bytes

def encrypt(key: bytes, plaintext: bytes) -> tuple:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce, ciphertext, tag

def decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

if __name__ == "__main__":
    key = token_bytes(16)  # AES-128 key (16 bytes)
    data = b"Hello, this is a secret message!"

    print("Original:", data)

    nonce, ciphertext, tag = encrypt(key, data)
    print("Encrypted:", ciphertext.hex())

    decrypted = decrypt(key, nonce, ciphertext, tag)
    print("Decrypted:", decrypted)
