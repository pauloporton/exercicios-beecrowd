O = input().strip()

matriz = []

for _ in range(12):
    linha = []
    for _ in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
soma = 0
contagem = 0
n = 12

for i in range(12):
    n -= 1
    for j in range(n):
        soma += matriz[i][j]
        contagem += 1
        
if 0 == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/contagem:.1f}')