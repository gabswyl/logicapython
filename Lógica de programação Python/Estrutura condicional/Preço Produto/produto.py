# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

primeiroProduto = float(input("Insira o preço do primeiro produto: "))
segundoProduto = float(input("Insira o preço do segundo produto: "))
terceiroProduto = float(input("Insira o preço do terceiro produto: "))

if primeiroProduto < segundoProduto and primeiroProduto < terceiroProduto:
  print("O primeiro produto é mais barato")
elif segundoProduto < primeiroProduto and segundoProduto < terceiroProduto:
    print("O segundo produto é mais barato")
elif terceiroProduto < primeiroProduto and terceiroProduto < segundoProduto:
    print("O terceiro produto é mais barato")
else:
   print("Todos produtos possui valores iguais")
