#QUESTÃO 01
'''
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere *
e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter
nenhum espaço.
'''
# Váriavel para receber o input de um número inteiro e não negativo.
n= int(input("Digite um número inteiro e não negativo: "))

#Loop para não aceitar valores negativos e excluindo a possibilidade de receber um 0 como valor.
while n<=0 or (n//1) !=n:
    n= int(input("Inválido, digite um número inteiro e não negativo: "))

#Contador i começando 0 e acrescentando +1 enquanto percorre o valor N.
for i in range(0,n+1):
    #Print usando da multiplicação entre espaços em branco, asteristicos e o contador para conseguir a escada.
    print(" " * (n-i) + "*" * i) 