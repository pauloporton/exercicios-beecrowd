t = int(input())

for num in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    anos = 0
    
    while pa <= pb and anos <= 100:
        pa += int((g1 / 100) * pa)
        pb += int((g2 / 100) * pb)
        anos += 1
    
    if anos > 100:
        print('Mais de 1 seculo.')
    else:    
        print(f'{anos} anos.')
        