# faça um programa um leia um numero inteiro menor que 1000 e imprima a qntd de centenas, dezenas e unidades do msm

numeroInt = int(input("Insira o numero menor que 1000: "))

if numeroInt > 1000:
    print("Programa encerrado! Insira um número menor que 1000")
else:
    numero = numeroInt
    unidade = numero % 10
    numero = (numero - unidade) / 10
    dezena = numero % 10
    numero = (numero - dezena) / 10
    centena = numero
    print("Centenas: {}, Dezenas: {}, Unidades: {}".format(int(centena), int(dezena), int(unidade)))