cod, quant = map(int, input().split())
cod -= 1
preços = [4, 4.5, 5, 2, 1.5]

print(f'Total: R$ {preços[cod] * quant:.2f}')
