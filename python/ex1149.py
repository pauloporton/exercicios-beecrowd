valores = list(map(int, input().split()))
a = valores[0]
n = 0

for num in valores[1:]:
    if num > 0:
        n = num
        break

soma = 0
for i in range(n):
    soma += a + i
print(soma)   