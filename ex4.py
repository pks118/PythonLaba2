import math
a = float(input("Введите a:"))
for i in range(-3, 6, 1):
    try:
        f = (math.pow(math.e, -a*i)+math.pow(math.e, a*i))/(math.pow(i, 3) - 7 * i - 6)
        print(f)
    except:
        print(f"Ошибка при значении аргумента {i}")
