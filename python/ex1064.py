a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a, b, c, d, e, f]

totpos = 0
somapos = 0
for c in lista:
    if c > 0:
        totpos += 1
        somapos += c
        
mediapos = somapos/totpos
print(f'{totpos} valores positivos')
print(f'{mediapos:.1f}')
