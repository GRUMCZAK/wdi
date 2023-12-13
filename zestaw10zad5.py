import cmath # bedzie nam potrzebny pierwiastek z liczby zespolonej
def add (n, m, f):
    p = (n[0] + m[0], n[1] + m[1])
    if f == 1:
        print("Wynik to: ",p[0], " + ", p[1],"i", sep="")
    return p
    
def subtract (n, m):
    p = (n[0] - m[0], n[1] - m[1])
    return p

def multiply(m, n):
    p = (m[0] * n[0] - m[1] * n[1], m[0] * n[1] + m[1] * n[0])
    return p
    
def divide(m, n, f): # l. zespolone dzielimy mnozac licznik i mianownik wyrazenia przez sprzezenie mianownika
    p = ( (m[0] * n[0] + m[1] * n[1]) / (n[0]* n[0] + n[1] * n[1]) , (m[1] * n[0] - m[0] * n[1] ) / (n[0]* n[0] + n[1] * n[1]) )
    if f == 1: # jesli chcemy wypisac wynik operacji
        if(m[0] * n[1] + m[1] * n[0] > 0 ):
            print("Wynik to:",p[0], " + ", p[1],"i",sep="")
        else:
            print("Wynik to: ",p[0], " - ", abs(p[1]),"i", sep="")
    return p
    
def power(m, deg):
    if deg == 0:
        print(1)
        return 1;
    elif deg == 1:
        return m
    elif deg > 1:
        return( multiply(power(m, deg - 1), m) )

print("Podaj dwie liczby zespolone")

a = float(input())
b = float(input())
z1 = (a,b)

c = float(input())
d = float(input())
z2 = (c,d)

print("Wybierz typ operacji:")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnozenie")
print("4 - dzielenie") 
print("5 - potegowanie") # tylko potegi naturalne
print("6 - rozwiaz rownanie") # niestety udalo mi sie tylko ze wspolczynnikami rzeczywistymi, jednak wyniki moga wyjsc zespolone
print("7 - wypisanie obu liczb")
e = int(input())

if e == 1:
    add(z1,z2)
    
elif e == 2:
    print(subtract(z1,z2))
    
elif e == 3:
    print(multiply(z1,z2)[0], " + ", multiply(z1,z2)[1],"i")
    
elif e == 4:
    divide(z1,z2,1)
    
elif e == 5:
    print("Do jakiej potegi chcesz podniesc te liczbe?")
    deg = int(input())
    print("Wynik to: ", power(z1, deg)[0], " + ", power(z1, deg)[1], "i", sep="")
    print("Wynik to: ", power(z2, deg)[0], " + ", power(z2, deg)[1], "i", sep="")

elif e == 6:

    print("Podaj wspolczynniki zespolone (czyli pary liczb rzeczywistych) a, b, c rownania kwadratowego ax^2 + bx + c = 0")
    k = float(input())
    l = float(input())
    a2 = (k,l)
    
    k = float(input())
    l = float(input())
    b2 = (k,l)
    
    k = float(input())
    l = float(input())
    c2 = (k,l)
    # delta = b^2 - 4*a*c
    four = (float(4),float(0))
    delta = subtract( power(b2,2) , multiply(four, multiply(a2, c2)) )
    z = complex(delta[0], delta[1]) #zapisujemy delte jako liczbe zespolona aby wyciagnac z niej pierwiastek za pomoca funkcji sqrt dla liczb zespolonych
    b3 = (-b2[0], -b2[1]) #zmieniamy znak b2 na potrzeby dalszych obliczen, bo nie ma operacji b2 = -b2 poniewaz b2 to krotka
    z1 = cmath.sqrt(z)
    z2 = ( z1.real, z1.imag ) # czyli z2 to po prostu pierwiastek z delty zapisany w postaci krotki
    a3 = ( 2*a2[0], 2*a2[1] )
    rozw1 = divide( add(b3, z2, 0), a3, 0)
    rozw2 = divide( subtract(b3, z2), a3, 0)
    print("Rozwiazaniem rownania jest: ",rozw1[0], " + ", rozw1[1],"i", sep="")
    print("Rozwiazaniem rownania jest: ",rozw2[0], " + ", rozw2[1],"i", sep="")



    
elif e == 7:
    print("z1 = ", end="")
    if(z1[1] >= 0):
        print(z1[0], " + ",z1[1]," i", sep="")
    else:
        print(z1[0], " - ",abs(z1[1])," i", sep="")
    
    print("z2 = ", end="")
    if(z2[1] >= 0):
       print(z2[0], " + ",z2[1]," i", sep="")
    else:
        print(z2[0], " - ",abs(z2[1])," i", sep="")
    
    
'''Przyklady:
z^2 + 1 = 0

z^2 + 6z + 10 = 0

z = -3 + i lub z = -3 - i

Sprzezenia liczb:
(2+2i) * (2 - 2i) = 8

(2+2i)^3 = -16 + 16i
3^3 = 27

(3+3i) / (15 + 15i) = 0.2

'''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    