import math
a = float(input("Введите a:"))
print("Цикл for")
for i in range(-3, 7, 1):
    try:
        f = (math.pow(math.e, -a*i)+math.pow(math.e, a*i))/(math.pow(i, 3) - 7 * i - 6)
        print(f"{i}){f}")
    except:
        print(f"Ошибка при значении аргумента {i}")
print("\n Цикл while")
i = -3
f = 1
while i <= 6:
    try:
        f = (math.pow(math.e, -a*i)+math.pow(math.e, a*i))/(math.pow(i, 3) - 7 * i - 6)
        print(f"{i}){f}")
        i += 1
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 1
print("\n Цикл do-while")
i = -3
f = 1
while True:
    try:
        f = (math.pow(math.e, -a*i)+math.pow(math.e, a*i))/(math.pow(i, 3) - 7 * i - 6)
        print(f"{i}){f}")
        i += 1
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 1
    if i > 6:
        break