#.Faça um programa que leia uma data de nascimento válida no formato dd/mm/aaaa
# e imprima a data com o mês escrito por extenso.
# Exemplo:
# Data = 20/02/1995
# Resultado gerado pelo programa:
# 20 de fevereiro de 1995
dia,mes,ano=input('Entre com uma data de nascimento:').split('/')
if (mes=='01'):
    print(f'Você nasceu dia {dia} de janeiro de {ano}')
if (mes=='02'):
    print(f'Você nasceu dia {dia} de fevereiro de {ano}')
if (mes=='03'):
    print(f'Você nasceu dia {dia} de março de {ano}')
if (mes=='04'):
    print(f'Você nasceu dia {dia} de abril de {ano}')
if (mes=='05'):
    print(f'Você nasceu dia {dia} de maio de {ano}')
if (mes=='06'):
    print(f'Você nasceu dia {dia} de junho de {ano}')
if (mes=='07'):
    print(f'Você nasceu dia {dia} de julho de {ano}')
if (mes=='08'):
    print(f'Você nasceu dia {dia} de agosto de {ano}')
if (mes=='09'):
    print(f'Você nasceu dia {dia} de setembro de {ano}')
if (mes=='10'):
    print(f'Você nasceu dia {dia} de outubro de {ano}')
if (mes=='11'):
    print(f'Você nasceu dia {dia} de novembro de {ano}')
if (mes=='12'):
    print(f'Você nasceu dia {dia} de dezembro de {ano}')