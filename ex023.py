from math import floor
num = int(input('Digite um número entre 0 e 9999: '))
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(floor(num % 10)))
num = num / 10
print('Dezena: {}'.format(floor(num % 10)))
num = num / 10
print('Centena: {}'.format(floor(num % 10)))
num = num / 10
print('Milhar: {}'.format(floor(num % 10)))

#unidade = num // 1 % 10
#dezena = num // 10 % 10
#centena = num // 100 % 10
#milhar = num // 1000 % 10
