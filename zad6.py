a=float(input())
b=float(input())

if (a<0 and b <0):

    print("Obie liczby są ujemne ")

else: #mamy gwarancje, ze conajmniej jedna z liczb jest dodatnia
    if a<0:
        a=-a
    if b<0:
        b=-b
    suma=float(a+b)
    print("Suma wynosi: %d" %suma)
    roznica=float(a-b)
    print("Roznica wynosi: %d" %roznica)
    iloczyn=float(a*b)
    if iloczyn==10:
        print("Yay!")
    print("Iloczyn wynosi: %d" %iloczyn)
    if b!=0:
        iloraz=float(round((a/b),3))
        print("Iloraz wynosi: %d" %iloraz)
    else:
        print("Nie dziel przez zero")
    akwadrat=float(a*a)
    print("A do kwadratu wynosi: %d" %akwadrat)
    bkwadrat=float(b*b)
    print("B do kwadratu wynosi: %d" %bkwadrat)
"""
komentarz
multiline:)
"""