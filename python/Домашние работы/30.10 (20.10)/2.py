size = int(input("Сторона квадрата: ")) #задача1

for row in range(size):
    print("*" * size)
    
    
    
width = int(input("Ширина: ")) #задача2
height = int(input("Высота: "))

for row in range(height):
    print("*" * width)
    
    
size = int(input("Сторона квадрата: "))

for row in range(size):
    if row == 0 or row == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")




number = int(input("Введите целое число: ")) #задача3
digits = str(abs(number))

count = 0
total = 0
zeros = 0

for digit in digits:
    count += 1
    total += int(digit)
    if digit == "0":
        zeros += 1

while True: #задача4
    print("1. Количество цифр")
    print("2. Сумма цифр")
    print("3. Среднее арифметическое цифр")
    print("4. Количество нулей")
    print("0. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print("Количество цифр:", count)
    elif choice == "2":
        print("Сумма цифр:", total)
    elif choice == "3":
        print("Среднее арифметическое:", total / count)
    elif choice == "4":
        print("Количество нулей:", zeros)
    elif choice == "0":
        break
    else:
        print("Такого пункта нет.")
        




size = int(input("Размер клетки: ")) #задача5

for row in range(8):
    if row % 2 == 0:
        line = ("*" * size + "-" * size) * 4
    else:
        line = ("-" * size + "*" * size) * 4

    for repeat in range(size):
        print(line)







from random import randint #задача6

print("1. Лёгкий: 3 вопроса, числа до 5")
print("2. Средний: 5 вопросов, числа до 7")
print("3. Сложный: 10 вопросов, числа до 10")

level = input("Выберите уровень: ")
while level not in ("1", "2", "3"):
    level = input("Введите 1, 2 или 3: ")

if level == "1":
    questions = 3
    limit = 5
elif level == "2":
    questions = 5
    limit = 7
else:
    questions = 10
    limit = 10

correct = 0

for question in range(questions): #задача7
    a = randint(2, limit)
    b = randint(2, limit)
    answer = int(input(f"{a} * {b} = "))

    if answer == a * b:
        correct += 1
        print("Верно!")
    else:
        print("Правильный ответ:", a * b)

print(f"Оценка: {correct} из {questions}")




 
size = int(input("Высота верхней половины ромба вместе с серединой: ")) #задача8

for row in range(1, size + 1):
    print(" " * (size - row) + "*" * (2 * row - 1))

for row in range(size - 1, 0, -1):
    print(" " * (size - row) + "*" * (2 * row - 1))


 