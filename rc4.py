def rc4(data, key):
    S = list(range(256))
    j = 0
    out = []

    # Key Scheduling Algorithm (KSA)
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(chr(ord(char) ^ K))

    return ''.join(out)

plaintext = "attack at dawn"
key = "secret"

cipher = rc4(plaintext, key)
print(rc4(plaintext, key))
print(rc4(cipher, key))
