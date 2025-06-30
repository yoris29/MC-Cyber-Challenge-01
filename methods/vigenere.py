# vig ene re
# key key ke
# v+k i+e g+y...

import string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

def vigenere_enc(plain, key):
    result = ""
    pos = 0
    for i in plain:
        if i.isalpha(): 
            if i.isupper():
                result += upper_letters[(upper_letters.index(i) + lower_letters.index(key[pos % len(key)])) % 26]
                pos += 1
            elif i.islower():
                result += lower_letters[(lower_letters.index(i) + lower_letters.index(key[pos % len(key)])) % 26]
                pos += 1
        else:
            result += i 
    return result

def vigenere_dec(cipher, key):
    result = ""
    pos = 0
    for i in cipher:
        if i.isalpha(): 
            if i.isupper():
                result += upper_letters[(upper_letters.index(i) - lower_letters.index(key[pos % len(key)])) % 26]
                pos += 1
            elif i.islower():
                result += lower_letters[(lower_letters.index(i) - lower_letters.index(key[pos % len(key)])) % 26]
                pos += 1
        else:
            result += i 
    return result

if __name__ == "__main__":
    plain = "sUp MaN"
    cipher = "Rijvs"
    key = "key"
    
    print(vigenere_enc(plain, key))
    print(vigenere_dec(cipher, key))
