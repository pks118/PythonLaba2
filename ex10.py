import math


def a_fun(k):
    if (k == 1):
        return 1
    elif (k == 2):
        return 0
    elif (k == 3):
        return 1
    else:
        return a_fun(k - 1) * math.sqrt(math.fabs((a_fun(k - 3)))) + (k*math.sin(a_fun(k - 2)))


n = (int(input("Введите номер члена последовательности ")))
if (n < 4):
    print("Можно найти только 4 член прогрессии или следующие")
else:
    a1 = 1
    a2 = 1
    a3 = 1
    a_summa = a1 + a2 + a3
    a_count = 3
    print("\n1 способ:")
    print("a 1", "=", a1)
    print("a 2", "=", a2)
    print("a 3", "=", a3)
    a1_new = a1
    a2_new = a2
    a3_new = a3
    for k in range(4, n + 1):
        a = a1_new * math.sqrt(math.fabs(a3_new)) + (k*math.sin(a2_new))
        if ((a // 1) % 2 == 0) :
            a_summa += a
            a_count += 1
            print("Целая часть чётная, a",k,"=",a, " ", a//1)
        else :
            print("a", k, "=", a)

        a3_new = a2_new
        a2_new = a1_new
        a1_new = a
    average = a_summa / a_count
    print(f"среднее арифметическое = {average}")
    print("\n2 способ:")
    for i in range(1, n + 1):
        a = a_fun(i)
        if ((a // 1) % 2 == 0):
            a_summa += a
            a_count += 1
            print("Целая часть чётная, a", k, "=", a, " ", a // 1)
        else:
            print("a", k, "=", a)
    a_average = a_summa / a_count
    print(f"среднее арифметическое = {average}")

