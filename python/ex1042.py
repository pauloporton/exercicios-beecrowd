a, b, c = map(int, input().split())
lista = [a, b, c]
copia = lista[:]
copia.sort()

for num in copia:
    print(num)
    
print()

for n in lista:
    print(n)
    