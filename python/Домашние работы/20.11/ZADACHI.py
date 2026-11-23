# Задача 1

print("Задача 1")
try:
    number = int(input("Введите целое число: "))
    print(number ** 2)
except ValueError:
    print("Введите целое число")


# Задача 2
print("Задача 2")
try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    print(a / b)
except ValueError:
    print("Нужно ввести два целых числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")


# Задача 3

print("Задача 3")
days = ["Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"]

try:
    number = int(input("Введите номер дня от 1 до 7: "))
    if number < 1 or number > 7:
        raise IndexError
    print(days[number - 1])
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")
