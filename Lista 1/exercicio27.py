#Faça um programa que leia um total de segundos e transforme para hora, minuto e segundo
segundo=int(input('digite os segundos'))
hora=segundo//3600
minutos=(segundo%3600)//60
segundos=(segundo%3600)%60
print(f'{hora} horas, {minutos} minutos e {segundos} segundos  ')