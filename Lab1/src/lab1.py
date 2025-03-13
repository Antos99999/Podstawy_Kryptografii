'''
Lab 1
BBS (Blum-Blum-Shub) - Implementacja generatora ciągów losowych oraz wybranych testów lsowości
Testy standardu FIPS 140-2
'''

import math
import random
import sympy
from sympy import isprime

def find_primes():
    primes = [p for p in range(1001, 10000, 2) if isprime(p) and p % 4 == 3]
    return primes


def relatively_prime_integers(n, limit):
    if n <= 0 or limit <= 0:
        return []

    relatively_prime_numbers = []
    for i in range(1, limit + 1):
        if math.gcd(n, i) == 1:
            relatively_prime_numbers.append(i)

    return relatively_prime_numbers

def main():
    prime_list = find_primes()
    #print(prime_list)

    x_table = [20000]
    bits = ""

    p = random.choice(prime_list)
    #p = 4 * kp + 3

    q = random.choice(prime_list)
    #q = 4 * kq + 3

    #print(p,q)

    N = p*q

    #print(N)

    relatively_prime = relatively_prime_integers(N,limit=9999)

    x = random.choice(relatively_prime)
    #print(x)

    x_table[0] = math.pow(x,2) % N
    #print(x0)

    for i in range(20000):
        x_table.append(math.pow(x_table[i],2) % N)
        #print(x_table[i+1])

    for i in x_table[1:]:
        bits = bits + str(int(i)&1)

    #print(bits)

    return bits



if __name__ == '__main__':
    main()