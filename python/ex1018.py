N = int(input())
print(N)

notas = [100, 50, 20, 10, 5, 2, 1]

for valor in notas:
    quantidade = N // valor
    N -= quantidade * valor
    print(f'{quantidade} nota(s) de R$ {valor},00') 
    