a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a, b, c, d, e, f] 

totpositivo = 0
for num in lista:
    if num > 0:
        totpositivo += 1

print(f'{totpositivo} valores positivos')        
        