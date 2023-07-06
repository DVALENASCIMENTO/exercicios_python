#imprimir todos os números pares entre 0 e o numero informado pelo
#usuário. Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero
#informado pelo usuário. Este exercício deve ser implementado utilizando o comando for.
# Autor: Diego Vale do Nascimento - 09/10/2022
print('='*51)
n = int(input("Insira um número positivo: "))
for n in range(0, n+2, 2):
    print(n, end=' ')
print('Números pares')
for n in range(1, n+2, 2):
    print(n, end=' ')
print('Números ímpares')

