n = int(input())

x = list(map(int, input().split()))

menor = x[0]
for n in range(len(x)):
    if x[n] < menor:
        menor = x[n]
        pos = n
        
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}') 
