print("(Ustaw saldo)")
saldo=int(input())
print("(Ustaw PIN)")
pin=input()
while True:
    print("Podaj PIN")
    if input()!=pin:
        print("Podano niepoprawny PIN")
    else:
        print("Co chcesz zrobić w kolejnym kroku? \n 1 - wplata \n 2 - wyplata \n 3 - sprawdz saldo \n 4 - wyjdz")
        x=int(input())
        if x==1:
            print("Podaj wplacana kwote:")
            dodaj=int(input())
            saldo=saldo+dodaj
            print("Twoje saldo wynosi teraz: ",end="")
            print(saldo)
        elif x==2:
            print("Podaj wyplacana kwote:")
            zadanie_kwoty=int(input())
            if zadanie_kwoty>saldo:
                print("Nie masz tylu pieniedzy")
            else:
                print("Wyplacono: ", end="") 
                saldo=saldo-zadanie_kwoty
                print(zadanie_kwoty)
                print("Twoje saldo wynosi teraz:" ,end="")
                print(saldo)
        elif x==3:
            print("Twoje saldo wynosi: ",end="") 
            print(saldo)
        elif x==4:
            print("Dziekujemy za skorzystanie z naszego bankomatu/wplatomatu")
            break
        else:
            print("Nieznana komenda")

