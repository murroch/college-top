a = int(input("Введите первое целое число: ")) #задача1
b = int(input("Введите второе целое число: "))

chet = 0
nechet = 0
sumk9 = 0

it_even = 0
it_odd = 0
countk9 = 0

for i in range(a, b + 1): 
    if i % 2 == 0:
        chet += i
        it_even += 1
    if i % 2 != 0: 
        nechet += i
        it_odd += 1
    if i % 9 == 0:
        sumk9 += i
        countk9 += 1

print("Сумма четных:", chet)
print("Среднее четных:", chet / it_even if it_even else 0)
print("Сумма нечетных:", nechet)
print("Среднее нечетных:", nechet / it_odd if it_odd else 0)
print("Сумма чисел, кратных 9:", sumk9)
print("Среднее чисел, кратных 9:", sumk9 / countk9 if countk9 else 0)

a = int(input("Введите длину: ")) #задача2
b = input("Введите символ: ")
for i in range(a):
    print(b)
    
while True:            #задача3
    number = int(input("Введите число: "))
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    elif number == 0:
        print("Number is equal to zero")
    if number == 7:
        print("Good bye!")
        break
    
    
itog = 0                          #задача4
max = None
min = None

while True:            
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    itog += num
    if max is None or num > max:
        max = num
    if min is None or num < max:
        min = num
print("Сумма:", itog)