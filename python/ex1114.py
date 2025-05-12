senha_correta = 2002

while True:
    tentativa = int(input())
    if tentativa != senha_correta:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break
    