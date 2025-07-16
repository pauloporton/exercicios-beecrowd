n = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    teste = input().split()
    quantia = int(teste[0])
    tipo = teste[1]
    
    total += quantia    
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    else:
        sapos += quantia
        
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhos * 100 / total:.2f} %')
print(f'Percentual de ratos: {ratos * 100 / total:.2f} %')
print(f'Percentual de sapos: {sapos * 100 / total:.2f} %')
