#Faça um programa que peça para o usuário entrar com uma senha e diga se a senha está correta ou incorreta. 
# A senha é definida como uma constante pelo programador.
senha='123'
s=(input('Entre com uma senha:\n'))
if (s==senha):
    print('Senha correta!')
else:
    print('Senha incorreta!')
