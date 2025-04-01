'''
Lab 2
DH
'''

import random
from sympy import isprime, primerange

def find_primes():
    primes = [p for p in range(1001, 10000, 2) if isprime(p)]
    return primes


def find_primitive_root(n):
    factors = list(primerange(2, n - 1))
    for g in range(2, n):
        is_primitive_root = True
        for factor in factors:
            if pow(g, (n - 1) // factor, n) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            return g
    return None

def A(g,n):
    x = random.randint(1, 9999)
    X = pow(g, x, n)
    return x, X

def A_k(x,Y,n):
    k = pow(Y, x, n)
    return k

def B(g,n):
    y = random.randint(1, 9999)
    Y = pow(g, y, n)
    return y, Y

def B_k(x,Y,n):
    k = pow(Y, x, n)
    return k

def main():
    prime_list = find_primes()
    n = random.choice(prime_list)
    g = find_primitive_root(n)

    Y = 0
    X = 0

    print(f"Liczba n: {n}")
    print(f"liczba g: {g}")

    x, X = A(g,n)
    y, Y = B(g,n)

    kA = A_k(x,Y,n)
    kB = B_k(y,X,n)

    print(f"Klucz k: {kA} oraz {kB}")




if __name__ == '__main__':
    main()