#Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, 
# se uma é igual à outra quando lida de traz para frente.
# •Exemplo: amor e roma.
frase1=input('frase1:').lower()
frase2=input('frase2:').lower()
if (frase1==frase2[::-1]):
    print('são palíndromas')
else:
    print('não são palíndromas')