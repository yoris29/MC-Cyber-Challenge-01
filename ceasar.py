import string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

def ceasar_enc(plain, key):
    result = ""
    for char in plain:
        if char.isalpha(): 
            if char.isupper():
                result += upper_letters[(upper_letters.index(char) + key) % 26]
            else:
                result += lower_letters[(lower_letters.index(char) + key) % 26]
        else:
            result += char   
    return result
        
def ceasar_dec(cipher, key):
    result = ""
    for char in cipher:
        if char.isalpha(): 
            if char.isupper():
                result += upper_letters[(upper_letters.index(char) - key) % 26]
            else:
                result += lower_letters[(lower_letters.index(char) - key) % 26]
        else:
            result += char   
    return result


text = "Hello"
cipher = "Khoor"
key = 3

print(ceasar_enc(cipher, key))
print(ceasar_dec(cipher, key))
