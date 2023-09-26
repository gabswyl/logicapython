# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoMB = float(input('Tamanho do arquivo MB: '))
velocidadeMBPS = float(input('Velocidade da internet'))

calc = (tamanhoMB / velocidadeMBPS) * 60

print('Esse é o tempo aproximado de download do arquivo: ', calc)