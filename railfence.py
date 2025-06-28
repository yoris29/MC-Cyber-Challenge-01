import numpy as np

key = 4312567
plain = "attack postponed to two am"
plain = plain.replace(" ", "")
key_list = [int(i) for i in str(key)]
sorted_key = [int(i) for i in str(key)]
sorted_key.sort()

remainder = len(plain) % len(key_list)
if(remainder > 0):
    nb_letters_to_add = len(key_list) - remainder

    for i in range(123 - nb_letters_to_add, 123):
        plain += chr(i)

def railfence_enc(key,plain):
    cipher = ""
    cols = len(key_list)
    rows = len(plain) // cols
    enc_rectangle = np.array([letter for letter in plain]).reshape(rows, cols)

    for number in sorted_key:
        col_index = key_list.index(number)
        cipher += "".join(list(enc_rectangle[:,col_index]))

    return cipher

def railfence_dec(key, cipher):
    key_list = [int(i) for i in str(key)]
    key_order = sorted([(val, idx) for idx, val in enumerate(key_list)])
    cols = len(key_list)
    rows = len(cipher) // cols

    dec_matrix = np.empty((rows, cols), dtype=str)

    start = 0
    for _, col_index in key_order:
        dec_matrix[:, col_index] = list(cipher[start:start+rows])
        start += rows

    plaintext = "".join(dec_matrix.flatten())
    return plaintext

print(railfence_dec(key, "ttovaptwtstuaodmcowxknoypeaz"))