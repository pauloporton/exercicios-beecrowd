num = int(input())

lista = [
    (61, 'Brasilia'),
    (71, 'Salvador'),
    (11,'Sao Paulo'),
    (21, 'Rio de Janeiro'),
    (32, 'Juiz de Fora'),
    (19, 'Campinas'),
    (27, 'Vitoria'),
    (31, 'Belo Horizonte')
    ]

cadastrado = False
for ddd, cidade in lista:
    if ddd == num:
        print(cidade)
        cadastrado = True
        break
        
if not cadastrado:
    print('DDD nao cadastrado')
    