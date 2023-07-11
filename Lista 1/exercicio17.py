#Faça um programa que leia o ano atual e quantos anos uma pessoa fez ou fará nesse ano, em seguida, calcule o ano em que a pessoa nasceu
ano=int(input('Digite seu ano atual:\n'))
idade=int(input('Digite quantos anos você fez ou fará esse ano:\n'))
nasceu=ano-idade
print(f'Você nasceu em {nasceu}')
