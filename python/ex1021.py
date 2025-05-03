N = float(input())
total_centavos = int(round(N * 100))  

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print('NOTAS:')
for valor in notas:
    quant = total_centavos // valor
    total_centavos -= quant * valor
    print(f'{quant} nota(s) de R$ {valor/100:.2f}')
    
print('MOEDAS:')
for valor in moedas:
    quant = total_centavos // valor
    total_centavos -= quant * valor
    print(f'{quant} moeda(s) de R$ {valor/100:.2f}')
    