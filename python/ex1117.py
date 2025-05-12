total = 0
cont = 0

while cont < 2:
    nota = float(input())
    
    if 0 <= nota <= 10:
        total += nota
        cont += 1
    else:
        print("nota invalida")

print(f'media = {total/2:.2f}')    
