a=int(input())
b=int(input())
if b<a:
    c=a
    a=b
    b=c
if b-a>20:
    sr=(a+b)/2
    i=sr-3
    while(i<sr+4):
        if i==sr:
            i=i+1
        else:
            print(i)
            i=i+1
else:
    for x in range(a,b+1):
        print(x)

