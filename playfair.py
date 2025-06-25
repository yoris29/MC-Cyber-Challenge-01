import numpy as np
import string

key = "playfair"
plain = "hello"

# To remove duplicates in the key
final_keyword = ""

for letter in key:
    if letter not in final_keyword:
        final_keyword += letter

# Matrix (key + alphabet letters)
matrix = [letter for letter in final_keyword]
alphabet = string.ascii_lowercase

for letter in alphabet:
    if letter == "j":
        continue
    elif letter not in matrix:
        matrix.append(letter)

matrix = np.matrix(matrix).reshape(5, 5)

plain = plain.replace(" ", "")
plain_pairs = []  # he lx lo
i = 0

while (i < len(plain) - 1):
    if plain[i] == plain[i+1]:
       plain_pairs.append([plain[i], 'x']) 
       i += 1
    else:
        plain_pairs.append([plain[i], plain[i+1]])
        i += 1

print(matrix)