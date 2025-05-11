i = 0.0

while i <= 2:
    for j in range(1, 4):
        respostaJ = i + j
        
        if i.is_integer():
            print(f"I={int(i)} J={int(respostaJ)}")
        else:
            print(f"I={i} J={respostaJ}")
            
    i *= 10
    i += 2
    i /= 10       
