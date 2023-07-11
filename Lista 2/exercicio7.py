c=int(input('Entre com um caractere alfanumérico:\n'))
a=str(c)
ca=a.lower()
if (c<=9) and (c>=0):
    print('Esse alfanumérico é um número.')
elif (ca=='a') or (ca=='e') or (ca=='i') or (ca=='o') or (ca=='u'):
    print('Esse alfanumérico é uma vogal.')
else:
    print('é uma consoante')
