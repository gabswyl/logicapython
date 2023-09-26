# 15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input('Quanto você ganha por hora: '))
qntdHoras = float(input('Insira sua quantidade de horas trabalhadas: '))

salario_bruto = hora * qntdHoras
inss, sindicato, IR = 0.08 * salario_bruto, 0.05 * salario_bruto, 0.11 * salario_bruto
salarioLiquido = salario_bruto - inss - sindicato - IR

print('Salário Bruto:', salario_bruto)
print('INSS:', inss)
print('Sindicato:', sindicato)
print('IR:', IR)
print('Salário Liquido:', salarioLiquido)