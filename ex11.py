while True:
    str_input = input("Введите строку (для выхода введите 'y'): ")
    if str_input == 'y':
        print("Выход из программы.")
        break
    flag = len(str_input) != 0
    if flag and (str_input[0] != ' ' and str_input[-1] != ' '):
        result = str_input
    elif not flag:
        print("Строчка пуста!")
    else:
        for i in range(len(str_input)):
            if str_input[i] != ' ':
                result = str_input[i:]
                break
        for i in range(len(result) - 1, -1, -1):
            if result[i] != ' ':
                result = result[:i + 1]
                break
    if flag:
        print(f"Исходный вариант: [{str_input}]")
        print(f"Результат: [{result}]")