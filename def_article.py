#Определение функции.
def greet():
    print("Привет, мир!")

greet()

#Вывод
Привет, мир!


#Функция с аргументами.
def greet(name):
    print("Привет,", name, "!")

greet("Алиса")
greet("Боб")
#Вывод
Привет, Алиса!
Привет, Боб!

#Функция с возвращаемым значением.
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)
#Вывод
8


#Функция с необязательными аргументами.
def greet(name="мир"):
    print("Привет,", name, "!")

greet()
greet("Алиса")
#Вывод
Привет, мир!
Привет, Алиса!


#Рекурсивные функции.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
#Вывод
120