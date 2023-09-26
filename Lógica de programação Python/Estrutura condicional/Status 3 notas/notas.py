# Faça um programa para a leitura de tres notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete com a respectiva media alcançada:
# - A mensagem "Reprovado", se a media for menor do que 7 com a respectiva média alcançada:
# - A mensagem "Aprovado com distinção", se a média for igual a dez

notaAluno = float(input("Insira sua primeira nota: "))
segundaNota = float(input("Insira sua segunda nota: "))
terceiraNota = float(input("Insira sua segunda nota: "))

calcNotas = (notaAluno + segundaNota + terceiraNota) / 2
resultado = calcNotas

if resultado >= 7:
  print("Parabéns! Você foi aprovado")
elif resultado >= 10:
  print("Parabéns! Você foi aprovado com distinção")
else:
    print("Infelizmente! Você foi reprovado.")