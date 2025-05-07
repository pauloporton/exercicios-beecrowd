for num in range(100):
    n = int(input())
    if num == 0:
        maior = n
        posmaior = num
    else:
        if n > maior:
            maior = n
            posmaior = num

print(maior)
print(posmaior + 1)
