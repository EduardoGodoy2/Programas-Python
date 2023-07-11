#Um comerciante comprou um produto que quer vende-lo com um lucro de 45% 
# se o valor da compra for menor que 20BRL caso contrário o lucro será de 30%.
#  Entre com o valor do produto e imprima o valor de venda.
valorp=int(input('Digite o valor do produto:\n'))
lucro45=valorp*0.45
lucro30=valorp*0.30
if (valorp<=20):
    print(f'O valor da venda será {lucro45+valorp}.')
else:
    print(f'O valor da venda será {lucro30+valorp}')