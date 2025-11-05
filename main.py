k = int(input("Введите k:"))

x = 1
p = 1

print("Цикл for")
for n in range(1, k+1):
    p *= (n / 2) + x
    print(p)

print("Цикл while")
p = 1
n = 1
while(n <= k):
    p *= (n / 2) + x
    print(p)
    n += 1

print("Цикл for")
x = 1
p = 1
n = 1
for i in range(k):
    p *= (n / 2) + x
    n += 1
    print(p)