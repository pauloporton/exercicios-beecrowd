n = int(input())

for _ in range(n):
    soma = 0
    x = int(input())
    
    for i in range(1, x):
        if x % i == 0:
            soma += i
            
    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')