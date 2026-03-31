Декораторы в Python — это удобный инструмент,
который позволяет добавлять функциональность к функциям или классам без изменения их исходного кода.

Представим, что мы хотим украсить торт. Мы не меняем сам торт,
а добавляем сверху украшения.
Так же работают декораторы — они «украшают» наши функции, делая их более гибкими и функциональными.

На этом занятии мы узнаем, как декораторы помогают писать более чистый,
компактный и переиспользуемый код.

С их помощью можно легко реализовать такие возможности,
как логирование, проверка прав доступа или измерение времени выполнения.



На занятии мы:

поймем, что такое декораторы и как они работают.

научимся писать простые и многослойные декораторы.

будем использовать встроенные декораторы Python, такие как @staticmethod, @classmethod и @property.

узнаем, как декораторы применяются в реальных проектах, например, для авторизации пользователей или ведения логов.

разберемся, как декораторы помогают избегать повторения кода и улучшить читаемость программ.


В Python функции — это объекты, и их можно передавать в другие функции как аргументы.

Это позволяет писать код, где одна функция может управлять поведением другой.
Эта идея лежит в основе декораторов.

Пример передачи функции в другую функцию:

def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)  # Вывод: 25

В этом примере apply_function принимает функцию square как аргумент и применяет её к значению 5.

Именно благодаря такой гибкости Python позволяет создавать декораторы,
которые оборачивают функции и добавляют им новую функциональность.

Декораторы в Python — это особые функции,
которые позволяют оборачивать другие функции или классы,
добавляя им дополнительную функциональность.


Они помогают изменить или расширить поведение функции или метода без изменения их исходного кода.



Декораторы полезны, когда мы хотим:

Добавить новую функциональность без изменения существующего кода.

Избежать повторения кода.

Сделать ваш код более читаемым и модульным.


Как работают декораторы?

Декоратор — это функция, которая принимает другую функцию как аргумент,
выполняет некоторую дополнительную логику и возвращает новую функцию.

Пример 1: Простая функция-декоратор

def decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

@decorator
def say_hello():
    print("Привет, мир!")

say_hello()

Что происходит?

Декоратор @decorator оборачивает функцию say_hello внутри функции wrapper.
При вызове say_hello() сначала выполняется код в wrapper,
а затем вызывается сама функция say_hello.

Вывод:

До вызова функции
Привет, мир!
После вызова функции
Как пишутся декораторы?




Пример 2: Декоратор с аргументами

Декораторы могут работать и с функциями, принимающими аргументы.

def decorator(func):
    def wrapper(name):
        print("До вызова функции")
        func(name)
        print("После вызова функции")
    return wrapper

@decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Иван")
Вывод:

До вызова функции
Привет, Иван!
После вызова функции


Встроенные декораторы в Python

Python предоставляет несколько встроенных декораторов:

@staticmethod
Позволяет создать метод,
который не требует доступа к экземпляру класса или его атрибутам.

class MyClass:
    @staticmethod
    def greet():
        print("Привет от статического метода!")

MyClass.greet()

@classmethod
Создаёт метод, который получает доступ к самому классу, а не к его экземпляру.

class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
        print(f"Счётчик: {cls.count}")

MyClass.increment_count()  # Счётчик: 1




@property
Используется для создания методов, которые работают как атрибуты.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(5)
print(circle.radius)  # Вывод: 5




Как работают декораторы с несколькими слоями?

Мы можем применять несколько декораторов к одной функции. Они выполняются сверху вниз.

def decorator1(func):
    def wrapper():
        print("Декоратор 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Декоратор 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Привет!")

say_hello()
Вывод:

Декоратор 1
Декоратор 2
Привет!



Декораторы и реальная жизнь

Логирование (Logging)
Декораторы часто используются для автоматического ведения журнала работы функций.

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 4))
Авторизация (Authorization)




Проверяют, имеет ли пользователь доступ к выполнению определённых операций.

def authorize(func):
    def wrapper(user):
        if user == "admin":
            return func()
        else:
            print("Доступ запрещён")
    return wrapper

@authorize
def secret():
    print("Секретная информация!")

secret("admin")  # Вывод: Секретная информация!
secret("guest")  # Вывод: Доступ запрещён







Преимущества декораторов:

Упрощают добавление новой функциональности.

Повышают читаемость и модульность кода.

Помогают избежать дублирования кода.

Теперь мы знаем, как работают декораторы, и видим,
что они полезны как в простых, так и в сложных проектах.








Типичные ошибки
Тип ошибки 1: Декоратор не возвращает функцию — TypeError: ‘NoneType’ object is not callable

Если забыть вернуть функцию из декоратора, он не будет работать.

Пример ошибки:

def decorator(func):
    def wrapper():
        print("Декоратор работает")
    # Здесь забыли return wrapper

@decorator
def say_hello():
    print("Привет!")
Вывод:

TypeError: 'NoneType' object is not callable


Решение:

def decorator(func):
    def wrapper():
        print("Декоратор работает")
        func()
    return wrapper  # Добавили возврат функции-обёртки

@decorator
def say_hello():
    print("Привет!")

say_hello()  # Вывод: Декоратор работает, Привет!






Тип ошибки 2: Неправильное использование декоратора — TypeError: ‘function’ object is not callable

Если декоратор принимает аргументы,
но используется как обычный декоратор, это вызовет ошибку.

Пример ошибки:

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat  # Пропустили скобки и аргумент
def greet():
    print("Привет!")


Вывод:

TypeError: 'function' object is not callable

Решение:

@repeat(3)  # Указали аргумент для декоратора
def greet():
    print("Привет!")

greet()  # Вывод: Привет! (три раза)







Тип ошибки 3: Потеря имени функции из-за декоратора

Если декоратор не использует functools.wraps, имя и документация исходной функции будут потеряны.

Пример ошибки:

def decorator(func):
    def wrapper():
        print("Обёртка")
        func()
    return wrapper

@decorator
def greet():
    """Функция приветствия."""
    print("Привет!")

print(greet.__name__)  # Вывод: wrapper (а не greet)



Решение:

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Обёртка")
        func()
    return wrapper

@decorator
def greet():
    """Функция приветствия."""
    print("Привет!")

print(greet.__name__)  # Вывод: greet





Тип ошибки 4: Аргументы декорируемой функции не учтены

Если функция принимает аргументы, но декоратор их не обрабатывает, это вызовет ошибку.

Пример ошибки:

def decorator(func):
    def wrapper():
        print("Обёртка")
        func()  # Здесь нет передачи аргументов
    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(3, 4)  # Ошибка: TypeError

Решение:

def decorator(func):
    def wrapper(*args, **kwargs):  # Добавили передачу аргументов
        print("Обёртка")
        func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(3, 4)  # Вывод: Обёртка, 7




Практикум
Задача 1: Логирование действий пользователя

Ситуация: мы разрабатываем приложение, которое отслеживает действия пользователей,
такие как вход в систему, обновление профиля или отправка сообщения.
Для каждого действия нужно сохранять лог с именем пользователя и названием выполненной функции.
Лог-файлы позволяют анализировать действия пользователей и выявлять ошибки в работе системы.

Задача: создать декоратор log_action, который:

Логирует имя пользователя и выполняемое действие.
Сохраняет эту информацию в текстовый файл actions.log.
Работает с любыми функциями, которые принимают username как первый аргумент.

Шаги реализации:

Напишите функцию log_action, которая принимает другую функцию, логирует её вызов и сохраняет информацию в файл.
from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open("actions.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"Пользователь: {username}, действие: {func.__name__}\n")
        return func(username, *args, **kwargs)
    return wrapper


Используйте декоратор, чтобы оборачивать функции, которые принимают имя пользователя.
При каждом вызове обернутой функции записывайте информацию в файл actions.log.




Реализация:

from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open("actions.log", "a", encoding="utf-8") as log_file:
            log_file.write(f"Пользователь: {username}, действие: {func.__name__}\n")
        return func(username, *args, **kwargs)
    return wrapper

@log_action
def login(username):
    print(f"{username} вошёл в систему.")

@log_action
def update_profile(username, profile_data):
    print(f"{username} обновил профиль с данными: {profile_data}.")

# Пример использования
login("Alice")
update_profile("Alice", {"age": 25, "city": "Москва"})








Задача 2: Авторизация доступа к секретным данным

Ситуация: мы разрабатываем систему для управления секретными данными,
доступ к которым должен быть только у пользователей с правами администратора.
Необходимо автоматически проверять права доступа перед выполнением функции.

Задача: создать декоратор authorize_admin, который:

Проверяет, является ли пользователь администратором.
Если пользователь администратор, выполняет функцию.
Если пользователь не администратор, выводит сообщение «Доступ запрещён».


Шаги реализации:

Напишите декоратор authorize_admin, который проверяет роль пользователя.
from functools import wraps

def authorize_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") == "admin":
            return func(user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для пользователя {user['name']}.")
    return wrapper


Проверяйте значение ключа role в словаре пользователя.
Если пользователь не администратор, выводите сообщение об отказе.






Реализация:

from functools import wraps

def authorize_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") == "admin":
            return func(user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для пользователя {user['name']}.")
    return wrapper

@authorize_admin
def view_secret_data(user):
    print(f"Секретные данные доступны для {user['name']}.")

# Пример использования
admin_user = {"name": "Alice", "role": "admin"}
regular_user = {"name": "Bob", "role": "user"}

view_secret_data(admin_user)  # Вывод: Секретные данные доступны для Alice.
view_secret_data(regular_user)  # Вывод: Доступ запрещён для пользователя Bob.