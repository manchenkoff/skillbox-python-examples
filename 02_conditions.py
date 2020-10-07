"""
Пример программы с условными конструкциями
"""

number_1 = int(input("Введите число 1 >>> "))
number_2 = int(input("Введите число 2 >>> "))

if number_1 > number_2:
    print("Число 1 больше")
elif number_1 == number_2:
    print("Числа равны")
else:
    print("Число 2 больше")
