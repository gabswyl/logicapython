# Um posto está vendendo combustíveis com a seguinte tabela de desconto:
# a) alcool b) até 20 litro, desconto de 3% por litro c) acima de 20 litros, desconto de 5% por litro
# d) gasolina e) ate 20 litros, desconto de 4% por litro f) acima de 20 litros, desconto de 6% por litros.
# escreve um algoritmo que leia o numero de litros vendidos, o tipo de combustivel (codificado da seguinte forma: alcool, gasolina)
# calcule e imprima o valor a ser pago pelo cliente sabendo-se o preço do litro da gasolina e 2,50 reais o preço do litro do alcol e 1,90

precoAlcool = 1.90
precoGasolina = 2.50

tipodeCombustivel = str(input("Alcool ou Gasolina "))
litro = float(input("quantos litros: "))

if tipodeCombustivel == "Alcool":
  if litro <= 20:
   valor = litro * (precoAlcool - (precoAlcool * 0.03))
   print("Valor a ser pago:", valor)
else:
  valor = litro * (precoAlcool - (precoAlcool * 0.05))
  print("Valor a ser pago:", valor)

if tipodeCombustivel == "Gasolina":
  if litro <= 20:
   valor = litro * (precoGasolina - (precoGasolina * 0.04))
   print("Valor a ser pago:", valor)
else:
  valor = litro * (precoGasolina - (precoGasolina * 0.06))
  print("Valor a ser pago:", valor)
