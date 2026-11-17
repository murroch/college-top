import random

a = [random.randint(-10, 10) for i in range(10)]
print("Список:", a)

b = sum(j for j in a if j < 0)
c = sum(j for j in a if j % 2 == 0)
d = sum(j for j in a if j % 2 != 0)
p = 1
for i in range(0, len(a), 3):
    p *= a[i]
m = a.index(min(a))
n = a.index(max(a))
l = min(m, n) + 1
r = max(m, n)
q = 1
for j in a[l:r]:
    q *= j
k = [i for i in range(len(a)) if a[i] > 0]

if len(k) >= 2:
    s = sum(a[k[0] + 1:k[-1]])
else:
    s = 0

print("Сумма отрицательных:", b)
print("Сумма четных:", c)
print("Сумма нечетных:", d)
print("Произведение элементов с индексами кратными 3:", p)
print("Произведение между минимумом и максимумом:", q)
print("Сумма между первым и последним положительными:", s)






import random
a = [random.randint(-10, 10) for i in range(10)]
print("Исходный список:", a)
chet = []
for i in a:
    if i % 2 == 0:
        chet.append(i)
print("Четные числа:", chet)
nechet = []
for i in a:
    if i % 2 != 0:
        nechet.append(i)
print("Нечетные числа:", nechet)
otric = []
for i in a:
    if i < 0:
        otric.append(i)
print("Отрицательные числа:", otric)
pol = []
for i in a:
    if i > 0:
        pol.append(i)
print("Положительные числа:", pol)