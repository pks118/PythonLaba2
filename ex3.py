import math
k = 6
x = 1
s = 1

print("Цикл for")
for n in range(1, k+1):
    s += math.pow((x*n-1), 3)
    print(s)

print("Цикл while")
s = 1
n = 1
while(n <= k):
    s += math.pow((x*n-1), 3)
    print(s)
    n += 1

print("Цикл do-while")
x = 1
s = 1
n = 1
while True:
    s += math.pow((x*n-1), 3)
    n += 1
    print(s)
    if n > k:
        break