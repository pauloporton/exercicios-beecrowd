n = int(input())

fat = 1
for num in range(n, 0, -1):
    fat *= num

print(fat)    
