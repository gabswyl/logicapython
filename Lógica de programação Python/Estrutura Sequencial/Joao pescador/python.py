# # 14 - joao papo de pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento depescado estadode são paulo (50 quilos)
# deve pagar uma multa de 4 reais por quilo excedente. joao precisa que você faça um programa que leia a variavel peso (peso de peixes) e calcule o excesso.
# gravar na variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa que joao deverá pagar.
# imprima os dados do programa com as mensagem adequadas.


peso = float(input('Insira o seu peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print("Peso: {}".format(peso))
print('Excesso: {}'.format(excesso))
print('Multa: {}'.format(multa))