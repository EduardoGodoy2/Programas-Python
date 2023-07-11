#Faça um programa que leia a sigla do estado em que uma pessoa nasceu e imprima uma das mensagens abaixo:
# •carioca 
# •paulista
# •mineiro
# •baiano  
# •outros casos
n=input('Entre com a sigla do seu estado:\n') 
a=n.lower()
if (a=='rj'):
    print(f'Carioca.')
elif (a=='sp'):
    print(f'Paulista.')
elif (a=='mg'):
    print('Mineiro.')
elif (a=='ba'):
    print('Baiano.')
else:
    print('Outros casos.')