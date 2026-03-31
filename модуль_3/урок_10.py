При работе с базами данных в Python часто приходится писать SQL-запросы вручную,
что может быть неудобно и затруднять понимание структуры программы.
Object-Relational Mapping (ORM) — это подход,
который позволяет работать с базами данных на уровне объектов,
абстрагируя SQL-запросы и делая код более читаемым и поддерживаемым.


ORM можно представить как переводчика между объектами программы и реляционной базой данных.
Вместо написания SQL-запросов разработчик взаимодействует с базой данных с помощью классов и методов,
что делает код более понятным и интегрированным в объектно-ориентированную архитектуру приложения.


Использование ORM позволяет:

работать с базой данных через Python-классы и объекты,
автоматически генерировать SQL-запросы без необходимости писать их вручную,
упрощать взаимодействие между программой и хранилищем данных,
избегать ошибок, связанных с ручным написанием SQL-кода.






Сегодня мы разберём:

что такое ORM и зачем оно нужно,
как связать объекты Python с базами данных,
как использовать ORM для работы с данными,
как реализовать связь между объектами программы и таблицами базы данных.






Глоссарий к десятому занятию
ORM (Object-Relational Mapping)

ORM — технология, позволяющая взаимодействовать с реляционными базами данных через
объектно-ориентированное программирование без необходимости писать SQL-запросы вручную.

Модель (Model)

Модель — класс в Python, который представляет таблицу базы данных. Атрибуты класса соответствуют столбцам таблицы.

Query (Запрос)

Query — объект, позволяющий выполнять SQL-запросы в ORM.

Связи (Relationships)

Связи — отношения между таблицами в базе данных, представленные через ORM. Например, One-to-Many, Many-to-Many.


Что такое ORM и из чего оно состоит?

Object-Relational Mapping (ORM) — это способ работы с базами данных, 
при котором вместо написания SQL-запросов используются классы и объекты.

Представьте, что у вас есть таблица в базе данных, в которой хранятся пользователи.
Вместо того чтобы каждый раз писать SELECT * FROM users,
вы можете просто вызвать метод .all() у класса User.

ORM используется, когда нужно работать с базами данных на более высоком уровне,
не погружаясь в детали SQL-запросов. Вот несколько случаев, когда ORM особенно полезен:

Когда важно ускорить разработку
Если вы создаёте веб-приложение или бэкенд-сервис,
ORM позволяет быстро работать с базой без написания SQL-запросов вручную.

Например, в Django ORM можно создать пользователя так:

user = User(name="Алиса", age=25)
user.save()  # Сохраняет данные в базу

Это гораздо проще, чем писать INSERT INTO users (name, age) VALUES ('Алиса', 25);.

Когда нужно работать с разными базами данных
Если ваш проект может в будущем переехать с SQLite на PostgreSQL или MySQL,
ORM делает код более универсальным.
Например, SQLAlchemy позволяет легко менять движок базы данных:

engine = create_engine("sqlite:///example.db")  # SQLite
# Или
engine = create_engine("postgresql://user:password@localhost/dbname")  # PostgreSQL

Без ORM пришлось бы менять все SQL-запросы вручную.

Когда код должен быть читабельным и поддерживаемым
Вместо сложных SQL-запросов можно писать понятные объектно-ориентированные вызовы.
Например, поиск пользователя в SQLAlchemy ORM:

user = session.query(User).filter_by(name="Алиса").first()

SQL-версия этого запроса сложнее для восприятия, особенно если запросов много.




Когда важно работать с объектами, а не строками данных
В ORM данные представлены как объекты Python.
Например, user.age сразу даёт доступ к возрасту пользователя,
а без ORM пришлось бы разбирать результат SQL-запроса (row[2]).

Основные компоненты ORM

Рассмотрим ключевые компоненты ORM.

Модель – это класс в Python, который соответствует таблице в базе данных.
Можно сказать, что модель – это «цифровая копия» таблицы,
с которой программа работает как с обычным объектом.

Допустим, у нас есть таблица users, в которой хранятся данные о пользователях:

id	name	age
1	Алиса	25
2	Боб	30

Вместо того чтобы обращаться к этой таблице напрямую через SQL-запросы,
мы создаём класс User, который представляет пользователей как объекты.

Вот простая модель User, которая соответствует таблице users:

class User:
    def __init__(self, id, name, age):
        self.id = id   # Уникальный идентификатор пользователя
        self.name = name  # Имя пользователя
        self.age = age  # Возраст пользователя

Теперь мы можем создать объект пользователя так же, как если бы добавляли строку в таблицу:

user = User(1, "Алиса", 25)
print(user.name)  # Выведет: Алиса
Связи (Relationships) в базе данных

Связи позволяют объединять данные из разных таблиц,
как кусочки головоломки.
Например, если у нас есть таблицы пользователей и заказов,
нам нужно как-то указать, какие заказы принадлежат какому пользователю.

Самый простой способ — добавить в таблицу заказов ссылку (ID) на пользователя.
Это и есть связь «один ко многим» (один пользователь — много заказов).

Создадим таблицы:

import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Таблица пользователей
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Таблица заказов, где каждый заказ связан с пользователем (user_id)
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

Добавим данные в таблицы:

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Добавляем пользователей
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Алиса",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Боб",))
conn.commit()

# Добавляем заказы, указывая user_id
cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (1, "Ноутбук"))
cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (1, "Телефон"))
cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (2, "Часы"))
conn.commit()

conn.close()

Как получить заказы конкретного пользователя?

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Получаем все заказы Алисы (user_id = 1)
cursor.execute("""
SELECT users.name, orders.item
FROM users
JOIN orders ON users.id = orders.user_id
WHERE users.id = ?
""", (1,))

orders = cursor.fetchall()
conn.close()

print(orders)  # [('Алиса', 'Ноутбук'), ('Алиса', 'Телефон')]







Генерация SQL-запросов – как ORM превращает код в SQL?

Когда мы работаем с базой данных вручную через sqlite3,
нам нужно писать SQL-запросы самим.
Например, чтобы найти пользователя по имени, мы бы использовали такой код:

cursor.execute("SELECT * FROM users WHERE name = ?", ("Алиса",))
user = cursor.fetchone()

Но ORM делает это автоматически.
Вместо SQL-запроса мы просто пишем код на Python, а ORM сама превращает его в SQL!

Как это работает в ORM?

Мы пишем понятный код на Python:

session.query(User).filter_by(name="Алиса").first()


2. ORM превращает его в SQL-запрос:

SELECT * FROM users WHERE name = 'Алиса' LIMIT 1;

Нам больше не нужно запоминать SQL-синтаксис!

Другие примеры автоматической генерации SQL

Добавить нового пользователя:

new_user = User(name="Боб", email="bob@example.com")
session.add(new_user)
session.commit()

ORM превращает в SQL:

INSERT INTO users (name, email) VALUES ('Боб', 'bob@example.com');

Обновить данные:

user = session.query(User).filter_by(name="Боб").first()
user.email = "bob_new@example.com"
session.commit()

ORM превращает в SQL:

UPDATE users SET email = 'bob_new@example.com' WHERE name = 'Боб';

Удалить запись:

user = session.query(User).filter_by(name="Боб").first()
session.delete(user)
session.commit()

ORM превращает в SQL:

DELETE FROM users WHERE name = 'Боб';





Использование ORM имеет ряд преимщуеств в сравнении с использованием «чистого» SQL:

ORM упрощает разработку, позволяя работать с базой данных как с объектами Python;
Использование ORM избавляет нас от необходимости писать сложные SQL-запросы;
ORM позволяет работать с базами данных пользователям без знания SQL.

Однако ORM не является универсальным инструментом. К недостаткам ORM можно отнести следующие:

ORM может создать неверный, избыточный или неэффективный запрос.
Написание SQL-запросов вручную повышает контролируемость при работе с базами данных;

ORM не всегда поддерживает все возможности СУБД;
Если код написан с использованием одной ORM,
то переход на другую систему может оказаться проблематичным;

Часто использование ORM приводит к увеличению количества вычислений,
т.к. кроме непосредственно запросов к базе данных добавляются вычисления для преобразования объектов ORM в SQL и обратно.










Типичные ошибки
Тип ошибки 1: Работа с ORM без объявления модели

При использовании ORM (Object-Relational Mapping) данные хранятся в виде объектов,
соответствующих строкам в базе данных. 
Перед тем как работать с данными, необходимо объявить модель, которая описывает структуру таблицы.

Если попытаться создать или запросить объект без объявленной модели, программа выдаст ошибку.

Пример ошибки:

user = User(name="Алиса", age=25)  # Ошибка: класс User не объявлен
session.add(user)
session.commit()

В этом примере предполагается, что существует класс User, 
однако он не был объявлен, из-за чего программа не понимает, как интерпретировать объект User.

Решение:

Перед использованием объекта нужно объявить модель, описав поля таблицы и их свойства:

class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age





Тип ошибки 2: Ошибки в связях между таблицами

При создании связей между таблицами с помощью FOREIGN KEY важно указывать правильные имена полей.
Если внешний ключ (FOREIGN KEY) ссылается на несуществующее поле, это приведет к ошибке при выполнении SQL-запроса.

Пример ошибки:

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(uid)  -- Ошибка: users.uid не существует
)
""")

В этом примере внешний ключ user_id пытается ссылаться на поле users.uid,
но в таблице users такого столбца нет (например, там есть users.id).

Решение:

Необходимо убедиться, что внешний ключ ссылается на существующее поле:

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)  -- Теперь ссылка корректная
)
""")

Также стоит включить поддержку внешних ключей в SQLite перед выполнением запросов:

cursor.execute("PRAGMA foreign_keys = ON;")
Это гарантирует, что SQLite будет проверять целостность данных при работе с внешними ключами.










Практикум
Задача 1: Вставка данных в таблицу с помощью ORM

Ситуация:
Вы получили исходный код ORM, 
которую разработали ваши коллеги для обслуживания нужд компании-заказчика. 
Вам нужно изучить принцип работы ORM, создать новую таблицу, 
добавить туда несколько строк и вывести на экран все записи.

ORM:

import sqlite3

class SimpleORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, **columns):
        columns_with_types = ', '.join([f'{col} {dtype}' for col, dtype in columns.items()])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {columns_with_types})')
        self.conn.commit()

    def insert(self, table_name, **data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})', tuple(data.values()))
        self.conn.commit()

    def select(self, table_name, **conditions):
        query = f'SELECT * FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, set_data, **conditions):
        set_clause = ', '.join([f'{col} = ?' for col in set_data.keys()])
        query = f'UPDATE {table_name} SET {set_clause}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(list(set_data.values()) + list(conditions.values())))
        else:
            self.cursor.execute(query, tuple(set_data.values()))
        self.conn.commit()

    def delete(self, table_name, **conditions):
        query = f'DELETE FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()



Задача:
Создайте экземпляр ORM и подключитесь к базе данных. 
Затем создайте таблицу «users» со столбцами «name» (текстовый тип данных) и «age» (целочисленный тип данных). 
Добавьте в таблицу несколько строк с указанием имени и возраста пользователей, 
а затем выведите на экран все записи из таблицы.

Шаги реализации:

Создаем экземпляр ORM и подключаемся к базе данных:
orm = SimpleORM('example.db')

Создаем таблицу «users» с колонками «name» и «age»:
orm.create_table('users', name='TEXT', age='INTEGER')

Вставляем данные в таблицу:
orm.insert('users', name='Alice', age=30)
orm.insert('users', name='Bob', age=25)

Выводим на экран все записи из таблицы:
print(orm.select('users'))


Реализация
import sqlite3

class SimpleORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, **columns):
        columns_with_types = ', '.join([f'{col} {dtype}' for col, dtype in columns.items()])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {columns_with_types})')
        self.conn.commit()

    def insert(self, table_name, **data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})', tuple(data.values()))
        self.conn.commit()

    def select(self, table_name, **conditions):
        query = f'SELECT * FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, set_data, **conditions):
        set_clause = ', '.join([f'{col} = ?' for col in set_data.keys()])
        query = f'UPDATE {table_name} SET {set_clause}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(list(set_data.values()) + list(conditions.values())))
        else:
            self.cursor.execute(query, tuple(set_data.values()))
        self.conn.commit()

    def delete(self, table_name, **conditions):
        query = f'DELETE FROM {table_name}'
        if conditions:
            query += ' WHERE ' + ' AND '.join([f'{col} = ?' for col in conditions.keys()])
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# Использование ORM согласно заданию
orm = SimpleORM('example.db')
orm.create_table('users', name='TEXT', age='INTEGER')
orm.insert('users', name='Alice', age=30)
orm.insert('users', name='Bob', age=25)
print(orm.select('users'))









Итоги:
Сегодня мы научились:

создавать и использовать модели для работы с базой данных
добавлять, изменять и удалять данные через ORM
настраивать связи между таблицами
анализировать, как ORM преобразует Python-код в SQL-запросы