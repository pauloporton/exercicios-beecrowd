salario = float(input())

faixas = [
    (400, 15),
    (800, 12),
    (1200, 10),
    (2000, 7),
    (float('inf'), 4)
]

percentual = 4  
for limite, perc in faixas:
    if salario <= limite:
        percentual = perc
        break

novo_salario = salario * (1 + percentual / 100)
    
print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {novo_salario - salario:.2f}')
print(f'Em percentual: {percentual} %')
