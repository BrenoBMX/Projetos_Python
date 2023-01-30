def bem_vindo():
    print('''
    Bem vido a calculadora''')

    ...


bem_vindo()


def calculate():
    operation = input('''
Escolha um operador a seguir :

+ soma
- subtração
* multiplicação
/ divisão 
''')

    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite outro número: '))

    if operation == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('O calculo é inválido, tente novamente !')

    again()


def again():
    cal_again = input('''
Para calcular novamente digite S para (sim)
e N para (não))
''')

    if cal_again.upper() == 'S':
        calculate()
    elif cal_again.upper() == 'N':
        print('Nos vemos na próxima :) !')
    else:
        again()


calculate()
