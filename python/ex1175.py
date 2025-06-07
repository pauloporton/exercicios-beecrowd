n = []

for _ in range(20):
    valor = int(input())
    n.append(valor)

for i in range(10):
    n[i], n[19-i] = n[19-i], n[i]
    
for i in range(20):
    print(f'N[{i}] = {n[i]}')