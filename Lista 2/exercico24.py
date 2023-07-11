#faça um programa que leia nome, nota 1 e nota 2 de um aluno. 
# em seguida calcelea média e informe se po alubo está aprovado, reprovado ou em prova final. 
# A média maior ou igual a 7 é aprovação menor que 3 a reprovação e demais casos o aluno está em prova final.
nome=input('Digite o nome do aluno:\n')
nota1=float(input('Digite a primeira nota:\n'))
nota2=float(input('Digite a segunda nota:\n'))
media=(nota1+nota2)/2
if (media>=7):
    print(f'A média do aluno {nome} é {media} portanto ele está aprovado.')
else:
    print(f'A média do aluno {nome} é {media} portanto ele está reprovado.')
