'''
Lab 1
BBS (Blum-Blum-Shub) - Implementacja generatora ciągów losowych oraz wybranych testów lsowości
Testy standardu FIPS 140-2
'''

import math
import random

def relatively_prime_integers(n, limit):
    if n <= 0 or limit <= 0:
        return []

    relatively_prime_numbers = []
    for i in range(1, limit + 1):
        if math.gcd(n, i) == 1:
            relatively_prime_numbers.append(i)

    return relatively_prime_numbers

def main():
    x_table = [20000]
    bits = ""

    kp = 100379
    p = 4*kp + 3

    kq = 102023
    q = 4*kq + 3

    N = p*q

    #print(N)

    relatively_prime = relatively_prime_integers(N,limit=10000000)

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