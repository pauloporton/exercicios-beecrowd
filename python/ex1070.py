x = int(input())

if x % 2 == 0:
    x += 1
else:
    x = x

for num in range(6):
    print(x)
    x += 2
