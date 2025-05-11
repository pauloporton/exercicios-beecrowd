n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    if x > y:
        a = y
        b = x
    else:
        a = x
        b = y
    
    somaimpar = 0
    for num in range(a + 1, b):
        if num % 2 != 0:
            somaimpar += num
    print(somaimpar) 
    