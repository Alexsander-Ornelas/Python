#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada poraluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
#A mensagem "Reprovado", se a média for menor do que sete
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
media= 7
NotaTotal = 10
NotaA = int(input("Digite a primeira Nota:"))
NotaB= int(input("Digite a segunda Nota:"))
mediaTotal =(NotaA/2 + NotaB /2)
if mediaTotal== NotaTotal:
    print("Aprovado com Distinção")
elif mediaTotal >= media:
    print ("Aprovado")
else:
    print("Reprovado")