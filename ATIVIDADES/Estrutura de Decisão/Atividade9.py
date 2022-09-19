#Faça um Programa que leia três números e mostre-os em ordem decrescente
ValorA =int(input("Digite o Primeiro número:"))
ValorB =int(input("Digite o Segundo número:"))
ValorC =int(input("Digite o Terceiro número:"))

Valores = [(ValorA),(ValorB),(ValorC)]
Valores.sort(reverse= True)
print(Valores)