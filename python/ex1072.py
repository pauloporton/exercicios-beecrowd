n = int(input())

totin = 0
totout = 0
for c in range(n):
    num = int(input())
    if 10 <= num <= 20:
        totin += 1
    else:
        totout += 1

print(f'{totin} in')
print(f'{totout} out')
