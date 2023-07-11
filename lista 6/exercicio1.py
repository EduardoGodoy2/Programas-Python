#1.Escreva um programa que lê uma frase, uma palavra antiga e uma palavra nova. 
# O programa deve imprimir a frase com as ocorrências da palavra antiga substituídas pela palavra nova.
# Exemplo:
# –Frase: “Quem parte e reparte fica com a maior parte”
# –Palavra antiga: “parte”
# –Palavra nova: “parcela”
# –Saída: “Quem parcela e reparte fica com a maior parcela”
frase=input('Entre com uma frase:').split()
antiga=input('Entre com uma palavra:')
nova=input('Entre com uma nova palavra:')
for i in (frase):
    if (i==antiga):
        i=nova
    print(i, end = ' ')