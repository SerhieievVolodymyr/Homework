print("Калькулятор")
a = float(input('Число 1: '))
d = input('Дія("+", "-", "/", "*", "mod"(залишок від ділення), "pow"(ступінь), "div"(ділення націло): ')
b = float(input('Число 2: '))

if d == '+':
    print(a + b)
elif d == '-':
    print(a - b)
elif d == '/':
    if b == 0:
        print('Ділення на 0!')
    else:
        print(a / b)
elif d == '*':
    print(a * b)
elif d == 'mod':
    if b == 0:
        print('Ділення на 0!')
    else:
        print(a % b)
elif d == 'pow':
    print(a ** b)
elif d == 'div':
    if b == 0:
        print('Ділення на 0!')
    else:
        print(a // b)
else:
    print('Неправильно вказана дія ')