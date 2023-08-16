#dada a lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52], faça um programa que:
#a)imprima o maior elemento
#b)imprima o menor elemento
#c)imprima os numeros pares
#d)imprima o numero de ocorrencias do primeiro elemento da lista
#e)imprima a media dos elementos
#f)imprima a soma dos elementos de valor negativo

#a)imprima o maior elemento
lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maior_numero = max(lista)
print("O maior número da lista é: ",maior_numero)

#b)imprima o menor elemento
menor_numero = min(lista)
print("O menor número da lista é: ",menor_numero)

#c)imprima os numeros pares
numeros_pares = [num for num in lista if num %2 == 0]
print("Os números pares são: ",numeros_pares)

#d)imprima o numero de ocorrencias do primeiro elemento da lista
contador = 0
for i in lista: 
    if i == lista[0]:
        contador +=1
print("O número do primeiro elemento é:", contador)

#e)imprima a media dos elementos
soma = sum(lista)
media = soma/len(lista)
print(f"A média dos números é:{media:.2f}")

#f)imprima a soma dos elementos de valor negativo
somai = 0
for k in lista:
    if k < 0:
        somai = somai + k
print(f"A soma dos números negativos é:{somai}")



