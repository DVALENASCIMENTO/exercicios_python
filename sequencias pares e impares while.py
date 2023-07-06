#imprimir todos os números pares entre 0 e o numero informado pelo
#usuário. Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero
#informado pelo usuário. Este exercício deve ser implementado utilizando o comando while.
# Autor: Diego Vale do Nascimento - 09/10/2022

i = 0
n = int(input("Insira um número inteiro: "))
while(i <= n):
    if(i % 2 == 0):
        print('{}  '.format(i), end='')
        print('número par')
    i += 1
    if (i % 2 == 1):
        print('{}  '.format(i), end='')
        print('número ímpar')
    i += 1





