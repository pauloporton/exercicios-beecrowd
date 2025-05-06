a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a, b, c, d, e]

totpar = 0
for c in lista:
    if c % 2 == 0:
        totpar += 1
print(f'{totpar} valores pares')   
