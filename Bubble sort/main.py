# глобальные переменные
userChoice = 0      # переменная, которая хранит выбор пользователя
values = [12, 32, 2, 0 , 11, 15, 88, 74, 33, 56, 10, 22, 17, 51, 59]         # Задание 1: объявить переменную, котоая будет хранить 15 значений


# Выводим меню пользователя
print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')

# Считываем ввод пользователя с клавиатуры
userChoice = int(input())


# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только знаенчия, из меню (1-6), в остальных случаях выдвала ошибку.
while userChoice != 6:
    if (userChoice < 1) | (userChoice > 6):                     # проверить, что выбор пользоателя в диапазоне 1-6
        print('Такой опции нет, выберите существующую опцию.')
        userChoice = int(input())
    else:
        # Задание 3: распечатать значения.
        if userChoice == 1:
            print(values)
        # Задание 3: добавить новое значение.
        elif userChoice == 2:
            print('Введите новое число:')
            newValue = int(input())
            values.append(newValue)
            print(values)
        # Задание 4: реализовать удаление значений путем перезаписи идей справа на лево.
        elif userChoice == 3:
            if len(values) != 0:
                print('Введите число для удаления:')
                searchValue = int(input())
                counter = 0
                deleted = False
                for count in range(0, len(values)):
                    if (values[count] == searchValue) & (count < len(values)):
                        deleted = True
                        while count+1 < len(values):
                            values[count] = values[count+1]
                            count = count+1
                if deleted is True:
                    del values[count]
                    print(values)
                elif deleted is False:
                    print('Значения нет в базе данных.')
            else:
                print('База пустая! Добавте значения!')
        # Задание 4: реализовать поиск значения с выводом его индекса в списке.
        elif userChoice == 4:
            if len(values) != 0:
                print('Введите число для поиска его индекса:')
                searchValue = int(input())
                found = False
                for count in range(0, len(values)):
                    if values[count] == searchValue:
                        found = True
                        print('Индекс значения "', searchValue, '":', count)
                if found is False:
                    print('Значение не найдено!')
            else:
                print('База пустая! Не можем искать!')

        elif userChoice == 5:
            if len(values) != 0:
                print("Список до: ", values)
                for i in range(len(values)):
                    for j in range(i, len(values)):
                        if values[i] > values[j]:
                            d = values[j]
                            values[j] = values[i]
                            values[i] = d

                print('Список после:', values)
            else:
                print('База пуста!')

        print('\n Меню:')
        print('1. Вывести на экран все знаения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('6. Выйти')
        print('Введите опцию:')
        userChoice = int(input())