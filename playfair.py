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

matrix = np.array(matrix).reshape(5, 5)

plain = plain.replace(" ", "")
plain_pairs = []  # he lx lo
i = 0

while (i < len(plain) - 1):
    if plain[i] == plain[i+1]:
       plain_pairs.append(plain[i] + 'x') 
       i += 1
    else:
        plain_pairs.append(plain[i] + plain[i+1])
        i += 2
# In case the last letter is alone
if(len(plain_pairs) * 2 <len(plain)):
    plain_pairs.append(plain[- 1]+'x')

# encyption
cipher = ""
for pair in plain_pairs:
    pair_handled = False
    # letters in same row
    for row in range(0,5):
        current_row = matrix[row, :]
        if(pair[0] in current_row and pair[1] in current_row):
            first_index = list(current_row).index(pair[0])
            second_index = list(current_row).index(pair[1])
            cipher += matrix[row, (first_index+1) % 5]
            cipher += matrix[row, (second_index+1) % 5]
            pair_handled = True
            break

    if pair_handled:
        continue

    # letters in the same column
    for col in range(0,5):
        current_col = matrix[:, col]
        if(pair[0] in current_col and pair[1] in current_col):
            first_index = list(current_col).index(pair[0])
            second_index = list(current_col).index(pair[1])
            cipher += matrix[(first_index+1) % 5, col]
            cipher += matrix[(second_index+1) % 5, col]
            pair_handled = True
            break

    if pair_handled:
        continue

    
print(matrix)

## letters in same col
