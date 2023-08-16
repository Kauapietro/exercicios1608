lançamentos = 50
vetor = []
for i in range(lançamentos):
    jogada = int(input(f'{i+1}° jogada: '))
    vetor.append(jogada)
print(vetor)
faces6 = 0
for i in vetor:
    if i == 6:
        faces6+=1
porcentagem = (faces6/lançamentos)*100
print(f'{porcentagem}%')