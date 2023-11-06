f = float(0) #dwa poczatkowe wyrazy ciagu
f1 = float(1)
i = 1
while 1==1: # nieskonczona petla
    print("n=",end="")#numerowwanie kolejnych ilorazow
    print(i,end=" ")
    i+=1
    print(float(f/f1)) # gdy zamienimy f i f1, to granica zmieni sie o 1
    a=f1
    f1=f1+f
    f=a
