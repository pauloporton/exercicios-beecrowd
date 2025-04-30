a, b, c = map(int, input().split())
maiorab = (a + b + abs(a - b)) / 2
maiortot = (maiorab + c + abs(maiorab - c)) / 2
print(f'{int(maiortot)} eh o maior')
