"""
Пример программы для работы с циклом
"""

calories = 5000
goal = 3600
step = 340
step_count = 0

while calories > goal:
    calories -= step
    step_count += 1

    print(f"Шаг {step_count}, калории {calories}")
else:
    print(f"Шагов сделано - {step_count}")
