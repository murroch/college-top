# Задача 1
s = input("Введите строку: ")
a = s.lower() # lower делает все буквы строчными!!!м

if a == a[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")


# Задача 2
s = input("Введите текст: ")
slova = input("Введите зарезервированные слова через пробел: ")

res = ""
w = ""

for c in s:
    if c or c == "_":
        w += c
    else:
        if w.lower() in slova:
            w = w.upper() # upper делает все буквы заглавными!!!
        res += w + c
        w = ""
if w.lower() in slova:
    w = w.upper()
res += w

print("Измененный текст:", res)


# Задача 3
s = input("Введите текст: ")
n = 0
flag = False

for c in s:
    if c in ".!?":
        if flag:
            n += 1
            flag = False
    elif not c:
        flag = True
if flag:
    n += 1

print("Количество предложений:", n)
