import math
import numpy as np
a = float(input("Введите a:"))
print("Цикл for")
for i in np.arange(-3, 3.3, 0.3):
    try:
        if math.fabs(math.sin(i)) > 0.5:
            f = math.pow(i+a,2)
        elif math.fabs(math.sin(i)) <= 0.5:
            f = i + 1
        print(f"{i}){f}")
    except:
        print(f"Ошибка при значении аргумента {i}")
print("\n Цикл while")
i = -3
f = 1
while i <= 3:
    try:
        if math.fabs(math.sin(i)) > 0.5:
            f = math.pow(i + a, 2)
        elif math.fabs(math.sin(i)) <= 0.5:
            f = i + 1
        print(f"{i}){f}")
        i += 0.3
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 0.3
print("\n Цикл do-while")
i = -3
f = 1
while True:
    try:
        if math.fabs(math.sin(i)) > 0.5:
            f = math.pow(i + a, 2)
        elif math.fabs(math.sin(i)) <= 0.5:
            f = i + 1
        print(f"{i}){f}")
        i += 0.3
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 0.3
    if i > 3:
        break
