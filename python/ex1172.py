x = []

for i in range(10):
    x.append(int(input()))
    if x[i] <= 0:
        x[i] = 1
    print(f'X[{i}] = {x[i]}')
    
    