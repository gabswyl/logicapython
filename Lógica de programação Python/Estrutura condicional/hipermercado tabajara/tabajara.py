# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
# compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


print("Carnes Disponiveis: file duplo, alcatra e picanha")

escolherCarne = str(input("insira qual tipo de carne que você quer: "))
qntd = int(input("Quantidade: "))

if escolherCarne == "file duplo":
 if qntd >= 5:
  compra = qntd * 5.8
 else:
  compra = qntd * 4.9

if escolherCarne == "alcatra":
 if qntd >= 5:
  compra = qntd * 6.8
 else:
  compra = qntd * 5.9


if escolherCarne == "picanha":
 if qntd >= 5:
  compra = qntd * 7.8
 else:
  compra = qntd * 6.9


print("PIX, cartao ou Dinheiro? ")
formadePagamento = str(input("Insira a forma de pagamento que deseja: "))

if formadePagamento == "cartao":
  desconto = compra - (compra * 0.5)
  resultadoFinal = desconto
else:
  resultadoFinal = compra

print("Tipo de carne: ", escolherCarne)
print("Quantidade desejada: ", qntd)
print("Valor total: ", resultadoFinal)
print("Forma de pagamento: ", formadePagamento)
