start, end = map(int, input().split())

if start == end:
    tempo = 24
elif start < end:
    tempo = end - start
else:
    tempo = (24 - start) + end
    
print(f'O JOGO DUROU {tempo} HORA(S)')    
