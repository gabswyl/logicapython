# # Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
# trabalhadas no mês.

# Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.


hora = float(input("Insira o valor da hora: "))
qntsHoras = float(input("Insira o quantidade de horas trabalhadas no mês: "))

salario_bruto = hora * qntsHoras


if salario_bruto <= 900:
   print("Salário bruto: ", salario_bruto)
elif salario_bruto <= 1500:
  calc = salario_bruto - (salario_bruto * 0.5)
  print("Salário bruto com desconto de 5%¨: ", calc)
elif salario_bruto <= 2500:
    calc = salario_bruto - (salario_bruto * 0.10)
    print("Salário bruto com desconto de 10%: ", calc)
else:
    calc = salario_bruto - (salario_bruto * 0.20)
    print("Salário bruto com desconto de 20%: ", calc)
