# Bektemir Kumarbay uulu
# bektemirkumarbayuulu@gmail.com
from random import randint
''' 1-задания '''
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
       55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
s = []
for i in range(len(lst)):
    s.append([i, lst[i]])  # Создать двумерный массив
d = dict(s)  # Создать словарь
print(d)    # Вывести его на экран

'''2-задания'''
c = 0
x = randint(1, 20)
while True:
    y = int(input('Угадай число: '))
    if y < x:
        print('слишком мало')
    elif y > x:
        print('слишком много')
    else:
        print('Класс! Вы угадали!!!')
        break
    c += 1
    if c >= 5:
        print('Все, вы не выиграли. Игра завершилась')
        break
'''3 - задания '''

stra = input('ведите сртока (7 символ): ')
stra_1 = stra[2]+stra[3]+stra[4]
print(stra_1)

'''4- задания '''
a1 = input('первое строка: ')
a2 = input('второе строка: ')
if len(a1) <= len(a2):
    a3 = ''
    for i in range(len(a1)):
        a3 += a1[i]
        a3 += a2[i]
    print(a3)
else:
    a3 = ''
    for i in range(len(a2)):
        a3 += a1[i]
        a3 += a2[i]
    print(a3)
