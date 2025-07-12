O = input()
matriz = []

for _ in range(12):
    linha = []
    for _ in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
        
soma = 0
contagem = 0

for i in range(1, 11):
    for j in range(11, 11 - i, - 1):
        if j > i:
            soma += matriz[i][j]
            contagem += 1
        
if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / contagem:.1f}')