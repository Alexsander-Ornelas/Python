#Obs.: Utilize a IDE PyCharm para fazer os programas de hoje
#1. Função recebe CPF
#Faça um programa em Python para receber o número de CPF informado pelo usuário e depois imprimí-lo.
#Observações:
    #use a função input para receber dados digitados pelo usuário
    #o recebimento do CPF deve ser feito em uma função
    #a impressão do CPF recebido deve ser feita no programa principal

def cpfValido():
    cpf =str(input("Qual o seu CPF:"))
    if len(cpf) ==14 :
        print("O seu CPF é:",cpf)
    elif len(cpf) == 11:
        cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        print("O seu CPF é:",cpf)
    else:
        print("O CPF é Inválido")
cpfValido()
