import random

f_crt = open('data.txt', 'w')
for i in range(20):
    f_crt.write(str(random.randint(2, 10)) + ' ')
    f_crt.write(str(random.randint(2, 10)) + ' ')
    f_crt.write(str(random.randint(10, 50)) + '\n')
f_crt.close()


f_read = open('data.txt', 'r')
f_ans = open('answer.txt', 'w')
for line in f_read:
    l = line.split()
    for i in range(1, int(l[2]) + 1):
        if not i % int(l[0]): #'F', end=''
            f_ans.write('F')

        if not i % int(l[1]): #'B', end=''
            f_ans.write('B')

        if i % int(l[0]) and i % int(l[1]): #i, end=''
            f_ans.write(f'{i}')

        f_ans.write(' ')
    f_ans.write('\n')

f_read.close()
f_ans.close()