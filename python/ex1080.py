for i in range(100):
    num = int(input())
    
    if i == 0:
        maior = num
    else:
        if num > maior:
            maior = num
            pos = i + 1
            
print(maior)
print(pos)
