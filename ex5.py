import math
a = float(input("Введите a:"))
print("Цикл for")
for i in range(-9, 22, 3):
    try:
        f = (a * i ** 2 + 3) / math.sin(math.pi * i / 6)
        print(f"{i}){f}")
    except:
        print(f"Ошибка при значении аргумента {i}")

print("\n Цикл while")
i = -9
f = 1
while i <= 21:
    try:
        f = (a * i ** 2 + 3) / math.sin(math.pi * i / 6)
        print(f"{i}){f}")
        i += 3
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 3

print("\n Цикл do-while")
i = -9
f = 1
while True:
    try:
        f = (a * i ** 2 + 3) / math.sin(math.pi * i / 6)
        print(f"{i}){f}")
        i += 3
    except:
        print(f"Ошибка при значении аргумента {i}")
        i += 3
    if i > 21:
        break
