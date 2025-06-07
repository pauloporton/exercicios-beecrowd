fibonacci = []

atual = 0
anterior = 1
proximo = 1
for _ in range(61):
    fibonacci.append(atual)
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    

t = int(input())

for i in range(t):
    pos = int(input())
    print(f'Fib({pos}) = {fibonacci[pos]}')
    