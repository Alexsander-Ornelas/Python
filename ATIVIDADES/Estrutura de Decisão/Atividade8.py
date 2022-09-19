# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que adecisão é sempre pelo mais barato.

ProdutoA =input("Digite o primeiro produto:")
ValorA = int(input("Digite o valor:R$"))
ProdutoB =input("Digite o segundo produto:")
ValorB = int(input("Digite o valor:R$"))
ProdutoC =input("Digite o terceiro produto:")
ValorC = int(input("Digite o valor:R$"))

#ProdutoA=int
#ProdutoB = int
#ProdutoC= int
menorValor =ValorA
if  ValorB < menorValor:
    menorValor = ValorB
    
if  ValorC < menorValor:
    menorValor = ValorC
    
print("O produto recomendado a comprar é:",menorValor)
