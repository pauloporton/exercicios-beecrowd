n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())
    mediap = (a * 2 + b * 3 + c * 5) / 10
    print(f'{mediap:.1f}')
    