#Страница 99, Задача "А"
def draw_line(N):
    line = "-" * N
    return line
print(draw_line(int(input("N="))))
#Страница 99, Задача "В"
def stolb(n):
    s = str(n)
    for i in s:
        print(i)
print(stolb(int(input("n="))))
#Cтраница 100, Задача "С"
def roman(numm):
    _1_ = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    _10_ = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    _100_ = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    _1000_ = ["", "M", "MM", "MMM", "MMMM"]
    f = _1000_[numm // 1000]
    s = _100_[numm // 100 % 10]
    t = _10_[numm // 10 % 10]
    fo = _1_[numm % 10]
    return f+s+t+fo
print(roman(int(input('numm='))))
#Страница 106, Задача "А"
def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        funkc = a + b
    print(funkc)
a=int(input())
b=int(input())
print(nod(a,b))
#Страница 106, Задача "В"
def summ(a):
    t=0
    while a != 0:
        t += a%10
        a//=10
    return t
print(summ(int(input())))
#Страница 107, Задача "С"
def perevorot(n1):
    n2 = 0
    while n1 > 0:
        digit = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + digit
    return n2
print(perevorot(int(input())))
#Страница 109, Задача "А"
def sort(a,b,c):
    if c < b:
        c,b = b,c
    if b < a:
        a,b = b,a
    return a,b,c
a = int(input())
b = int(input())
c = int(input())
print(sort(a,b,c))
#Cтраница 109, Задача "В"
def sokr(n, d):
    def nod(n, d):
        while n != d:
            if n > d:
                n -= d
            else:
                d -= n
        return n
    nod = nod(n, d)
    n //= nod
    d //= nod
    return f"{n}/{d}"
n=int(input())
d=int(input())
print(sokr(n,d))
#Cтраница 110, Задача "С"
def gcd(a, b):
    t = max(a,b)
    for i in range(1, t + 1):
        if ((a % i == 0) and (b % i == 0)):
            n = i
    return f"NOD{a, b}={n}\nNOK{a, b}={a * b // n}"
a= int(input())
b= int(input())
print(gcd(a, b))
#Cтраница 117, Задача "A":
def absolutenumber(numm):
    t=1
    for i in range(2, numm):
        if numm%i==0:
            t+=i
        else:
            continue
    if t == numm:
        return f"Число {numm} совершенно"
    else:
        return f"Число {numm} не совершенно"
print(absolutenumber(int(input())))
#Страница 118, Задача "В"
def prime(num1, num2):
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            return False
    return True
print(prime(28, 15))





