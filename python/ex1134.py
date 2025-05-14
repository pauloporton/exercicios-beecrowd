cont1 = 0
cont2 = 0
cont3 = 0
while True:
    num = int(input())
    if 1 <= num <= 4:
        if num == 1:
            cont1 += 1
        elif num == 2:
            cont2 += 1
        elif num == 3:
            cont3 += 1
        else:
            break
    else:
        continue

print('MUITO OBRIGADO')
print(f'Alcool: {cont1}')
print(f'Gasolina: {cont2}')
print(f'Diesel: {cont3}')
