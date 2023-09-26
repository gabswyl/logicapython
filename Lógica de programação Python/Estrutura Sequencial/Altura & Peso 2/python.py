# # 13 - Tendo dado de entrada a altura (h) de uma pessoa, construa um algortimo que calcule seu peso ideal, utilizando as seguinte fórmulas:
# a. para homens: (72.7*h) - 58
# b. para mulheres: (62.1*h) - 44.7

sexo = int(input('Selecione opção 1 se for do sexo Masculino / Selecione opção 2 se for do sexo feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')


print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))