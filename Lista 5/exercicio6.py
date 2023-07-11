# O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. 
# Faça o programa que lê o valor de N e M e informa o número de combinações possíveis
# –Número de combinações é igual a N!/(M! * (N-M)!)
# –Use funções para evitar repetição de código
def vcombinacoes(n,m):
    fatn=1
    fatm=1
    fatnm=1
    for i in range(1,n+1):
        fatn*=i
    for i in range(1,m+1):
        fatm*=i
    for i in range(1,(n-m)+1):
        fatnm *=i
    return fatn/(fatm * fatnm)

#programa principal
n=int(input('Entrei com da primeira turma:'))
m=int(input('Entrei com da segunda turma:'))
print(vcombinacoes(n,m))