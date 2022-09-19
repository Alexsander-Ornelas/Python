'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou NNoturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso'''
print(" M-Matutino\n V-Vespertino\n N-Noturno")
turno = input("Qual o turno que você estuda?")
if turno == "M" or turno =="m":
    print("Bom dia!")
elif turno == "V" or turno =="v":
    print("Boa tarde!")
elif turno =="N" or turno =="n":
    print("Boa noite!")
else:
    print("Valor Inválido")