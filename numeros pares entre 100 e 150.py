#Implementar um script em python que imprima os números pares entre 100 e 150.
# Este exercício deve ser implementado utilizando o comando for.
# Autor: Diego Vale do Nascimento - 09/10/2022
mensagem = "Executando um script"
for palavra in mensagem.split():
    print(palavra)

n = 150
for n in range(100, n+2, 2):
    print(n, end=' ')
