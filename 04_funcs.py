"""
Пример программы с функциями
"""

user_list = ['John', 'Kate', 'David', 'Alice']


def send_message(text, users):
    for user in users:
        print(f"Отправляю текст '{text}' пользователю {user}")


send_message('Привет!', user_list)
send_message('У нас сегодня акция 30%!', user_list)
