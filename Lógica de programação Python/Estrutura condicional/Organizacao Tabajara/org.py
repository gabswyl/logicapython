# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.


# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento."

salario = float(input("Insira o seu salário: "))

if salario <= 280:
  valor = salario + (salario * 20/100)
  novoSalario = valor
  print("O salario antes do reajuste: ", salario)
  print("A porcentagem do salário foi 20%")
  print("Seu novo salario: ", novoSalario)

elif salario > 280 and salario <= 700:
 valor = salario + (salario * 15/100)
 novoSalario = valor
 print("O salario antes do reajuste: ", salario)
 print("A porcentagem do salário foi 20%")
 print("Seu novo salario: ", novoSalario)

elif salario > 700 and salario <= 1500:
 valor = salario + (salario * 10/100)
 novoSalario = valor
 print("O salario antes do reajuste: ", salario)
 print("A porcentagem do salário foi 20%")
 print("Seu novo salario: ", novoSalario)

else:
 valor = salario + (salario * 5/100)
 novoSalario = valor
 print("O salario antes do reajuste: ", salario)
 print("A porcentagem do salário foi 20%")
 print("Seu novo salario: ", novoSalario)


