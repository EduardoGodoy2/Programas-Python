 #Faça um programa que leia 3 números diferentes e os imprima em ordem crescente e decrescente. 
 # Se houver números iguais exibir mensagem de erro.
n=int(input('Entre com um número:\n'))
n2=int(input('Entre com um número:\n'))
n3=int(input('Entre com um número:\n'))
if (n==n2) or (n==n3) or (n3==n2):
    print('Error!')
elif (n<n2) and (n2<n3):
    print(f'{n}{n2}{n3} crescente')
    print(f'{n3}{n2}{n} decrescente')
elif (n>n2) and (n2>n3):
    print(f'{n3}{n2}{n} crescente')
    print(f'{n}{n2}{n3} decrescente')
elif (n<n2) and (n>n3):
    print(f'{n3}{n}{n2} crescente')
    print(f'{n2}{n}{n3} decrescente')
elif (n<n3) and (n2>n3):
    print(f'{n}{n3}{n2} crescente')
    print(f'{n2}{n3}{n} decrescente')
elif (n>n3) and (n3>n2):
    print(f'{n2}{n3}{n} crescente')
    print(f'{n}{n3}{n2} decrescente')
else:
    print(f'{n3}{n}{n2} crescente')
    print(f'{n2}{n}{n3} decrescente')