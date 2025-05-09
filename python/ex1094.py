n = int(input())

totcobaias = 0
totc = 0
totr = 0
tots = 0
for _ in range(n):
    teste = input().split()
    num = int(teste[0])
    tipo = teste[1].upper()
    
    totcobaias += num
    
    if tipo == 'C':
        totc += num
    elif tipo == 'R':
        totr += num
    elif tipo == 'S':  
        tots += num
        
print(f'Total: {totcobaias} cobaias')
print(f'Total de coelhos: {totc}')
print(f'Total de ratos: {totr}')
print(f'Total de sapos: {tots}')
print(f'Percentual de coelhos: {(totc/totcobaias)*100:.2f} %')
print(f'Percentual de ratos: {(totr/totcobaias)*100:.2f} %')
print(f'Percentual de sapos: {(tots/totcobaias)*100:.2f} %')
