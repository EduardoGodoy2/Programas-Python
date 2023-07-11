#Faça um programa que leia hora, minuto e segundo e transforme tudo para segundos
hora=int(input('digite a hora:\n'))
minuto=int(input('digite os minutos:\n'))
segundo=int(input('digite os segundos:\n'))
valor=(hora*3600)+(minuto*60)+(segundo)
print(f'Seu horário em segundos é {valor}')