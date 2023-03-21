real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.22
euro = real / 5.57
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}.'.format(real, dolar, euro))

#dolar = 3.27
#dolar = real / 3.27