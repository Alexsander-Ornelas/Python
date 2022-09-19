# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram paradesenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280, 00 (incluindo): aumento de 20%
#salários entre R$ 280, 00 e R$ 700, 00: aumento de 15 % salários entre R$ 700, 00 e R$ 1500, 00: aumento de 10 % salários de R$ 1500, 00 em diante: aumento de 5 % Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste
#o percentual de aumento aplicado
#o valor do aumento
#o novo salário, após o aumento.
salario = int(input("Digite o seu salário:"))
bonificacao1 = salario * 0.20
bonificacao2 = salario * 0.15
bonificacao3 = salario * 0.10
bonificacao4 = salario * 0.05

print("Antes do Reajuste: ", salario)

if salario <= 280:
    print("Aumento de: 20%\nValor: ", bonificacao1, "\nNovo Salário: ", salario*1.20)
elif salario > 200 and salario <= 700:
    print("Aumento de: 15%\nValor: ", bonificacao2, "\nNovo Salário: ", salario*1.15)
elif salario > 700 and salario <= 1500:
    print("Aumento de: 10%\nValor: ", bonificacao3, "\nNovo Salário: ", salario*1.10)
else:
    print("Aumento de: 5%\nValor: ", bonificacao4,  "\nNovo Salário: ", salario*1.05)
    