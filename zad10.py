import random 
while True:
    print("Podaj dwie liczby:")
    #a=float(input())
    a=int(input())
    b=int(input())
    #b=float(input())
    print("Podaj typ operacji:")
    t=input()
    if t=="+":
        print(a+b)
    elif t=="-":
        print(a-b)
    elif t=="*":
        print(a*b)
    elif t=="/":
        print(a/b)
    elif t=="#":
        print(a**(1/b))
    elif t=="^":
        print(a**b)
    elif t=="x":
        print(random.randint(a,b))
    print("Czy chcesz wprowadzić nowe dane? T/N")
    ans=input()
    if ans=="N":
        break
    if ans=="T":
        continue
    else:
        print("Nieznana komenda")
        break
    