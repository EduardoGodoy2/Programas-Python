#Faça um programa que leia um número binário de 4 dígitos e diga qual é o seu decimal correspondente
n=int(input('Entre com um número binário de 4 digitos:\n')) #1001
dig1=((n//1000)*(2**3))
dig2=(((n%1000)//100)*(2**2))
dig3=(((n%100)//10)*(2**1))
dig4=((n%10)*(2**0))
print(f'{dig1+dig2+dig3+dig4}')
