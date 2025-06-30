from methods.ceasar import ceasar_dec, ceasar_enc 
from methods.vigenere import vigenere_dec, vigenere_enc
from methods.hashing import md5, sha1, sha256
from methods.playfair import playfair_dec, playfair_enc
from methods.railfence import railfence_dec, railfence_enc
from methods.rc4 import rc4
from methods.rsa import rsa_dec, rsa_enc
# from methods.test_aes import encrypt, decrypt
# from methods.test_des import encrypt, decrypt

if __name__ == "__main__":
    # print(ceasar_enc("hello", 3))
    # print(ceasar_dec("khoor", 3))
    # print(vigenere_enc("hello", "key"))
    # print(vigenere_dec("rijvs", "key"))
    # print(md5("hello"))
    # print(sha1("hello"))
    # print(sha256("hello"))
    # print(playfair_enc("sup", "playfair"))
    # print(playfair_dec("nxyu", "playfair"))
    # print(railfence_enc(4312567, "hello"))
    # print(railfence_dec(4312567, "llehoyz"))
    # cipher = rc4("hey", "key")
    # print(rc4("hey", "key"))
    # print(rc4(cipher, "key"))
    print(rsa_enc(65, 17, 53, 61))
    print(rsa_enc(2790, 17, 53, 61))