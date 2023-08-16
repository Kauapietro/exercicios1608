vetor = []
for i in range (5):
    num = int(input(f'digite o valor {i + 1}° valor: '))
    vetor.append(num)
print(vetor)
x = int(input("Coloque o valor solicitado: "))
for i,n in enumerate(vetor):
    if x == n:
        print(f"este número está na {i}° posição: ")
    else:
        print(-1)
        break
        