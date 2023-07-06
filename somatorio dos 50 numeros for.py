#Implementar um script em python que imprima todos os números entre 1 e 50.
# Ao final, o programa também deve imprimir o somatório destes números.
# Este exercício deve ser implementado utilizando o comando for.
# Autor: Diego Vale do Nascimento - 09/10/2022
soma = 0
n = 50
for n in range(1, n + 1):
    print(n, end=' ')
    soma += n

print(' - O Somatório destes números é: {}'.format(soma))

