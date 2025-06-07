n = []

t = int(input())
    
n = 0    
for i in range(1000):
    
    if n < t:
        valor = n
        n += 1
    else:
        valor = 0
        n = 1
        
    print(f'N[{i}] = {valor}') 
    