n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    soma = 0
    impares_encontrados = 0 
    
    
    while impares_encontrados < y:
        if x % 2 != 0:
            soma += x
            impares_encontrados += 1
        x += 1    
    
    print(soma)