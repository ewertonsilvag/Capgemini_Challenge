#QUESTÃO 03
'''
Dada uma string qualquer, desenvolva um algoritmo que 
encontre o número de pares de substrings que são anagramas.
'''
#Módulo usado para a criação de iteradores, no nosso caso vamos usar o iterador combinatório
import itertools 

#Recebendo a palavra do usuário
palavra = input(str("Digite a palavra: "))

#Utilizando a classe 'list' do módulo itertools para separar todos os caracteres da palavra recebida pelo usuário dentro de uma lista
lista = list(palavra)
print(lista)

#Variável recebendo a lista de caracteres + o módulo de combinação. o R é o parâmetro de permutação, no caso é 2 pois queremos pares
anagrama = list(itertools.combinations(lista, r=2))

#Contador para percorrer todas as combinações dentro da lista de anagrama
for i in list(anagrama):
    print (i)
print(len(anagrama))
