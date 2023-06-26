#Функция sleep для задержки выполнения
from time import sleep

print("Привет!")
sleep(2)  # Приостановить выполнение на 2 секунды
print("Мир!")
#Вывод:
Привет!
[ожидание 2 секунды]
Мир!


#Работа с интервалами времени с помощью timedelta
from datetime import datetime, timedelta

now = datetime.now()
print("Текущая дата и время:", now)

# Добавляем одну неделю к текущей дате
one_week = timedelta(weeks=1)
future_date = now + one_week
print("Дата через неделю:", future_date)

# Вычитаем 2 дня из текущей даты
two_days = timedelta(days=2)
past_date = now - two_days
print("Дата два дня назад:", past_date)

#Вывод:
Текущая дата и время: 2023-06-25 10:30:00
Дата через неделю: 2023-07-02 10:30:00
Дата два дня назад: 2023-06-23 10:30:00

#Форматирование даты и времени
from datetime import datetime

now = datetime.now()

# Форматирование даты и времени в строку
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Форматированная дата и время:", formatted_date)

# Получение текущего года
year = now.strftime("%Y")
print("Текущий год:", year)

#Вывод:
Форматированная дата и время: 2023-06-25 10:30:00
Текущий год: 2023


#Вычисление разницы между датами и временем
from datetime import datetime, timedelta

start_time = datetime(2023, 6, 25, 10, 0, 0)
end_time = datetime(2023, 6, 25, 11, 30, 0)

duration = end_time - start_time
print("Продолжительность:", duration)

seconds = duration.total_seconds()
print("Продолжительность в секундах:", seconds)

#Вывод:
Продолжительность: 1:30:00
Продолжительность в секундах: 5400.0

