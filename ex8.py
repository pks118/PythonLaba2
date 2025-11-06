import math
import numpy as np
a = float(input("Введите a:"))
n = int(input("Введите n:"))
a1 = 1
a2 = 1
a3 = 0
print("Цикл for")
for i in range(4, n):
    try:
        a = math.pow(a3,2)*math.sqrt((2/i)*a1)+i
        print(f"a{i} = {a}")
    except:
        print(f"Ошибка при значении аргумента {i}")