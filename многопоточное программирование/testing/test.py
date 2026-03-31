Навык тестирования кода — один из самых важных в деле программиста.
Зачем нужен код, если он не работает и/или работает неправильно?


Вспомним известные баги, например:
возможность проходить сквозь стены в старых версиях Counter-Strike или сбои в крупных банковских системах.

Такие ошибки могут стоить компании не только репутации,
но и больших финансовых потерь.
Поэтому навык тестирования кода — это не просто дополнение,
а необходимость для профессионального разработчика.


Сегодня мы познакомимся с основами тестирования и узнаем, как обнаружить и исправить ошибки в нашем коде.

Сегодня на занятии мы

узнаем основные понятия тестирования: тестовые случаи, наборы тестов и ожидания;

научимся использовать модули pytest и unittest для написания и запуска тестов;

проверим результаты выполнения функций с помощью утверждений (assertions);

рассмотрим примеры создания простых и более сложных тестов.



Глоссарий к третьему занятию
Unit Testing (Модульное тестирование)

Unit Testing — процесс проверки на корректность отдельных модулей исходного кода программы.

Test case (Тестовый случай)

Test case — отдельная проверка в рамках теста.

Assertion (Утверждение)

Assertion — проверка выполнения условия в тесте.

Test suite (Набор тестов)

Test suite — набор тестов, объединённых для выполнения.

Test runner (дословно «Тестовый бегунок»)

Test runner — инструмент для запуска тестов и отображения результатов.

Refactoring (Перепроектирование кода)

Refactoring — процесс изменения программы, не затрагивающий её поведения,
цель которого — облегчение понимания её работы.

TDD (Разработка через тестирование)

TDD (Test Driven Development) — техника создания ПО, 
основанная на повторении коротких циклов разработки: написание тестов — написание кода — рефакторинг.


Искать ошибки и тестировать программы само по себе является отдельной профессией,
однако каждый сильный программист должен обладать этими навыками на уверенном уровне:
в некоторых компаниях распространена практика TDD (Test Driven Development),
основанная на повторении небольших циклов:
написание тестов, кода и рефакторинга — редактирование кода для упрощения его понимания.


Рассмотрим типы ошибок и способы их отладки.

 
Типы ошибок
Все ошибки можно разделить на два типа:

Синтаксические
Логические

Рассмотрим каждый из типов по отдельности.

Синтаксические ошибки

Они возникают, когда код написан с нарушением правил языка программирования.

Такие ошибки легко исправляются, так как:

IDE подсвечивают их и указывают на проблемные строки;
они отображаются в виде сообщений об ошибке с указанием номера строки;
в сложных случаях можно обратиться к документации языка.
Пример:

print("Hello, world!    # Пропущена закрывающая кавычка




Логические ошибки

Их обнаружить сложнее. Код запускается без ошибок, но результат оказывается неправильным.

Существует множество методов их обнаружения.

Рассмотрим некоторые из них, а также их плюсы и минусы:

Вставка print в код
Самый простой способ — вставить команды print() в ключевые места кода,
чтобы проверить значения переменных и ход выполнения программы. Пример:

def calculate_total(price, discount):
    total = price - discount
    print(f"Price: {price}, Discount: {discount}, Total: {total}")
    return total

Плюс: лёгок в использовании.

Минус: можно упустить сообщение об ошибке в остальном выводе программы.




Использование отладчика
Современные IDE предоставляют инструменты для отладки.
Мы можем выделять строки, которые нужно отладить, чтобы пошагово анализировать выполнение программы.

Пример «дебаггера» в Visual Studio Code:
https://top-academy.site/wp-content/uploads/2025/01/%D0%91%D0%B5%D0%B7-%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.png

Это пошаговое выполнение программы, где слева отображается текущее значение каждой переменной.

Плюс: удобное отображение всех переменных на лету, легко определить, в какой именно строке была допущена ошибка.

Минус: на начальном этапе у новичков могут возникать сложности при отладке комплексных программ,
например, работающих с сетью или с графическом интерфейсом.


Инструкция assert
На этапе разработки можно использовать assert для проверки корректности данных. Пример:

def divide(a, b):
    assert b != 0, "zero division"
    return a / b

divide(5, 2)    # 2.5
divide(5, 0)    # AssertionError: zero division

Плюс: автоматическое игнорирование assert в режиме оптимизации (при запуске программы командой python -o main.py).

Минус: остановка программы после первого невыполненного assert.


Модульное тестирование
Этот инструмент позволяет автоматизировать процесс проверки отдельных модулей кода.

Плюс: тесты пишутся в отдельном модуле — основной код не нагромождается проверочными конструкциями.

Минус: невозможность проверить работу модуля построчно, отображается только результат его выполнения.

Рассмотрим основы модульного тестирования на языке Python с использованием библиотек unittest и pytest.

Основы модульного тестирования с использованием unittest

Импорт модуля:

import unittest

2. Создание тестового класса. Тестовый класс должен наследоваться от объекта unittest.TestCase:

class TestExample(unittest.TestCase):
...

3. Написание тестов. Каждый метод созданного класса, начинающийся с test_, будет выполняться как тест:

class TestExample(unittest.TestCase):
 def test_addition(self):
     self.assertEqual(2 + 2, 4)


4. Для запуска тестов используется команда unittest.main():

if __name__ == "__main__":
 unittest.main()


Основные утверждения (assertions):
assertEqual(a, b) — проверяет, равны ли значения a и b.

assertNotEqual(a, b) — проверяет, что значения a и b не равны.

assertTrue(x) — проверяет, что значение x истинно.

assertFalse(x) — проверяет, что значение x ложно.

assertRaises(Exception, func, *args, **kwargs) — проверяет, что вызов функции func вызывает исключение Exception.


Пример теста:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class TestDivideFunction(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == "__main__":
    unittest.main()


Вывод:

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK



Также рассмотрим pytest — это сторонняя библиотека для тестирования,
которая является более гибкой и удобной в использовании, чем unittest.

Использование pytest для тестирования кода
Перед использованием pytest его необходимо установить:

python3 -m pip install pytest

Преимущества pytest

Простота:
Тесты пишутся как обычные функции без необходимости наследоваться от класса.
Нет потребности вызывать unittest.main().

Разные функции:
Поддержка фикстур для настройки окружения (фикстуры — это элемент библиотеки pytest,
который используется для настройки тестового окружения),
они позволяют повторно использовать код для подготовки данных или состояния, которое нужно для выполнения тестов.

Более удобные сообщения об ошибках.

Гибкость:
Подходит не только для модульного тестирования, но и для интеграционного.

Пример теста с pytest

Пример той же функции add, но с использованием pytest:

add = lambda a, b: a + b

def test_add():
    assert add(2, 3) == 5  # Проверяем, что 2 + 3 = 5
    assert add(-1, 1) == 0  # Проверяем, что -1 + 1 = 0

Для запуска тестов используем команду:

python3 -m pytest test_math_utils.py

Вывод:

============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/jootiee
collected 1 item

test_math_utils.py .                                                     [100%]

============================== 1 passed in 0.03s ===============================


Тестирование — не менее важная часть, чем написание кода.
В процессе разработки отладка кода занимает не меньше времени, чем его написание.
По этой причине каждый специалист обязан владеть умением самостоятельно проверять и отлаживать код.

Чем выше уровень программиста, тем меньше времени у него занимает процесс отладки кода.







Типичные ошибки

Тип ошибки 1: Неправильное имя метода

В тестовом классе ничего не выполняется.

Пример ошибки:

class TestMath(unittest.TestCase):
    def addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)  # Ошибка: метод addition не будет выполнен

Решение:

import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

Перед запуском теста проверяем корректность названий метода.





Тип ошибки 2: Неверное использование assertEqual

Возникает, когда в тесте неверно используем метод assertEqual для проверки значения.

Пример ошибки:

import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 5)  # Ошибка: 2 + 2 не равно 5

Решение:

self.assertEqual(result, 4)  # Исправлено: 2 + 2 == 4

Убедимся, что используем правильные значения при сравнении. Метод assertEqual проверяет, что два аргумента равны.









Тип ошибки 3: Неправильная работа с исключениями

Возникает при неверном использовании метода assertRaises().


import unittest

division = lambda a, b: a / b

class TestMath(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divison(1, 0)) # деление на ноль сразу вызовет исключение

Решение:

import unittest

division = lambda a, b: a / b

class TestMath(unittest.TestCase):
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)  # программа закончит свою работу корректно













Практикум
Задание 1. Проверка корректности вычисления скидок

Ситуация: в магазине действует программа лояльности,
где покупателям предоставляются скидки в зависимости от их уровня в этой программе:
базовый, серебряный и золотой.
Чтобы избежать ошибок в расчётах,
руководство решило опробовать систему с использованием модульного тестирования.

Задача — создать функцию,
которая рассчитает скидку в зависимости от уровня покупателя в программе лояльности и суммы покупки,
и написать тесты с использованием модуля unittest,
чтобы проверить корректность работы функции.

Шаги реализации

Напишем функцию для расчёта скидки:

Аргументы — уровень покупателя (basic, silver, gold) и сумма покупки.

Возвращаемое значение — итоговая сумма после скидки.

def calculate_discount(level, amount):
    if level == "basic":
        return amount * 0.95
    elif level == "silver":
        return amount * 0.90
    elif level == "gold":
        return amount * 0.85
    else:
        raise ValueError("Unknown level")

Напишем тесты с использованием unittest:
Проверим расчёт для каждого уровня.
Проверим наличие некорректного ввода.
Реализация:

import unittest


class TestCalculateDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(calculate_discount("basic", 100), 95.0)

    def test_silver_discount(self):
        self.assertEqual(calculate_discount("silver", 100), 90.0)

    def test_gold_discount(self):
        self.assertEqual(calculate_discount("gold", 100), 85.0)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calculate_discount("platinum", 100)

if __name__ == "__main__":
    unittest.main()


Задание 2. Количество знаков препинания
"""
Windows ()

:: Создание папки проекта
mkdir punctuation_project
cd punctuation_project

:: Создание виртуального окружения
python -m venv venv

:: Активация ()
source venv/Scripts/activate


:: Установка pytest
python -m pip install --upgrade pip
pip install pytest

:: Запуск тестов
pytest


Mac/Linux
bash
# Создание папки проекта
mkdir punctuation_project
cd punctuation_project

# Создание виртуального окружения
python3 -m venv venv

# Активация
source venv/bin/activate

# Установка pytest
pip install pytest

# Запуск тестов
pytest
"""

Ситуация: коллега написал часть программы, которая работает с текстом.
Задача функции, которую нам передали, — вычислять количество знаков препинания в полученной строке.
Ниже представлена её реализация:

def count_punct_marks(string: str) -> int:
    total_count = 0
    for sym in ",.::'":
        total_count += string.count(sym)
    return total_count

Задача — проверить, верно ли работает функция, и в случае найденных ошибок исправить их. Для поиска ошибок использовать pytest.

Шаги реализации

Напишем тесты, покрывающие все возможные ошибки.
В случае обнаружения ошибок исправим их. Каждое исправление поясним комментарием.
Реализация:

# test_module.py
import pytest


def count_punct_marks(string: str) -> int:
    total_count = 0
    for sym in ",.::'":
        total_count += string.count(sym)
    return total_count


def test_empty_string():
   assert count_punct_marks("") == 0

def test_no_punctuation():
    assert count_punct_marks("Hello World") == 0

def test_single_punctuation():
    assert count_punct_marks("Hello World!") == 1

def test_multiple_punctuation():
    assert count_punct_marks("Hello, World! How are you?") == 3

def test_edge_case():
    assert count_punct_marks("!!!") == 3

def test_all_punctuation():
    assert count_punct_marks(".,:;!?") == 6
Вывод:

collected 6 items

test_math_utils.py ...FFF                                                   [100%]

==================================== FAILURES =====================================
____________________________ test_multiple_punctuation ____________________________

    def test_multiple_punctuation():
>       assert count_punct_marks("Hello, World! How are you?") == 3
E       AssertionError: assert 1 == 3
E        +  where 1 = count_punct_marks('Hello, World! How are you?')

test_math_utils.py:21: AssertionError
_________________________________ test_edge_case __________________________________

    def test_edge_case():
>       assert count_punct_marks("!!!") == 3
E       AssertionError: assert 0 == 3
E        +  where 0 = count_punct_marks('!!!')

test_math_utils.py:24: AssertionError
______________________________ test_all_punctuation _______________________________

    def test_all_punctuation():
>       assert count_punct_marks(".,:;!?") == 6
E       AssertionError: assert 4 == 6
E        +  where 4 = count_punct_marks('.,:;!?')

test_math_utils.py:27: AssertionError
============================= short test summary info =============================
FAILED test_math_utils.py::test_multiple_punctuation - AssertionError: assert 1 == 3
FAILED test_math_utils.py::test_edge_case - AssertionError: assert 0 == 3
FAILED test_math_utils.py::test_all_punctuation - AssertionError: assert 4 == 6
=========================== 3 failed, 3 passed in 0.13s ===========================

Функция выводит неверный результат в 3/6 тестов. Видимо, она проверяет не все знаки препинания. Отредактируем функцию:

import string

def count_punct_marks(string: str) -> int:
    total_count = 0
    for sym in string.punctuation:  # используем стандартный набор знаков препинания
        total_count += string.count(sym)
    return total_count


Проверим после изменений:

collected 6 items

test_math_utils.py ......                                                   [100%]

================================ 6 passed in 0.03s ================================


"""
Сначала деактивируйте окружение (если оно активно):
deactivate

Затем удалите папку виртуального окружения:
Для Windows в Git Bash/MINGW64 или Mac/Linux
rm -rf venv

"""