from datetime import datetime

# Создание объекта datetime
dt = datetime(2023, 6, 25, 10, 30, 0)
print(dt)

#Вывод
2023-06-25 10:30:00

from datetime import datetime

# Получение текущей даты и времени
now = datetime.now()
print(now)

#Вывод
2023-06-25 12:45:23.456789

from datetime import datetime

# Форматирование вывода даты и времени
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

#Вывод
2023-06-25 12:45:23


from datetime import datetime, timedelta

# Арифметические операции с датами
now = datetime.now()
next_week = now + timedelta(weeks=1)
print(next_week)

one_hour_ago = now - timedelta(hours=1)
print(one_hour_ago)

new_date = now.replace(year=2024, month=9, day=1)
print(new_date)

#Вывод
2023-07-02 12:45:23.456789
2023-06-25 11:45:23.456789
2024-09-01 12:45:23.456789



