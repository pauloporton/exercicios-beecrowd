a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse=True)
a, b, c = lista

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:    
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')
        
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
        