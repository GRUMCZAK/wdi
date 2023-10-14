a=int(input())
print(a)
for x in range(1,a):
    print(" ",end="")
for x in range(0,a+1):
    for i in range(1,a-x+1):
        print(" ", end="")
    for g in range(1,2+2*(x-1)):
        if x==1:
            print("X", end="")
        else:
            if g%2==0:
                print("o", end="")
            else:
                print("*", end="")
    print("\n",end="")
    x=x-1
for x in range (1,a):
    print(" ",end="")
print("U")