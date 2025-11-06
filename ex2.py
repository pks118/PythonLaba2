import math
k = 5
x = 1
p = 1

print("Цикл for")
for n in range(1, k+1):
    p *= 1/ (math.sqrt(2*n)) + x
    print(p)

print("Цикл while")
p = 1
n = 1
while n <= k:
    p *= 1/ (math.sqrt(2*n)) + x
    print(p)
    n += 1

print("Цикл do-while")
n = 1
p = 1
while True:
    p *= 1/ (math.sqrt(2*n)) + x
    n += 1
    print(p)
    if n > k:
        break