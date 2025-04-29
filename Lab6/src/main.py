import random
import sympy

def trywailny(n,t):
    if n != t:
        print("N i T musza być równe")
        return
    k = 100
    sekret = 50
    udzialy = []
    for i in range(n-1):
        udzialy.append(random.randint(0, k-1))

    #Podział sekretu
    ostatni = (sekret-sum(udzialy)) % k
    udzialy.append(ostatni)

    print(f"Sekret: {sekret}")

    print(f"Udzialy: {udzialy}")

    #Odtworzenie sekretu
    sekret_po_odtworzeniu = sum(udzialy) % k
    print(f"Sekret po odtworzeniu: {sekret_po_odtworzeniu}")

def shamir(n,t):
    if t > n:
        print("T musi byc mniejsze lub rowne n")
        return
    a = []
    s = random.randint(0, 100)
    min_p=max(s,n)
    primary_p = sympy.randprime(min_p,min_p*2)
    print(f"Primary p: {primary_p}")

    print(f"Sekret: {s}")

    for i in range(t-1):
        a.append(random.randint(0, primary_p-1))

    a = [s] + a

    udzialy = []
    for i in range(1, n + 1):
        si = 0
        x = i
        for j in range(t):
            si = (si + a[j] * ((x ** j) % primary_p))
        udzialy.append((i, si))

    print(f"Udzialy: {udzialy}")

    udzialy_do_odtworzenia = random.sample(udzialy,t)
    odtworzenie_sekretu(udzialy_do_odtworzenia,primary_p)


def odtworzenie_sekretu(udzialy,p):
    print(f"Udzialy do odtworzenia: {udzialy}")
    suma = 0
    for i in range(t):
        xi, si = udzialy[i]
        lagrange = 1
        for j in range(t):
            if i != j:
                xj, _ = udzialy[j]
                licznik = (-xj) % p
                mianownik = (xi - xj) % p
                odwrotnosc = pow(mianownik, -1, p)
                lagrange = (lagrange * odwrotnosc * licznik) % p
        suma = (suma + si * lagrange) % p

    print(f"Sekret po odtworzeniu: {int(suma)}")

if __name__ == '__main__':
    n = int(input("Podaj n: "))
    t = int(input("Podaj t: "))
    trywailny(n,t)
    n = int(input("Podaj n: "))
    t = int(input("Podaj t: "))
    shamir(n,t)