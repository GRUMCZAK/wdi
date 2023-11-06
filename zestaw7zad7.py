n = int(input())
T = [[0 for _ in range(n)] for _ in range(n)]
for a in range(0,n):
    for g in range(0,n):
        T[a][g]=int(input())

print(T)

wszedzie_zera = int(1)

for wiersz in range(n):
    zero_wiersz=int(0)
    for kol in range(n):
        if T[wiersz][kol]==0:
            zero_wiersz=1
    if zero_wiersz==0:
        wszedzie_zera=0
        break
    
for kol in range(n):
    zero_kol=int(0)
    for wiersz in range(n):
        if T[wiersz][kol]==0:
            zero_kol=1
    if zero_kol==0:
        wszedzie_zera=0
        break
    
if wszedzie_zera==0:
    print(False)
elif wszedzie_zera==1:
    print(True)