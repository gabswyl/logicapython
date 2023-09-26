# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

dia = int(input("Insira dia: "))
mes = int(input("Insira mes: "))
ano = int(input("Insira ano: "))

if mes >= 1 and mes <= 12:
  if (dia >= 1 and dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)):
    print("A Data {}/{}/{} é valida".format(dia, mes, ano))
  elif (dia >= 1 and dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)):
    print("A Data {}/{}/{} é valida".format(dia, mes, ano))
  elif (dia >= 1 and dia <= 28 and mes == 2):
    print("A Data {}/{}/{} é valida".format(dia, mes, ano))
  else:
   print("A Data {}/{}/{} é invalida".format(dia, mes, ano))
