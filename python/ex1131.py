cont = 0
inter = 0
gremio = 0
empate = 0
while True:
    cont += 1
    x, y = map(int, input().split())
    if x > y:
        inter += 1
    elif y > x:
        gremio += 1
    else:
        empate += 1
        
    print('Novo grenal (1-sim 2-nao)')
    ans = int(input())
    if ans == 2:
        break

print(f'{cont} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
if gremio == inter:
    print('Nao houve vencedor')
else:
    if inter > gremio:
        print('Inter venceu mais')
    else:
        print('Gremio venceu mais')
        