import math
import numpy as np
a = float(input("Введите a:"))
print("Цикл for")
for i in np.arange(-2, 7.1, 0.4):
    try:
        if math.fabs(math.cos(i)) > 1/math.sqrt(2):
            f = math.sqrt(a) + i
        elif math.fabs(math.cos(i)) <= 1/math.sqrt(2):
            f = i - 1
        print(f"{i}){f}")
    except:
        print(f"Ошибка при значении аргумента {i}")
print("\n Цикл while")
i = -2
f = 1
while i <= 7:
    try:
        if math.fabs(math.cos(i)) > 1 / math.sqrt(2):
            f = math.sqrt(a) + i
        elif math.fabs(math.cos(i)) <= 1 / math.sqrt(2):
            f = i - 1
        print(f"{i}){f}")
        i += 0.4
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 0.4
print("\n Цикл do-while")
i = -2
f = 1
while True:
    try:
        if math.fabs(math.cos(i)) > 1 / math.sqrt(2):
            f = math.sqrt(a) + i
        elif math.fabs(math.cos(i)) <= 1 / math.sqrt(2):
            f = i - 1
        print(f"{i}){f}")
        i += 0.4
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 0.4
    if i > 7:
        break
