# Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
# –Nota acima de 6  “Aprovado”
# –Nota entre 4 e 6  “Verificação Suplementar”
# –Nota abaixo de 4  “Reprovado”
def status(n):
    if (n>=6):
        return 'Aprovado'
    if (n<6) and (n>=4):
        return 'Verificação Suplementar'
    else:
        return 'Reprovado'

#Programa Principal
n=int(input('Digite sua nota:'))
print(status(n))