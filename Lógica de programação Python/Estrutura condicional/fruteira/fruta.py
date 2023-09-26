# uma fruteira está vendendo frutas com a seguinte tabela de preços
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar rs 25,00, receberá ainda um desconto de 10% sobre este total.
# escreva um algortimo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kilosMorango = float(input("Insira a quantidade de kg em morangos: "))
kilosMacas = float(input("Insira a quantidade de kg em maças: "))

valorMorango = 2.50
valorMacas = 1.80

calcMorango = valorMorango * kilosMorango
calcMacas = valorMacas * kilosMacas

valorTotal = calcMorango + calcMacas

if valorTotal > 25 or (kilosMorango + kilosMacas > 8):
  desconto = valorTotal - (valorTotal * 0.10)
  print("Esse é o valor da compra: ", desconto)
else:
 valorTotal
 print("Esse é o valor da compra: ", valorTotal)