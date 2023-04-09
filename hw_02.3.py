fizz = int(input('fizz: '))
buzz = int(input('buzz: '))
number = int(input('number: '))

for i in range(1, number + 1):
    if not i % fizz:
        print('F', end='')

    if not i % buzz:
        print('B', end='')

    if i % fizz and i % buzz:
        print(i, end='')

    print(' ', end='')
