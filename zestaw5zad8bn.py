from decimal import Decimal, getcontext
n = int(input())
getcontext().prec = n
e = 1
i = 1
l = []
l.append(e)
dzielnik = 1
while i < 1000:
    dzielnik *= i
    e = e + Decimal(1/dzielnik)
    #print(e)
    i=i+1
    l.append(e)
 # robimy liste roznic w przyblizeniach
for g in range(0,len(l)-1):
    l[g] = l[len(l)-1]-l[g]

print("10 pierwszych wyrazow")
for h in range(0,10):
    print(l[h])
print(" ")
print("10 srodkowych wyrazow")
if (len(l) % 2) == 0:
    for p in range(int((len(l)/2))-5,(int(len(l)/2))+5):
        print(l[p])

print(" ")
print("10 ostatnich wyrazow")
for k in range(0,10):
    print(l[len(l)-1-k])
