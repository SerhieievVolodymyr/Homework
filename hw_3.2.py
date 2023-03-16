import random

f_crt = open('data.txt', 'w')
for i in range(20):
    f_crt.write(str(random.randint(2, 10)) + ' ')
    f_crt.write(str(random.randint(2, 10)) + ' ')
    f_crt.write(str(random.randint(10, 50)) + '\n')
f_crt.close()


f_read = open('data.txt', 'r')
for line in f_read:
    l = line.split()
    for i in range(1, int(l[2]) + 1):
        if not i % int(l[0]):
            print('F', end='')

        if not i % int(l[1]):
            print('B', end='')

        if i % int(l[0]) and i % int(l[1]):
            print(i, end='')

        print(' ', end='')
    print()


f_read.close()
