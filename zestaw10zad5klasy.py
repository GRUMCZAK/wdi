import cmath

class complexus:
    def __init__(self, realis, imaginaria):
        self.realis = realis
        self.imaginaria = imaginaria*1j
    
    def __add__(self, z):
        return complexus(self.realis + z.realis, self.imaginaria + z.imaginaria)
    
    def __sub__(self, z):
        return complexus(self.realis - z.realis, self.imaginaria - z.imaginaria)
    
    def __mul__(self, z):
        return complexus(self.realis*z.realis + self.imaginaria * z.imaginaria, self.realis * (z.imaginaria/1j) + (self.imaginaria/1j) * z.realis)
    #zmienilem znak dla czesci rzeczywistej z uwagi na to , ze self.imaginaria  i z.imaginaria zawieraja j, ktore po przemnozeniu sie dadza -1

    def __truediv__(self, z):
        return complexus( (self.realis*z.realis - self.imaginaria*z.imaginaria) / (pow(z.realis,2) - pow(z.imaginaria,2)), (-self.realis * (z.imaginaria/1j) + (self.imaginaria/1j) * z.realis)/(pow(z.realis,2) - pow(z.imaginaria,2)))
    
    def __pow__(self, n):
        t = self
        for i in range(1,n):
            self = self * t
        return self
    

    

print("Podaj dwie liczby zespolone")

k = float(input())
l = float(input())
a = complexus(k,l)

m = float(input())
n = float(input())
b = complexus(m,n)

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
    c = a + b
    print(c.realis, '+', c.imaginaria)
    
elif e == 2:
    h = a - b
    print(h.realis, "+", h.imaginaria)
    
elif e == 3:
    d = a * b
    print(d.realis, "+", d.imaginaria)
    
elif e == 4:
    e = a / b
    print(e.realis, "+", e.imaginaria) 
    
elif e == 5:
    print("Do jakiej potegi chcesz podniesc te liczbe?")
    deg = int(input())
    f = pow(a,deg)
    g = pow(b,deg)
    print(f.realis, "+", f.imaginaria)
    print(g.realis, "+", g.imaginaria)

elif e == 6:

    print("Podaj wspolczynniki zespolone (czyli pary liczb rzeczywistych) a, b, c rownania kwadratowego ax^2 + bx + c = 0")
    p = float(input())
    o = float(input())
    a2 = complexus(p, o)
    
    p = float(input())
    o = float(input())
    b2 = complexus(p, o)
    
    p = float(input())
    o = float(input())
    c2 = complexus(p, o)

    four = complexus(4,0)
    delta = b2*b2 - (four*(a2 * c2))
    z = complex(delta.realis, delta.imaginaria) # z to delta, ale jako liczba zespolona, zeby moc wyciagnac pierwiastek z uzyciem biblioteki cmath
    z = cmath.sqrt(z)
    sqrtdelta = complexus(z.real, z.imag)
    b3 = complexus(-b2.realis, -b2.imaginaria/1j) # b3 to -b2
    a3 = complexus(2*a2.realis, 2*a2.imaginaria/1j)
    rozw1 = ((b3 - sqrtdelta) /  a3)
    rozw2 = ((b3 + sqrtdelta) /  a3)
    print(rozw1.realis,"+", rozw1.imaginaria/1j)
    print(rozw2.realis,"+", rozw2.imaginaria/1j)

   
elif e == 7:
    print(a.realis, '+', a.imaginaria)
    print(b.realis, '+', b.imaginaria)
    
    
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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    