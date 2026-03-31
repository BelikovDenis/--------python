Сегодня мы рассмотрим два популярных формата для хранения данных — CSV и JSON.

Это фундаментальные навыки, которые понадобятся в разработке веб-приложений,
аналитике данных и создании API — Application Programming Interface — интерфейса для управления приложениями.

API позволяет нескольким приложениям взаимодействовать между собой путём передачи данных друг другу,
зачастую — путём передачи информации в формате JSON.

Мы научимся работать с этими форматами, считывать данные из файлов и записывать их обратно,
а также преобразовывать их в нужный формат для дальнейшей работы.


На занятии мы:

разберёмся в особенностях и ограничениях этих форматов;
проанализируем, что такое формат CSV и когда его использовать;
узнаем, как работать с CSV-файлами с помощью библиотеки csv;
изучим формат JSON и его популярность в веб-разработке;
научимся работать с JSON в Python с использованием библиотеки json.



Глоссарий ко второму занятию
CSV (Значения, разделённые запятыми)

CSV (Comma-Separated Values) — это текстовый формат для представления табличных данных.
Каждая строка этого файла является строкой таблицы, а значения столбцов разделяются запятыми.

JSON (Обозначение объектов в JavaScript)

JSON (JavaScript Object Notation) — текстовый формат обмена данными.
Изначально применялся в JavaScript, но теперь активно используется во всех языках программирования.
Файлы этого формата могут хранить структуру данных.

Serialization (Преобразование данных)

Serialization — процесс преобразования данных в формат для хранения или передачи.

Deserialization (Обратное преобразование)

Deserialization — обратный процесс преобразования формата в объекты.

Delimeter (Разделитель)

Delimeter — разделитель, обычно употребляется в контексте разделителя символов в предложении,
разделитель в данных.



Очень часто в программировании случаются ситуации,
когда нужно сохранить данные и передать их куда-то дальше.
Например, в другое приложение через API, которое было упомянуто ранее,
или просто восстановить данные, полученные при прошлом запуске программы.
Для этого и используются форматы JSON и CSV.



В чём же разница между ними?

JSON — формат, который чаще всего используется для хранения структур.
Например, именно в формате JSON браузер отправляет запросы для получения доступа к веб-страницам.

Пример JSON-запроса:

{
    "value": "Иванов Виктор",
    "unrestricted_value": "Иванов Виктор",
    "data": {
        "surname": "Иванов",
        "name": "Виктор",
        "patronymic": null,
        "gender": "MALE"
    }
}

Такой запрос может быть отправлен, к примеру, когда мы заполняем поле для регистрации на сайте.





Формат CSV больше напоминает таблицу и используется в случае,
когда необходимо хранить большое количество данных.

Формат CSV
CSV (Comma-Separated Values) — это текстовый формат,
в котором данные разделяются запятыми (или другим символом-разделителем).
Он широко используется для обмена табличными данными,
такими как таблицы из Excel или экспортированные из баз данных.

Пример CSV-файла:

Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago

Отметим, что если такой файл открыть через блокнот,
то вид будет именно таким образом — значения через запятую.
А если же открыть через Excel, то такой формат откроется как обычная таблица.


Чтение данных из CSV-файла:

import csv

with open('output.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)
    print("Все данные:", data)


"""
import csv
import os

file_path = 'output.csv'

try:
    # Проверка существования файла
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    
    # Проверка размера файла
    if os.path.getsize(file_path) == 0:
        print("Файл пуст")
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Чтение и вывод данных
            for line_num, row in enumerate(reader, 1):
                print(f"Строка {line_num}: {row}")
                
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except PermissionError:
    print("Ошибка: Нет прав для чтения файла")
except UnicodeDecodeError:
    print("Ошибка: Проблемы с кодировкой файла. Попробуйте другую кодировку.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
"""


Давайте разберём аргументы, которые мы передаём в open:

data.csv — файл, который мы хотим открыть;

r — метод, по которому хотим открыть, в данном случае — для чтения (read);

encoding='utf-8' — кодировка файла.




Запись данных в CSV-файл:

import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

Здесь обратим внимание на параметр newline.
Он нужен, чтобы избежать пустых строк при записи.



Формат JSON
Теперь рассмотрим другой формат — JSON.
В отличие от CSV, чаще всего он используется,
когда нам нужно передать какие-то небольшие и/или структурированные данные.

JSON-объект — это неупорядоченное множество пар «ключ:значение».
Его структура очень похожа на словарь.
Используется для представления структурированных данных.
Поддерживает различные типы данных: объекты, массивы, строки, числа, булевые значения и null.

Чтение JSON:
открыть файл JSON

import json
import os

file_path = 'example.json'

try:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    print("Данные успешно загружены:")
    print(json.dumps(data, ensure_ascii=False, indent=2))

except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования JSON: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

Заметим, что метод load библиотеки json возвращает уже знакомый нам словарь:

print(type(data))
# <class 'dict'>

Теперь сохраним уже существующий словарь в файл:


import json

data = {
    "Name": "Alice",
    "Age": 30,
    "Skills": ["Python", "Data Analysis"]
}
with open('example.json', mode='w', encoding='utf-8') as file:
    json.dump(obj=data,
              fp=file,
              indent=4
    )
example.json:

{
    "Name": "Alice",
    "Age": 30,
    "Skills": [
        "Python",
        "Data Analysis"
    ]
}






Параметры json.dump

obj — объект, который хотим записать в файл;

fp — в какой файл записываем;

indent — отступ в файле, количество пробелов;

ensure_ascii управляет тем, как сериализуются не-ASCII символы (например, кириллица, иероглифы или акценты):

ensure_ascii=True — все не-ASCII символы преобразуются в escape-последовательности Unicode (например, \u041f вместо П);

ensure_ascii=False — не-ASCII символы записываются как есть, в их естественном виде (например, П).


Также существует метод json.dumps, который преобразует словарь в строку синтаксиса JSON.
Эти строки мы будем использовать позднее, когда познакомимся со сторонней библиотекой requests.

Пример использования:

import json

data = {
    "Name": "Alice",
    "Age": 30,
    "Skills": ["Python", "Data Analysis"]
}

json_string = json.dumps(data, indent=4)
print(json_string)
# {
#     "Name": "Alice",
#     "Age": 30,
#     "Skills": [
#         "Python",
#         "Data Analysis"
#     ]
# }






Сравнение форматов CSV и JSON
https://top-academy.site/wp-content/uploads/2025/01/Screenshot_2.jpg







Типичные ошибки

Тип ошибки 1: Ошибка в кодировке при чтении файла

Возникает, когда мы не указываем кодировку при чтении файла.

Пример ошибки:

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        row

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)


Решение:

указываем в параметрах функции reader encoding='utf-8'.







Тип ошибки 2: Символы кириллицы сохраняются в виде escape-последовательностей

Ошибка возникает, когда мы пытаемся записать в JSON-файл словарь,
содержащий кириллицу или другие не-ASCII символы.

Пример ошибки:

data = {
    "Имя": "Андрей",
    "Возраст": 30,
    "Умения": [
            "Python",
            "Data Analysis"
    ]
}
print(json.dumps(data, indent=4))
# {
#     "\u0418\u043c\u044f": "\u0410\u043d\u0434\u0440\u0435\u0439",
#     "\u0412\u043e\u0437\u0440\u0430\u0441\u0442": 30,
#     "\u0423\u043c\u0435\u043d\u0438\u044f": [
#         "Python",
#         "Data Analysis"
#     ]
# }

Решение:

указываем параметр ensure_ascii=False

print(json.dumps(data, indent=4, ensure_ascii=False))
# {
#     "Имя": "Андрей",
#     "Возраст": 30,
#     "Умения": [
#         "Python",
#         "Data Analysis"
#     ]
# }





Практикум
Задание 1. Анализ продаж

Ситуация: мы работаем в отделе аналитики и получаем CSV-файл с данными о продажах за месяц.
Каждый ряд содержит следующую информацию: наименование товара, количество проданных единиц и цену за единицу.

Задача — необходимо вычислить общий доход для каждого товара и общий доход за месяц.

Реализуем функцию analyze_sales(file_path), которая:

Читает данные из CSV-файла.
Вычисляет общий доход для каждого товара (количество × цена).
Возвращает итоговый доход за месяц.
Пример CSV-файла:

product,quantity,price
Laptop,5,1000
Smartphone,10,500
Tablet,7,300
Шаги реализации:

Откроем CSV-файл для чтения.
Прочитаем данные с использованием модуля CSV.
Для каждого ряда рассчитаем доход (количество × цена) и добавим его к итоговому.
Вернём общий доход.
Реализация:

import csv

def analyze_sales(file_path):
    total_revenue = 0

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_revenue += quantity * price

    return total_revenue









Задание 2. Формирование отчёта

Ситуация: мы работаем в IT-компании, и нам нужно обработать данные с задачами сотрудников.
Данные хранятся в JSON-файле, где каждая задача содержит название, исполнителя и статус (выполнено или нет).

Задача — необходимо сформировать отчёт, в котором указано, сколько задач выполнил каждый сотрудник.

Реализуем функцию generate_report(json_file_path), которая:

Читает данные из JSON-файла.
Подсчитывает количество выполненных задач для каждого сотрудника.
Возвращает отчёт в виде словаря.
Пример JSON-файла:

[
    {"task": "Fix bugs", "assignee": "Anna", "status": "completed"},
    {"task": "Develop feature", "assignee": "Boris", "status": "in progress"},
    {"task": "Code review", "assignee": "Anna", "status": "completed"},
    {"task": "Write tests", "assignee": "Victoria", "status": "completed"}
]
Шаги реализации:

Откроем JSON-файл и загрузим данные с использованием модуля JSON.
Пройдём по списку задач и подсчитаем выполненные задачи для каждого сотрудника.
Вернём итоговый отчёт.
Реализация:

import json
from collections import defaultdict

def generate_report(json_file_path):
    report = defaultdict(int)

    with open(json_file_path, mode='r') as file:
        tasks = json.load(file)
        for task in tasks:
            if task['status'] == 'completed':
                report[task['assignee']] += 1

    return dict(report)