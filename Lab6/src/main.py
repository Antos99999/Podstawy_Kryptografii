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
    if n <= t:
        print("T musi byc mniejsze lub rowne n")
        return
    a = []
    primary_p = sympy.randprime(n,100)
    sekret = s = random.randint(0,primary_p)

    print(f"Sekret: {sekret}")

    for i in range(t-1):
        a.append(random.randint(0,100000000))

    udzialy = []
    suma = 0
    for i in range(n):
        x=i
        for j in range(1, t):
            suma += a[j - 1] * (x ** j)
        s_i = (s + suma) % primary_p
        udzialy.append([i,s_i])

    print(f"Udzialy: {udzialy}")

    #Odtworzenie sekretu
    suma = 0
    lagrange = 1
    t = len(udzialy)

    for i in range(t):
        xi, si = udzialy[i]
        licznik = 1
        mianownik = 1
        for j in range(t):
            if i != j:
                xj, _ = udzialy[j]
                licznik = (licznik * (0 - xj))
                mianownik = (mianownik * (xi - xj))
        lagrange = ((licznik/mianownik) % primary_p) * lagrange
        suma = (suma + si * lagrange) % primary_p

    print(f"Sekret po odtworzeniu: {int(suma)}")

if __name__ == '__main__':
    n = int(input("Podaj n: "))
    t = int(input("Podaj t: "))
    trywailny(n,t)
    n = int(input("Podaj n: "))
    t = int(input("Podaj t: "))
    shamir(n,t)