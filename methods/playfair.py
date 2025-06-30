import numpy as np
import string



def text_to_pairs(text):
    text = text.lower().replace(" ", "").replace("j", "i")
    pairs = []
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            pairs.append(text[i] + 'x')
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2
    if i < len(text):
        pairs.append(text[i] + 'x')
    return pairs


def playfair_enc(plain_text, key):
    key_final = ""
    for char in key:
        if char not in key_final:
            key_final += char

    matrix_list = [char for char in key_final]
    for char in string.ascii_lowercase:
        if char == 'j':
            continue
        if char not in matrix_list:
            matrix_list.append(char)

    matrix = np.array(matrix_list).reshape(5, 5)


    cipher = ""
    pairs = text_to_pairs(plain_text)
    for pair in pairs:
        pair_handled = False
        for row in range(5):
            row_data = matrix[row, :]
            if pair[0] in row_data and pair[1] in row_data:
                idx1 = list(row_data).index(pair[0])
                idx2 = list(row_data).index(pair[1])
                cipher += matrix[row, (idx1 + 1) % 5]
                cipher += matrix[row, (idx2 + 1) % 5]
                pair_handled = True
                break
        if pair_handled:
            continue
        for col in range(5):
            col_data = matrix[:, col]
            if pair[0] in col_data and pair[1] in col_data:
                idx1 = list(col_data).index(pair[0])
                idx2 = list(col_data).index(pair[1])
                cipher += matrix[(idx1 + 1) % 5, col]
                cipher += matrix[(idx2 + 1) % 5, col]
                pair_handled = True
                break
        if pair_handled:
            continue
        r1, c1 = np.where(matrix == pair[0])
        r2, c2 = np.where(matrix == pair[1])
        cipher += matrix[r1[0], c2[0]]
        cipher += matrix[r2[0], c1[0]]
    return cipher

def playfair_dec(cipher_text, key):
    key_final = ""
    for char in key:
        if char not in key_final:
            key_final += char

    matrix_list = [char for char in key_final]
    for char in string.ascii_lowercase:
        if char == 'j':
            continue
        if char not in matrix_list:
            matrix_list.append(char)

    matrix = np.array(matrix_list).reshape(5, 5)

    decrypted = ""
    cipher_pairs = text_to_pairs(cipher_text)
    for pair in cipher_pairs:
        pair_handled = False
        for row in range(5):
            row_data = matrix[row, :]
            if pair[0] in row_data and pair[1] in row_data:
                idx1 = list(row_data).index(pair[0])
                idx2 = list(row_data).index(pair[1])
                decrypted += matrix[row, (idx1 - 1) % 5]
                decrypted += matrix[row, (idx2 - 1) % 5]
                pair_handled = True
                break
        if pair_handled:
            continue
        for col in range(5):
            col_data = matrix[:, col]
            if pair[0] in col_data and pair[1] in col_data:
                idx1 = list(col_data).index(pair[0])
                idx2 = list(col_data).index(pair[1])
                decrypted += matrix[(idx1 - 1) % 5, col]
                decrypted += matrix[(idx2 - 1) % 5, col]
                pair_handled = True
                break
        if pair_handled:
            continue
        r1, c1 = np.where(matrix == pair[0])
        r2, c2 = np.where(matrix == pair[1])
        decrypted += matrix[r1[0], c2[0]]
        decrypted += matrix[r2[0], c1[0]]
    return decrypted


if __name__ == "__main__":
    cipher = playfair_enc("hello", "sup")
    playfair_dec("sh", "sup")
