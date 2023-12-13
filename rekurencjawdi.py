def maxel(l, number, curr):
    if int(number) == len(l) - 1:
        return max(curr, l[number] )
    else:
        curr = max(curr, l[number] )
        return max(curr, maxel(l, number + 1, curr))

def sum(l, position):
    if int(position) == len(l)-1:
        return int(l[position])
    else:
        return (l[position] + sum(l, position + 1))

l = []
n = int(input("Podaj wymiar listy:"))

for x in range (0,n):
    a = int(input())
    l.append(a)
    
print("Najwiekszy element na liscie to:", maxel(l, 0, l[0] ))
print("Suma wszystkich elementow z listy wynosi:", sum(l,0))