soma = 0
count = 0
while True:
    idade = int(input())
    if idade >= 0:
        soma += idade
        count += 1
    else:
        break
    
media = soma / count    
print(f'{media:.2f}')  
