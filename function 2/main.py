# 2. Написать программу, которая считает 5 значений, введенных пользователем из консоли, сохранит их в список
#    затем передаст значения в фукцию, которая выводит на экран сумму значений списка.

def function2():
    print('Введите первое число для списка:')
    v = int(input())
    values.append(v)
    print('Введите второе число для списка:')
    w = int(input())
    values.append(w)
    print('Введите третье число для списка:')
    x = int(input())
    values.append(x)
    print('Введите четвертое число для списка:')
    y = int(input())
    values.append(y)
    print('Введите пятое число длясписка:')
    z = int(input())
    values.append(z)
    print('Список введенных Вами чисел:',values)
    print('Сумма введенных Вами значений равна:',v+w+x+y+z)


values = []
function2()








