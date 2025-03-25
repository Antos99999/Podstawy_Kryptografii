'''
Lab 2
RSA
'''

import random
import math
from sympy import isprime

def find_primes():
    primes = [p for p in range(1001, 10000, 2) if isprime(p)]
    return primes

def find_relatively_prime(n):
    while True:
        candidate = random.randint(2, n-1)  # Losujemy liczbę z przedziału [2, n-1]
        if math.gcd(candidate, n) == 1:
            return candidate

def main():
    prime_list = find_primes()

    p = random.choice(prime_list)
    q = random.choice(prime_list)

    n=p*q
    phi = (p-1)*(q-1)

    e = find_relatively_prime(phi)

    d = pow(e, -1, phi)

    #e i n -> publiczne
    #d i n -> prywatne

    message = "To jest tekst jawny i on będzie zaszyfrowany (RSA)"
    zaszyfrowany_message = []
    odszyfrowany_message = ""

    for char in message:
        zaszyfrowany_message.append(pow(ord(char),e,n))

    print(f"zaszyfrowana wiadomość: {zaszyfrowany_message}")

    for char in zaszyfrowany_message:
        odszyfrowany_message += chr(pow(char,d,n))

    print(f"Odszyfrowana wiadomość: {odszyfrowany_message}")


if __name__ == '__main__':
    main()