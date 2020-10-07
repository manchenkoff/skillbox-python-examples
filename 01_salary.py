"""
Пример программы для расчеты заработной платы по кол-ву дней
"""

hour_cost = int(input("Укажите стоимость часа (руб) >>> "))
day_quantity = int(input("Укажите количество рабочих дней >>> "))

total = (hour_cost * 8) * day_quantity
salary = total - (total * .13)

print(f"Сумма за {day_quantity} рабочих дня(ей) = {salary}")
