import math
a = float(input("Введите a:"))
for i in range(-9, 21, 3):
    try:
        f = (a * i ** 2 + 3) / math.sin(math.pi * i / 6)
        print(f)
    except:
        print(f"Ошибка при значении аргумента {i}")
