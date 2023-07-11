#Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. 
# Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. 
# Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). 
# Após a conclusão da soma, o novo estado da memória passa a ser 8.
# Estado da memória: 0
# Opções:
# (1) Somar
# (2) Subtrair
# (3) Multiplicar
# (4) Dividir
# (5) Limpar memória
# (6) Sair do programa
# Qual opção você deseja?
def soma(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
em=0
opcao=0
while (opcao != 6):
    opcao=int(input(f"""Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
O valor da memória é {em}
Qual opção você deseja?:"""))
    if (opcao == 1):
        b=int(input(f'Entre com um valor para somar com {em}:'))
        print(soma(em,b))
        em=soma(em,b)
    if (opcao == 2):
        b=int(input(f'Entre com um valor para subtrair com {em}:'))
        print(subtrair(em,b))
        em=subtrair(em,b)
    if (opcao == 3):
        b=int(input(f'Entre com um valor para multiplicar com {em}'))
        print(multiplicar(em,b))
        em=multiplicar(em,b)
    if (opcao == 4):
        b=int(input(f'Entre com um valor para dividir com {em}'))
        print(dividir(em,b))
        em=dividir(em,b)
    if (opcao == 5):
        em = 0
    if (opcao == 6):
        print('Programa Encerrado')
    else:
        print('Opção Invalida!')