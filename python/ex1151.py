n = int(input())

anterior = 0
atual = 0
proximo = 1
for num in range(n):
    if num == n - 1:
        print(atual)
    else:    
        print(atual, end=' ')
    anterior = atual
    atual = proximo
    proximo = anterior + atual