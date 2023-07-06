#Construir um programa que leia um número inteiro e positivo informado pelo usuário.
# O programa deve verificar se o número informado pelo usuário é primo ou não.
# Autor: Diego Vale do Nascimento - 09/10/2022
mensagem = "Executando um script"
for palavra in mensagem.split():
    print(palavra)

n = 150
i = 100
while(i <= n):
    if(i % 2 == 0):
        print('{}  '.format(i), end='')
    i += 1