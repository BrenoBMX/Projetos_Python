p = float(input('Qual o preço do produto ? R$'))
d = p - (p * 5 / 100)
print('O valor do produto é R${:.2f}, mas com o desconto o valor é R${:.2f}.'.format(p, d))
