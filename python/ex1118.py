while True:
    total = 0
    cont = 0
    while cont < 2:
        nota = float(input())
        
        if  0 <= nota <= 10:
            total += nota
            cont += 1
        else:
            print('nota invalida')
    
    print(f'media = {total/2:.2f}')
    
    while True:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())
        if x == 1 or x == 2:
            break
    if x == 2:
        break
    