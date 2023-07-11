#Faça um programa que entre com um número de 3 dígitos (em apenas uma variável) e o 
# escreva na ordem inversa em que foi digitado. Ex.: se o usuário digitar 379 terá que aparecer na tela 973.
n=int(input('Entre com um número de 3 digitos:\n'))
uni=n%10
dez=(n%100)//10
cen=n//100
print(f'Seu número invertido é {uni}{dez}{cen}')