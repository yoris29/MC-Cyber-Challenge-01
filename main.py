from methods.ceasar import ceasar_dec, ceasar_enc 
from methods.vigenere import vigenere_dec, vigenere_enc
from methods.hashing import md5, sha1, sha256
from methods.playfair import playfair_dec, playfair_enc
from methods.railfence import railfence_dec, railfence_enc
from methods.rc4 import rc4
from methods.rsa import rsa_dec, rsa_enc
from methods.test_aes import aes_enc, aes_dec
from methods.test_des import des_enc, des_dec
from secrets import token_bytes

def menu():
    print("Select a category:")
    print("1. Classical Ciphers")
    print("2. Stream & Block Ciphers")
    print("3. Asymmetric Encryption")
    print("4. Hashing")
    return input("Choice: ")

def classical_menu():
    print("\n-- Classical Ciphers --")
    print("1. Caesar")
    print("2. Vigenère")
    print("3. Playfair")
    print("4. Rail Fence")
    return input("Choice: ")

def stream_block_menu():
    print("\n-- Stream & Block Ciphers --")
    print("1. RC4")
    print("2. AES")
    print("3. DES")
    return input("Choice: ")

def asymmetric_menu():
    print("\n-- Asymmetric Encryption --")
    print("1. RSA")
    print("2. Diffie-Hellman")
    return input("Choice: ")

def hashing_menu():
    print("\n-- Hashing --")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    return input("Choice: ")

def enc_dec_menu():
    return input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

if __name__ == "__main__":
    choice = menu()

    if choice == "1":
        algo = classical_menu()
        action = enc_dec_menu()
        text = input("Enter text: ")

        if algo == "1":  # Caesar
            shift = int(input("Enter shift value: "))
            if action == "e":
                print("Encrypted:", ceasar_enc(text, shift))
            else:
                print("Decrypted:", ceasar_dec(text, shift))

        elif algo == "2":  # Vigenère
            key = input("Enter key: ")
            if action == "e":
                print("Encrypted:", vigenere_enc(text, key))
            else:
                print("Decrypted:", vigenere_dec(text, key))

        elif algo == "3":  # Playfair
            key = input("Enter key: ")
            if action == "e":
                print("Encrypted:", playfair_enc(text, key))
            else:
                print("Decrypted:", playfair_dec(text, key))

        elif algo == "4":  # Rail Fence
            pattern = int(input("Enter numeric pattern: "))
            if action == "e":
                print("Encrypted:", railfence_enc(pattern, text))
            else:
                print("Decrypted:", railfence_dec(pattern, text))

    elif choice == "2":
        algo = stream_block_menu()
        action = enc_dec_menu()

        if algo == "1":  # RC4 (same for enc and dec)
            text = input("Enter text: ")
            key = input("Enter key: ")
            result = rc4(text, key)
            print("Output:", result)

        elif algo == "2":  # AES
            if action == "e":
                key = token_bytes(16)
                text = input("Enter text: ")
                nonce, ciphertext, tag = aes_enc(key, text.encode())
                print("Key:", key.hex())
                print("Nonce:", nonce.hex())
                print("Ciphertext:", ciphertext.hex())
                print("Tag:", tag.hex())
            else:
                key = bytes.fromhex(input("Enter key (hex): "))
                nonce = bytes.fromhex(input("Enter nonce (hex): "))
                ciphertext = bytes.fromhex(input("Enter ciphertext (hex): "))
                tag = bytes.fromhex(input("Enter tag (hex): "))
                print("Decrypted:", aes_dec(key, nonce, ciphertext, tag).decode())

        elif algo == "3":  # DES
            if action == "e":
                key = token_bytes(8)
                text = input("Enter text: ")
                nonce, ciphertext, tag = des_enc(key, text.encode())
                print("Key:", key.hex())
                print("Nonce:", nonce.hex())
                print("Ciphertext:", ciphertext.hex())
                print("Tag:", tag.hex())
            else:
                key = bytes.fromhex(input("Enter key (hex): "))
                nonce = bytes.fromhex(input("Enter nonce (hex): "))
                ciphertext = bytes.fromhex(input("Enter ciphertext (hex): "))
                tag = bytes.fromhex(input("Enter tag (hex): "))
                print("Decrypted:", des_dec(key, nonce, ciphertext, tag).decode())

    elif choice == "3":
        algo = asymmetric_menu()
        action = enc_dec_menu()

        if algo == "1":  # RSA
            e = int(input("Enter public exponent e: "))
            p = int(input("Enter prime p: "))
            q = int(input("Enter prime q: "))
            if action == "e":
                msg = int(input("Enter integer message to encrypt: "))
                print("Encrypted:", rsa_enc(msg, e, p, q))
            else:
                cipher = int(input("Enter cipher integer to decrypt: "))
                print("Decrypted:", rsa_dec(cipher, e, p, q))

        elif algo == "2":
            print("Diffie-Hellman has been implemented in the .\methods\diffie_hellman_socket folder where you have to run the server and the client at the same time.")

    elif choice == "4":
        algo = hashing_menu()
        text = input("Enter text to hash: ")
        if algo == "1":
            print("MD5:", md5(text))
        elif algo == "2":
            print("SHA-1:", sha1(text))
        elif algo == "3":
            print("SHA-256:", sha256(text))

    else:
        print("Invalid selection.")