""" Implemente um sistema de login que verifique se o usuário inseriu uma senha 
correta. Se a senha estiver incorreta três vezes, levante uma exceção 
personalizada de "Tentativas Excessivas". """

senha_correta = 'Daniel123!'

tentativa = 0

while tentativa < 3:
    try:
        senha = str(input('Digite a senha: '))

        if senha_correta == senha:
            print('Acesso liberado!')
            break
        else:
            print('Senha incorreta.')
            tentativa += 1
        
        if tentativa == 3:
            raise Exception('Tentativas Exessivas!!!')
    except Exception as erro:
        print(erro)