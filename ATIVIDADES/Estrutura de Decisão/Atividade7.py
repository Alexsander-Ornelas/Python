#Faça um Programa que leia três números e mostre o maior e o menor deles
ValorA =int(input("Digite o Primeiro número:"))
ValorB =int(input("Digite o Segundo número:"))
ValorC =int(input("Digite o Terceiro número:"))
maior=ValorA
if ValorB > maior:
    maior = ValorB
    ValorC>maior
    maior = ValorC
menor = ValorA
if ValorB < menor:
    menor = ValorB
    ValorC<menor
    menor = ValorC
print("O maior valor é:",maior)
print("O menor valor é:",menor)