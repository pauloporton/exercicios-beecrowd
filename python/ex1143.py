n = int(input())
current = 1

for num in range(1, n+1):
    print(f'{current} {current**2} {current**3}')
    current += 1
