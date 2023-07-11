#Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. 
# Por exemplo, “Iracema” é um anagrama para “America”. 
# Escreva um programa que decida se uma stringé um anagrama de outra string, ignorando os espaços em branco. 
# O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, 
# ou seja, “a” = “A”. Obs.: utilize a função sorted() 
# que transforma uma stringem uma lista de caracteres em ordem crescente.
palavra1=input('Entre com uma palavra:').strip()
palavra2=input('Entre com uma segunda palavra:').strip()
p1=palavra1.lower()
p2=palavra2.lower()
p1=sorted(p1)
p2=sorted(p2)
if (p1==p2):
    print('é um anagrama')
else:
    print('não é um anagrama')