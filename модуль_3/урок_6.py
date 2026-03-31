Мы уже научились работать с запросами, 
извлекать данные из таблиц и фильтровать результаты. 
Все эти действия мы проводили в отдельных таблицах. 
Однако базы данных позволяют хранить информацию в разных таблицах, 
связанных между собой с помощью внешних ключей.

Внешними ключами называются поля таблиц, 
которые указывают на связанные записи в других таблицах. 
С помощью внешних ключей мы можем объединять данные из нескольких таблиц.

Например, если у нас есть таблица пользователей и их заказов, 
с помощью внешнего ключа мы можем увидеть, 
какие заказы делал конкретный пользователь.


В таких случаях используются многотабличные запросы — это запросы, 
которые позволяют работать с данными из нескольких таблиц, связывая их между собой.

Зачем разбивать данные на несколько таблиц?

Распределение данных между таблицами называется нормализацией. 
Это процесс, который позволяет:

устранить повторения (например, 
имя пользователя можно записать один раз в таблице «Пользователи», 
не дублируя его каждый раз в таблице «Заказы» с нужной ссылкой);
обеспечить целостность данных (например, 
мы можем изменить email пользователя в таблице «Пользователи», 
и эта информация автоматически отразится во всех связанных данных);
упростить управление базой и улучшить схему представления данных.


Для эффективной работы с подобными структурами 
используются различные типы соединений таблиц (JOINs).

Кроме того, при использовании многотабличных запросов часто применяются операции с множествами. 
Например, в таблице с заказами пользователей с их помощью можно:

найти заказы, которые были сделаны пользователями из определенной группы;
вывести список пользователей, у которых нет заказов;
объединить данные из нескольких таблиц, исключив дубликаты.
Сегодня мы научимся:

использовать различные типы соединений (INNER JOIN, LEFT JOIN);
объединять таблицы и извлекать данные из нескольких источников;
выбирать данные (даже если они находятся в разных таблицах);
выполнять операции с множествами.









Глоссарий к шестому занятию
JOIN (Объединение)
JOIN — операция в SQL, 
которая позволяет объединять строки из двух или более таблиц на основе связанного поля.

INNER JOIN (Внутреннее объединение)
INNER JOIN — тип соединения, 
который возвращает только строки, которые совпадают в обеих таблицах.

LEFT JOIN (Левое объединение)
LEFT JOIN — тип соединения, 
который возвращает все строки из левой таблицы и соответствующие строки из правой.

RIGHT JOIN (Правое объединение)
RIGHT JOIN — тип соединения, 
который возвращает все строки из правой таблицы и соответствующие строки из левой.

FULL JOIN (Полное объединение)
FULL JOIN — тип соединения, 
который возвращает все строки из обеих таблиц, заполняя отсутствующие значения NULL.

Normalization (Нормализация)
Normalization — процесс организации информации в базе данных, 
предполагающий разделение данных на несколько таблиц и установление
 связей между ними с целью уменьшить избыточность и повысить целостность данных.

FOREIGN KEY (Внешний ключ)
FOREIGN KEY — это столбец или набор столбцов, 
ссылающийся на первичный ключ другой таблицы. 
Внешний ключ используется для установления связи между таблицами.






Многотабличные запросы — это запросы, использующие данные из нескольких таблиц в базе данных.

Представьте, что у вас есть гардероб, 
где одежда разложена по разным шкафам: рубашки в одном, 
брюки в другом, обувь в третьем. 
Такая организация помогает поддерживать порядок и быстрее находить нужные вещи. 
Точно так же в базах данных: 
информация распределяется по разным таблицам для удобства хранения, 
обновления и обработки.



Многотабличные запросы в SQL позволяют объединять данные из нескольких таблиц
 с использованием общих полей. 
 Это полезно, когда информация распределена между разными таблицами 
 и необходимо получить целостное представление о данных, 
 например соединить данные о клиентах и их заказах.

Базы данных позволяют создавать разные таблицы, 
но как их связать? Для этого требуется внешний ключ.


Внешний ключ — это идентификатор, 
который используется для соотнесения данных разных таблиц посредством ссылок.

Пример структуры базы данных

Вместо того чтобы хранить все данные в одной таблице, 
мы разбиваем их на связанные друг с другом таблицы. 
Это можно сравнить с хранением одежды. 
Мы раскладываем брюки и рубашки по разным шкафам для удобства,
 но, когда одеваемся, объединяем комплекты в единый образ.

Предположим, у нас есть две таблицы.

«Пользователи» (users):
id (уникальный идентификатор пользователя),
name (имя пользователя),
email (электронная почта пользователя).
«Заказы» (orders):

id (уникальный идентификатор заказа),
user_id (внешний ключ, указывающий на id пользователя из таблицы «Пользователи»),
order_date (дата заказа),
amount (сумма заказа).

Здесь связь между таблицами осуществляется через поле user_id, 
которое является внешним ключом и указывает, кто именно совершил заказ.




Пример работы с многотабличными запросами

Создадим две таблицы:

employees (сотрудники), которая содержит информацию о работниках, 
включая идентификатор отдела (наш внешний ключ);
departments (отделы), в которой хранятся данные об отделах компании.
-- Создание таблицы сотрудников

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER
);

-- Создание таблицы отделов
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);




import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Создаем таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
)
''')

# Добавляем данные в таблицы
departments_data = [
    (1, 'ИТ'),
    (2, 'Маркетинг'),
    (3, 'Финансы')
]

employees_data = [
    (1, 'Алексей Иванов', 1),
    (2, 'Мария Петрова', 2),
    (3, 'Иван Сидоров', 1),
    (4, 'Елена Козлова', None)  # Сотрудник без отдела
]

cursor.executemany('INSERT OR IGNORE INTO departments VALUES (?, ?)', departments_data)
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?, ?, ?)', employees_data)
conn.commit()

# Примеры многотабличных запросов
print("1. Все сотрудники с названиями отделов:")
cursor.execute('''
SELECT e.name, d.department_name 
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
''')
for row in cursor.fetchall():
    print(row)

print("\n2. Отделы с количеством сотрудников:")
cursor.execute('''
SELECT d.department_name, COUNT(e.id) as employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
''')
for row in cursor.fetchall():
    print(row)

print("\n3. Сотрудники без отдела:")
cursor.execute('''
SELECT name FROM employees 
WHERE department_id IS NULL
''')
for row in cursor.fetchall():
    print(row[0])

# Закрываем соединение
conn.close()



Как работает внешний ключ в созданных таблицах:

В таблице employees столбец department_id ссылается на столбец department_id в таблице departments.
Это означает, что мы не сможем добавить сотрудника в employees, 
если в таблице departments нет такого отдела с соответствующим department_id.
Заполним таблицы тестовыми данными:

-- Вставка данных в таблицу сотрудников
INSERT INTO employees (id, name, department_id)
VALUES (1, 'Alice', 1),
       (2, 'Bob', 2),
       (3, 'Charlie', 3);

-- Вставка данных в таблицу отделов
INSERT INTO departments (department_id, department_name)
VALUES (1, 'HR'),
       (2, 'IT'),
       (4, 'Sales');
Теперь у нас есть две заполненные таблицы, которые можно связать между собой.




Типы соединений (JOIN)

Для соединения таблиц используются операции JOIN. 
Они позволяют связывать строки из разных таблиц на основе общих значений.

INNER JOIN возвращает только те строки, 
у которых есть соответствия в обеих таблицах. 
Если в одной из таблиц нет соответствующих записей, они исключаются из результата.

Пример: необходимо получить список сотрудников и их отделов.

SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;


Пояснение:

Alice и Bob присутствуют в employees и имеют соответствия в departments.
Charlie не попал в результат, так как его department_id = 3, 
а в departments нет отдела с department_id = 3.



LEFT JOIN возвращает все строки из левой таблицы (employees), 
даже если в правой таблице (departments) нет соответствий. 
Если соответствий нет, столбцы из правой таблицы заполняются NULL.

Пример: необходимо получить данные обо всех сотрудниках и их отделах, включая тех, у кого отдел не указан.

SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;


Пояснение:

Alice и Bob попали в результат с названиями их отделов.
Charlie тоже попал в результат, но у него NULL, 
так как в departments нет отдела с department_id = 3.



RIGHT JOIN работает наоборот: он возвращает все строки из правой таблицы (departments), 
а также строки из левой таблицы (employees), которые имеют соответствия.

Пример: необходимо получить данные по всем отделам и сотрудникам, если они там есть.

SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.department_id;


Пояснение:

Alice и Bob попали в результат с названиями их отделов.
Sales попал в результат, но сотрудников там нет, поэтому в name значение NULL.





FULL JOIN возвращает все строки из обеих таблиц. Если соответствий нет, возвращается NULL.

Пример: необходимо получить данные по всем сотрудникам и отделам, 
даже если у них нет соответствий.

SELECT employees.name, departments.department_name
FROM employees
FULL JOIN departments ON employees.department_id = departments.department_id;


Пояснение:

Alice и Bob попали в результат с названиями их отделов.
Charlie попал в результат, но у него NULL, потому что в departments нет соответствующего отдела.
Sales попал в результат, но у него NULL, 
так как в employees нет сотрудников, работающих в этом отделе.







Сферы применения:

INNER JOIN используется, когда нужно получить только совпадающие строки.
LEFT JOIN подходит, когда важны все строки из первой таблицы, 
даже если нет соответствий во второй.


Операции со множествами

UNION

Оператор UNION объединяет результаты двух или более запросов, удаляя дубликаты строк.

SELECT column_name FROM table1
UNION
SELECT column_name FROM table2;


Предположим, мы хотим получить список всех уникальных имён сотрудников и названий отделов:

-- Список всех имён сотрудников и названий отделов
SELECT name FROM employees
UNION
SELECT department_name FROM departments;

Этот запрос вернёт все уникальные имена сотрудников из таблицы employees 
и все уникальные названия отделов из таблицы departments.



Различия между JOIN и UNION

Оба оператора используются для работы с несколькими таблицами, 
но принцип их действия разный:

JOIN объединяет таблицы по общим полям, 
добавляя недостающие столбцы. 
Это похоже на соединение двух частей пазла: одна деталь дополняет другую.

UNION объединяет строки по одинаковым столбцам, 
добавляя данные друг под друга. 
Это похоже на складывание одинаковых стопок бумаги в одну.




EXCEPT — разность множеств

Оператор EXCEPT возвращает строки, 
которые есть в первом запросе, но отсутствуют во втором. 
Эта процедура называется разностью множеств.

Предположим, мы хотим получить список сотрудников, 
чьи имена не совпадают с названием отдела (например, 
мы исключаем сотрудников, чьи имена совпадают с названием отдела):

-- Список сотрудников, чьи имена не совпадают с названиями отделов
SELECT name FROM employees
EXCEPT
SELECT department_name FROM departments;

Этот запрос вернёт имена сотрудников, 
которых нет в списке отделов (то есть исключит имена, 
совпадающие с названиями отделов).

Мы научились связывать данные из 
нескольких таблиц с помощью операций INNER JOIN и LEFT JOIN, 
а еще изучили операции со множествами для работы с результатами нескольких запросов. 
Перейдем к практике, 
чтобы научиться задействовать эти операции на реальных данных.










Типичные ошибки
Тип ошибки 1: Пропущенное условие соединения

Ошибка возникает, когда в запросе при использовании JOIN не указано условие, 
по которому нужно соединять таблицы. 
SQL попытается объединить каждую отдельную строку 
из одной таблицы с каждой строкой из другой. 
В результате это приведет к огромному числу лишних строк.

Пример ошибки:

SELECT Customers.name, Orders.order_id
FROM Customers JOIN Orders;

В этом запросе мы не указали, 
по какому признаку нужно объединять таблицы Customers и Orders, 
и SQL соединит все строки первой таблицы со строками второй. 
Мы получим множество строк и ошибки в данных.

Решение:

Следует добавить условие ON, определяющее, 
какие строки из первой таблицы нужно соединить со
 строками из второй таблицы. Например, 
 можно соединять строки по полю customer_id:

SELECT Customers.name, Orders.order_id
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;

Теперь мы указали конкретно, 
что строки из таблицы Customers должны соединяться с строками из таблицы Orders, 
где значения customer_id в обеих таблицах совпадают.





Тип ошибки 2: JOIN без явного указания таблицы

Ошибка возникает, 
когда в запросе используются столбцы с одинаковыми именами из разных таблиц. 
SQL не может понять, к какой из таблиц относится каждый из этих столбцов.

Это часто происходит при объединении таблиц с помощью JOIN, 
когда в обеих таблицах есть одинаковые названия столбцов:
 например, id, customer_id и другие.

Пример ошибки:

SELECT name, order_id
FROM Customers
JOIN Orders ON customer_id = customer_id;

В этом запросе столбец customer_id используется в обеих таблицах: 
Customers и Orders. Однако в SQL не указано, 
из какой таблицы следует брать данный столбец. Это вызывает конфликт в работе СУБД.

Решение:

Необходимо указывать конкретное имя таблицы перед каждым столбцом:

SELECT Customers.name, Orders.order_id
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;














Практикум
Задача 1: Объединение данных из двух таблиц с помощью JOIN в SQLite

Ситуация:
Вам необходимо работать с базой данных интернет-магазина, 
содержащей информацию о клиентах и их заказах. 
Требуется получить список клиентов вместе с их заказами, 
а также учесть клиентов, у которых пока нет заказов.

Задача:
Создайте две таблицы: Customers (для хранения данных о клиентах) 
и Orders (для хранения данных о заказах). 
Добавьте тестовые данные о клиентах и их заказах. 
Используйте INNER JOIN, чтобы получить список клиентов, 
которые сделали заказы, и LEFT JOIN, 
чтобы показать всех клиентов, включая тех, у кого нет заказов. 
Проверьте результаты выполнения запросов.

Шаги реализации:

Создание таблиц для хранения данных о клиентах и заказах:

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate TEXT,
    Amount REAL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

Добавление данных о клиентах:

INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
VALUES
(1, 'Alice', 'Smith', 'alice@example.com'),
(2, 'Bob', 'Johnson', 'bob@example.com'),
(3, 'Charlie', 'Brown', 'charlie@example.com');

Добавление данных о заказах:

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Amount)
VALUES
(101, 1, '2025-02-01', 150.00),
(102, 1, '2025-02-02', 200.00),
(103, 2, '2025-02-03', 50.00);

Использование INNER JOIN для получения клиентов, которые сделали заказы:

SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.Amount
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;


Реализация

import sqlite3

def create_tables(cursor):
    """Создание таблиц Customers и Orders"""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        OrderDate TEXT,
        Amount REAL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
    ''')

def insert_data(cursor):
    """Добавление тестовых данных"""
    # Добавляем клиентов
    customers_data = [
        (1, 'Alice', 'Smith', 'alice@example.com'),
        (2, 'Bob', 'Johnson', 'bob@example.com'),
        (3, 'Charlie', 'Brown', 'charlie@example.com')
    ]
    
    orders_data = [
        (101, 1, '2025-02-01', 150.00),
        (102, 1, '2025-02-02', 200.00),
        (103, 2, '2025-02-03', 50.00)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO Customers VALUES (?, ?, ?, ?)', customers_data)
    cursor.executemany('INSERT OR IGNORE INTO Orders VALUES (?, ?, ?, ?)', orders_data)

def inner_join_example(cursor):
    """INNER JOIN - только клиенты с заказами"""
    print("INNER JOIN - клиенты с заказами:")
    print("-" * 50)
    
    cursor.execute('''
    SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, 
           Orders.OrderID, Orders.OrderDate, Orders.Amount
    FROM Customers
    INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    ''')
    
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Имя: {row[1]} {row[2]}, "
              f"Заказ №{row[3]}, Дата: {row[4]}, Сумма: ${row[5]:.2f}")
    
    print(f"Всего клиентов с заказами: {len(results)}")
    return results

def left_join_example(cursor):
    """LEFT JOIN - все клиенты, включая тех без заказов"""
    print("LEFT JOIN - все клиенты:")
    print("-" * 50)
    
    cursor.execute('''
    SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, 
           Orders.OrderID, Orders.OrderDate, Orders.Amount
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    ORDER BY Customers.CustomerID
    ''')
    
    results = cursor.fetchall()
    for row in results:
        if row[3] is not None:  # Есть заказ
            print(f"ID: {row[0]}, Имя: {row[1]} {row[2]}, "
                  f"Заказ №{row[3]}, Дата: {row[4]}, Сумма: ${row[5]:.2f}")
        else:  # Нет заказов
            print(f"ID: {row[0]}, Имя: {row[1]} {row[2]}, "
                  f"Заказы: нет")
    
    return results

def additional_queries(cursor):
    """Дополнительные аналитические запросы"""
    print("ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ")
    print("=" * 50)
    
    # 1. Общая сумма заказов по клиентам
    print("1. Общая сумма заказов по клиентам:")
    cursor.execute('''
    SELECT c.CustomerID, c.FirstName, c.LastName, 
           COALESCE(SUM(o.Amount), 0) as TotalAmount,
           COUNT(o.OrderID) as OrderCount
    FROM Customers c
    LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY c.CustomerID
    ORDER BY TotalAmount DESC
    ''')
    
    for row in cursor.fetchall():
        status = "активный" if row[3] > 0 else "без заказов"
        print(f"Клиент: {row[1]} {row[2]}, "
              f"Заказов: {row[4]}, "
              f"Общая сумма: ${row[3]:.2f} ({status})")
    
    # 2. Клиенты без заказов
    print("2. Клиенты без заказов:")
    cursor.execute('''
    SELECT c.CustomerID, c.FirstName, c.LastName, c.Email
    FROM Customers c
    LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
    WHERE o.OrderID IS NULL
    ''')
    
    no_orders = cursor.fetchall()
    if no_orders:
        for row in no_orders:
            print(f"ID: {row[0]}, Имя: {row[1]} {row[2]}, Email: {row[3]}")
    else:
        print("Все клиенты сделали хотя бы один заказ")

def main():
    """Основная функция"""
    # Подключение к базе данных
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    try:
        # Создание таблиц и вставка данных
        create_tables(cursor)
        insert_data(cursor)
        conn.commit()
        
        print("БАЗА ДАННЫХ ИНТЕРНЕТ-МАГАЗИНА")
        print("=" * 60)
        
        # Выполнение JOIN запросов
        inner_results = inner_join_example(cursor)
        left_results = left_join_example(cursor)
        
        # Дополнительные аналитические запросы
        additional_queries(cursor)
        
        # Вывод статистики
        print("СТАТИСТИКА")
        print("-" * 30)
        print(f"Всего клиентов в базе: 3")
        print(f"Клиентов с заказами (INNER JOIN): {len(inner_results)}")
        print(f"Всего записей в LEFT JOIN: {len(left_results)}")
        
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        # Закрытие соединения
        conn.close()
        print("Соединение с базой данных закрыто")

if __name__ == "__main__":
    main()











Итоги:
Сегодня мы научились:

работать с внешними ключами, чтобы связывать данные между таблицами;
использовать JOIN-операции: 
применять INNER JOIN, LEFT JOIN, RIGHT JOIN и FULL JOIN для объединения данных;
оперировать множествами: использовать UNION, EXCEPT и понимать разницу между ними и JOIN.