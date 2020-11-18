# 3. Написать программу, которая:
#       - выводит следующее меню на экран
#           1. Ввести значения а и b
#           2. Умножить значения а и b
#           3. Делить а на b
#           4. Выход
#       - реализует кажду опцию как фукцию
#       - реализует все ошибки и исключения.


print('Меню')
print('1. Ввести значения a и b')
print('2. Умножить значения a и b')
print('3. Делить значение a на b')
print('4. Выйти')
print('Выберите опцию:')

userchoise = int(input())
a = -9999999999 # Болатжан Арменович сказал поставить сюда значения
b = -9999999999 # которые пользователь точно не введет
while userchoise != 4:
    if (userchoise < 1) | (userchoise > 4):
        print('Такого пункта нет, введите существующий пункт:')
        userchoise = int(input())
    else:
        if userchoise == 1:
            def show (x, y):
                return x, y

            print('Введите значение а:')
            a = int(input())
            print('Введите значение b:')
            b = int(input())
            print('значение a:',a)
            print('значение a:',b)


        elif userchoise == 2:
            if a != -9999999999 and b != -9999999999:
                def umnojenie (x, y):
                    return x*y

                print('Мы умножили значения и получилось:',umnojenie(a, b))
            elif a == -9999999999 and b == -9999999999:
                def umnojenie (x, y):
                    return x*y

                print('Значения не введены, введите значения.')
                print('Введите значение а: ')
                a = int(input())
                print('Введите значение b: ')
                b = int(input())
                print('Мы умножили значения и получилось:', umnojenie(a, b))


        elif userchoise == 3:
            if a != -9999999999 and b != -9999999999:
                if b != 0:
                    def delenie(x, y):
                        return x/y
                    print('Мы умножили значения и получилось:', delenie(a, b))
                elif b == 0:
                    print('Ошибка!На ноль делить нельзя.Задайте новые значения')
                    print('Введите значение а:')
                    a = int(input())
                    print('Введите значение b:')
                    b = int(input())


            elif a == -9999999999 and b == -9999999999:
                def delenie(x, y):
                    return x / y
                print('Значения не введены, введите значения.')
                print('Введите значение а: ')
                a = int(input())
                print('Введите значение b: ')
                b = int(input())
                print('Мы умножили значения и получилось:', delenie(a, b))


        print('Меню:')
        print('1. Ввести значения a и b')
        print('2. Умножить значения a и b')
        print('3. Делить значение a на b')
        print('4. Выйти')
        print('Выберите опцию:')
        userchoise = int(input())