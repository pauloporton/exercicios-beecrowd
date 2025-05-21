x = int(input())
while True:
    z = int(input())
    if z > x:
        break
  
soma = 0   
count = 0
n = x  
while soma <= z:
    soma += n
    count += 1
    n += 1

print(count) 
