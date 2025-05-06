a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a, b, c, d, e]

totpar = 0
totimpar = 0
totpos = 0
totneg = 0
for c in lista:
    if c % 2 == 0:
        totpar += 1
    else:
        totimpar += 1
    if c > 0:
        totpos += 1
    elif c < 0:
        totneg += 1
        
print(f'{totpar} valor(es) par(es)')        
print(f'{totimpar} valor(es) impar(es)')   
print(f'{totpos} valor(es) positivo(s)')   
print(f'{totneg} valor(es) negativo(s)')
