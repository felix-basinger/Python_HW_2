# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Enter a count of coins: "))
a = int(input("Enter a count of coins with 1: "))
b = n - a
if a > n:
    print("Incorrect data")
elif a == n:
    print("All coins is 1")
else:
    str_1 = "1" * a
    str_2 = "0" * b
    sum_str = str_1 + str_2
    print(sum_str)
    count = 0

    if a > b:
        for i in sum_str:
            if i == "0":
                count += 1
        print(count)
    else:
        for i in sum_str:
            if i == "1":
                count += 1
        print(count)





