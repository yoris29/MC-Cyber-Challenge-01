import math

def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def rsa_enc(m, e,p, q):
    if not (est_premier(p) and est_premier(q)):
        return "p et q doivent être premiers et distincts"
    if p == q:
        return "p et q doivent être distincts"
    
    n = p * q

    return pow(m, e, n)

def rsa_dec(c, e, p, q):
    if not (est_premier(p) and est_premier(q)):
        return "p et q doivent être premiers et distincts"
    if p == q:
        return "p et q doivent être distincts"
    
    
    n = p * q
    phi = (p - 1) * (q - 1)


    d = modinv(e, phi)
    m = pow(c, d, n)

    return chr(m)

if __name__ == "__main__":     
    c= 2790
    p = 61
    q = 53
    e = 17
    m = 65
    
    # print(rsa_enc(m, e,p, q))
    # print(rsa_dec(c, p, q, e))
