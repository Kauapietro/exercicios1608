#Faça um programa que preencha por leitura um vetor de 10 posiçoes
#e conta quantos valores diferentes existem no vetor:

lista = [0]
for i in range (10):
    tmp = int(input(f'Digite o {i+1}" número: '))
    lista.append(tmp)
print(lista)

numerosunicos = []
for n in lista:
    if n not in lista:
        numerosunicos.append(n)
print(f'Na lista tem, {numerosunicos}')
