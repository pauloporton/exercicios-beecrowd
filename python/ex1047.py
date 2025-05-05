hora_inicio, min_inicio, hora_fim, min_fim = map(int, input().split())

inicio = hora_inicio * 60 + min_inicio
fim = hora_fim * 60 + min_fim

if fim > inicio:
    duracao = fim - inicio
else:
    duracao = (24 * 60 - inicio) + fim

horas = duracao // 60
minutos = duracao % 60
    
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
