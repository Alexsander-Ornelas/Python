#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -Masculino, Sexo Inválido.
print("F para feminino | M para Masculino")
sexo = input("digite o seu Sexo:")
if sexo == "F" or sexo == "f":
    print("Sexo Feminino")
elif sexo =="M" or sexo =="m":
    print("Sexo Masculino")
else:
    print("Sexo inválido")