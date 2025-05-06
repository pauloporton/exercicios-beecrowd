x = int(input())
y = int(input())

if x > y:
    a = x
    b = y
else:
    a = y
    b = x
    
somaimpar = 0    
for num in range(b+1, a):
    if num % 2 != 0:
        somaimpar += num

print(somaimpar)        
        