def bem_vindo():
    print('''
    Bem-vindo a calculadora
    ''')


...
bem_vindo()


# Definido funçoes


def calculate():
    operation = input('''
Por favor digite a operação:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Digite um numero: '))
    number_2 = int(input('Digite outro: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não fez uma operação válida, Por favor tente novamente .')

    again()


def again():
    calc_again = input('''
Você deseja calcular novamente?
Digite S para sim,e N para não. ''')

    if calc_again.upper() == 'S':
        calculate()

    elif calc_again.upper() == 'N':
        print('Nos vemos na próxima.')
    else:
        again()


calculate()
