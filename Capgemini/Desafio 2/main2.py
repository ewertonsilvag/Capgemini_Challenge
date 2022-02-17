#QUESTÃO 2
'''
Construção de um algoritmo que informa qual é o número MÍNIMO de
caracteres que devem ser adicionados para uma string qualquer ser considerada segura.
'''
#Mensagem na tela inicial para dar informações ao usuário.

print(""" 
   # A senha do sistema deve:
   # ● Conter no MÍNIMO 6 caracteres;
   # ● Conter no MÍNIMO 1 digito;
   # ● Conter no MÍNIMO 1 letra em minúsculo;
   # ● Conter no MÍNIMO 1 letra em maiúsculo;
   # ● Conter no MÍNIMO 1 caractere especial. Os caracteres especiais válidos são: !@#$%^&*()-+
""")

#Variável 'senha' recebendo o input do usuário.
senha = str(input("Digite sua senha: "))

#Variável  'qtd_caracteres' com a função len que retorna o número de caracteres de uma string.
qtd_caracteres = len(senha)

#Loop 'while' para garantir que a senha tenha 6 caracteres com a função len que retorna a quantidade de caracteres da string.
while len(senha) < 6: 
    print(f"Sua senha tem {6-len(senha)} digito(s).")
    #Input para receber novamente a senha do usuário caso não tenha 6 dígitos.
    senha = input("Por favor, tente novamente: ") 

print('Senha cadastrada no sistema!')