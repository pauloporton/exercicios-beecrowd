C = int(input())
T = input().strip()

matriz = []

for _ in range(12):
    linha = []
    for i in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
coluna_escolhida = []
for linha in matriz:
    coluna_escolhida.append(linha[C])

soma = 0
for n in coluna_escolhida:
    soma += n
    
if T == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')
    