x = float(input())
n = []

for i in range(100):
    n.append(x)
    print(f'N[{i}] = {x:.4f}')
    x = x/2
    