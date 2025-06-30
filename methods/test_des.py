from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(data: bytes) -> bytes:
    """PKCS7 padding for block size 8."""
    pad_len = 8 - len(data) % 8
    return data + bytes([pad_len] * pad_len)

def unpad(data: bytes) -> bytes:
    """Remove PKCS7 padding."""
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 8:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

def encrypt(key: bytes, plaintext: bytes) -> tuple:
    """
    Encrypt plaintext using DES in CBC mode.
    Returns (iv, ciphertext).
    """
    cipher = DES.new(key, DES.MODE_CBC)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return cipher.iv, ciphertext

def decrypt(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    """
    Decrypt ciphertext using DES in CBC mode.
    Returns original plaintext after unpadding.
    """
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext)

# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(8)  # DES key is 8 bytes (64 bits)
    data = b"Secret DES message!"

    print("Original:", data)

    iv, ciphertext = encrypt(key, data)
    print("Encrypted (hex):", ciphertext.hex())

    decrypted = decrypt(key, iv, ciphertext)
    print("Decrypted:", decrypted)
