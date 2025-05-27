n = int(input())

for _ in range(n):
    x = int(input())
    totdiv = 0
    
    for i in range(1, x+1):
        if x % i == 0:
            totdiv += 1
    
    if totdiv == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')