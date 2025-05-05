# Lendo a primeira linha (hora inicial)
linha1 = input().split()
dia_inicio = int(linha1[1])

# Lendo a segunda linha (hora inicial)
linha2 = input().strip().split(' : ')
hora_inicio, minuto_inicio, segundo_inicio = map(int, linha2)

# Lendo a terceira linha (dia final)
linha3 = input().split()
dia_fim = int(linha3[1])

# Lendo a quarta linha (hora final)
linha4 = input().strip().split(' : ')
hora_fim, minuto_fim, segundo_fim = map(int, linha4)

dia = dia_fim - dia_inicio
hora = hora_fim - hora_inicio
minuto = minuto_fim - minuto_inicio
segundo = segundo_fim - segundo_inicio

# Ajustando os valores negativos
if segundo < 0:
    segundo += 60
    minuto -= 1

if minuto < 0:
    minuto += 60
    hora -= 1

if hora < 0:
    hora += 24
    dia -= 1

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')