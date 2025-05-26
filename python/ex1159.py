while True:
    somapares = 0
    x = int(input())
    if x == 0:
        break
    else:
        if x % 2 != 0:
            x += 1
            
        for num in range(5):
                somapares += x
                x += 2
                
        print(somapares) 
        