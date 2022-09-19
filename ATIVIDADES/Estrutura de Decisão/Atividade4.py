#Faça um Programa que verifique se uma letra digitada é vogal ou consoante
#vogal =str("A"),("E"),("I"),("O"),("U"),("a"),("e"),("i"),("o"),("u")
Letra =str(input("Digite a letra desejada:"))
def vogal(Letra):
    if Letra == ("A")or Letra == ("E")or Letra == ("I")or Letra == ("O")or Letra == ("a")or Letra == ("e")or Letra == ("i")or Letra == ("o")or Letra == ("u"):
        print("O que você digitou é uma vogal")
    else:
        print("O que você digitou não é uma vogal")
vogal(Letra)