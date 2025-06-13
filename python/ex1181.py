L = int(input())
T = input().upper().strip()

matriz = []

for _ in range(12):
    linha = []
    for i in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

linha_escolhida = matriz[L]

soma = 0
for n in linha_escolhida:
    soma += n
    
if T == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')
    