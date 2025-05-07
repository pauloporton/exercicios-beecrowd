n = int(input())

for num in range(2, 10001, n):
    if num % n == 2:
        print(num)
        