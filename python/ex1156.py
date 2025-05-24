s = 1
n = 1
d = 1

while n <= 39:
    n += 2
    d *= 2
    s += (n / d)

print(f'{s:.2f}') 
