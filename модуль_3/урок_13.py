Мы изучили основополагающие принципы объектно-ориентированного программирования (ООП) 
– инкапсуляцию и наследование – на примере разработки ORM (Object-Relational Mapping).

Сегодня мы продолжим изучать продвинутое ООП и познакомимся с принципом полиморфизма.
Также мы рассмотрим использование декораторов в ООП и их использование в ORM. Разберём:

что такое полиморфизм в ООП,
как создавать и применять декораторы при разработке ORM.





Глоссарий к тринадцатому занятию
Полиморфизм (Polymorphism)
Полиморфизм – принцип ООП,
позволяющий использовать один и тот же интерфейс для работы с разными типами объектов.
В Python реализуется через переопределение методов, утиную типизацию и абстрактные классы.

Утиная типизация (Duck Typing)
Утиная типизация – концепция, при которой тип объекта определяется не его классом,
а наличием нужных методов и свойств («Если что-то крякает как утка, то это утка»).

Абстрактный класс (Abstract Type)
Абстрактный класс – класс, который не предназначен для создания экземпляров,
а служит шаблоном для других классов.
Содержит абстрактные методы (@abstractmethod), которые должны быть переопределены в дочерних классах.

Декоратор (Decorator)
Декоратор – функция (или класс),
которая изменяет поведение другой функции или метода без изменения её исходного кода.
Синтаксис: @decorator_name.

Функция-обёртка (Wrapper)
Функция-обёртка – внутренняя функция в декораторе,
которая добавляет новую логику вокруг вызова исходной функции (например, логирование или кеширование).





Что такое полиморфизм?

Полиморфизм — это одна из ключевых концепций объектно-ориентированного программирования,
которая позволяет использовать один и тот же объект Python для работы с разными типами данных.
Название «полиморфизм» переводится с греческого как «много форм».

Зачем использовать полиморфизм в ORM?

Гибкость: можно легко добавлять новые типы полей и моделей.
Единообразие: все модели и поля работают по одному принципу.
Масштабируемость: легко добавлять новую функциональность через наследование.
Создаем ORM с использование принципов полиморфизма

Давайте шаг за шагом разберём, как работает ORM (Object-Relational Mapping) с использованием полиморфизма.

Создадим простую ORM, которая будет состоять из:

поля (Field) – отвечает за отдельные колонки в таблице;

модели (Model) – представляет целую таблицу;

метакласса (ModelMeta) – помогает автоматически собирать информацию о полях.

Шаг 1: Создаём класс Field (Поле)

class Field:
    def __init__(self, name, column_type):
        self.name = name  # Название поля (например, "age")
        self.column_type = column_type  # Тип в БД (например, "integer")

    def __str__(self):
        return f"{self.name}:{self.column_type}"

Это базовый класс для всех типов полей.

Каждое поле знает своё имя и тип в базе данных.

Метод __str__ просто возвращает информацию о поле (для отладки).

Пример использования:

age_field = Field("age", "integer")
print(age_field)  # Выведет: age:integer

Шаг 2: Специализированные поля (наследование)

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "integer")  # Вызываем конструктор родителя

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar(255)")

IntegerField и StringField наследуются от Field. Они фиксируют конкретный тип данных для БД. super().__init__ вызывает конструктор родительского класса.

Мы можем использовать любые поля одинаково, несмотря на их разные типы:

age = IntegerField("age")
name = StringField("name")
print(age)  # age:integer
print(name)  # name:varchar(255)

Шаг 3: Метакласс ModelMeta

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs["_fields"] = fields
        return super().__new__(cls, name, bases, attrs)

Метакласс – это «класс для классов», он управляет их созданием.

__new__ вызывается при создании нового класса. Здесь мы собираем все поля класса в словарь _fields.

Как это работает:

Когда мы создаём класс модели (например, User), Python вызывает ModelMeta.__new__.

Мы проверяем все атрибуты класса и находим те, что являются подклассами Field.

Сохраняем эти поля в _fields для дальнейшего использования.

Шаг 4: Базовый класс Model

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        values = []
        for name, field in self._fields.items():
            fields.append(field.name)
            values.append(getattr(self, name, None))

        sql = f"INSERT INTO {self.__class__.__name__.lower()} ({','.join(fields)}) VALUES ({','.join(['%s']*len(values))})"
        print(f"Выполняется SQL: {sql} с параметрами {values}")
metaclass=ModelMeta указывает, что для создания Model используется наш метакласс.

__init__ принимает параметры и устанавливает их как атрибуты.

save() формирует SQL-запрос на основе полей модели.

Шаг 5: Создаём модель User python

class User(Model):
    id = IntegerField("id")
    name = StringField("name")
Интерпретатор видит class User(Model) и понимает, что нужно создать новый класс.

Так как Model имеет метакласс ModelMeta, вызывается ModelMeta.__new__.

ModelMeta находит все поля (id и name) и сохраняет их в User._fields.

Создаётся класс User с этими атрибутами.

Шаг 6: Использование ORM python

# Создаём объект пользователя
user = User(id=1, name="John")

# Сохраняем в "базу данных" (на самом деле просто печатаем SQL)
user.save()




Реализация
# Шаг 1: Создаём класс Field (Поле)
class Field:
    def __init__(self, name, column_type):
        self.name = name  # Название поля (например, "age")
        self.column_type = column_type  # Тип в БД (например, "integer")

    def __str__(self):
        return f"{self.name}:{self.column_type}"


# Шаг 2: Специализированные поля (наследование)
class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "integer")  # Вызываем конструктор родителя


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar(255)")


# Шаг 3: Метакласс ModelMeta
class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs["_fields"] = fields
        return super().__new__(cls, name, bases, attrs)


# Шаг 4: Базовый класс Model
class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        values = []
        for name, field in self._fields.items():
            fields.append(field.name)
            values.append(getattr(self, name, None))

        sql = f"INSERT INTO {self.__class__.__name__.lower()} ({','.join(fields)}) VALUES ({','.join(['%s']*len(values))})"
        print(f"Выполняется SQL: {sql} с параметрами {values}")


# Шаг 5: Создаём модель User
class User(Model):
    id = IntegerField("id")
    name = StringField("name")


# Шаг 6: Использование ORM
if __name__ == "__main__":
    # Пример использования полей
    age_field = Field("age", "integer")
    print(f"Пример поля: {age_field}")  # Выведет: age:integer

    age = IntegerField("age")
    name = StringField("name")
    print(f"IntegerField: {age}")  # age:integer
    print(f"StringField: {name}")  # name:varchar(255)

    # Создаём объект пользователя
    user = User(id=1, name="John")

    # Сохраняем в "базу данных" (на самом деле просто печатаем SQL)
    user.save()
    
    # Дополнительный пример с другим пользователем
    user2 = User(id=2, name="Alice")
    user2.save()




Что выведет программа:

Выполняется SQL: INSERT INTO user (id,name) VALUES (%s,%s) с параметрами [1, 'John']
Как работает полиморфизм в нашей ORM

Мы создали единый интерфейс для разных типов полей:

Классы IntegerField и StringField наследуются от Field, но:
используют общий метод __init__ через super();
переопределяют тип колонки ("integer" vs "varchar(255)").
В коде они используются одинаково (например, id = IntegerField("id") и
         name = StringField("name")), несмотря на разную внутреннюю логику.
Полиморфизм используется при обработке полей в метаклассе ModelMeta:

Метакласс ищет атрибуты-поля через isinstance(value,
    Field) независимо от их конкретного типа (IntegerField или StringField).

Любое поле, которое наследуется от Field, автоматически попадает в _fields.
Формирование SQL-запроса в методе save():


Метод save() работает с любыми полями модели через общий интерфейс:
Извлекает имя поля (field.name) и значение (getattr(self, name)), не зная их конкретного типа.
Поля разных типов (IntegerField, StringField) обрабатываются единообразно при построении SQL.
Наконец, можно добавить новые типы полей (например, BooleanField, DateField), унаследовав их от Field. 
Они автоматически будут поддерживаться ORM без изменения кода в ModelMeta или Model.

Преимущества применения принципов полиморфизма при разработке ORM

Удобство: работаем с объектами, а не с SQL.
Безопасность: ORM сама экранирует значения, предотвращая SQL-инъекции.
Переносимость: код работает с разными СУБД (если расширить ORM).
Поддержка: легко добавлять новую функциональность.
Ограничения нашей ORM

Наша ORM использует базовые средства Python.
В масштабных системах, таких как Django ORM или SQLAlchemy, есть:

поддержка отношений между таблицами (один-ко-многим, многие-ко-многим);

миграции базы данных;

сложные запросы (фильтрация, сортировка, агрегация);

кеширование (механизм временного хранения данных);

оптимизация запросов.

Но даже такая простая реализация показывает,
как полиморфизм помогает создавать расширяемые системы.
Например, мы можем создавать иерархии объектов,
в которых дочерние классы могут добавлять свои поля и методы, сохраняя общий интерфейс.
Так, мы можем сформировать класс User и объекты AdminUser, GuestUser с общими свойствами.

Полиморфизм можно использовать при создании ORM, чтобы:

создавать гибкие и расширяемые системы;

уменьшать дублирование кода;

обеспечивать единообразный интерфейс для работы с разными типами данных;

легко адаптировать систему к изменениям.








Декораторы в контексте ORM

Декоратор — это функция, которая позволяет обернуть,
т. е. добавить новый функционал к существующей функции. В ORM декораторы можно использовать для:

валидации (проверки) данных перед сохранением,

логирования (сохранения истории) SQL-запросов,

кеширования (сохранения во временное хранилище) результатов запросов.

Примеры использования декораторов в ORM

Пример 1: Декоратор для валидации:
def validate_email(func):
    def wrapper(self, *args, **kwargs):
        if hasattr(self, 'email'):
            if '@' not in self.email:
                raise ValueError("Некорректный email")
        return func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, email):
        self.email = email

    @validate_email
    def save(self):
        print(f"Пользователь с email {self.email} сохранён")

# Использование
user = User("alice@example.com")
user.save()  # Пройдёт валидацию

invalid_user = User("invalid-email")
invalid_user.save()  # Вызовет ValueError







Пример 2: Декоратор для логирования SQL:
def log_sql(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняется SQL: {func.__name__}")
        print(f"Аргументы: {args[1:]}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

class Database:
    @log_sql
    def execute(self, query):
        # Здесь была бы реальная логика выполнения SQL
        return f"Результат запроса '{query}'"

# Использование
db = Database()
db.execute("SELECT * FROM users")






Пример 3: Декоратор для кеширования запросов:
def cache_queries(func):
    cache = {}
    def wrapper(self, query):
        if query in cache:
            print("Результат из кеша")
            return cache[query]
        result = func(self, query)
        cache[query] = result
        return result
    return wrapper

class Database:
    @cache_queries
    def execute(self, query):
        print("Выполнение тяжёлого запроса...")
        return f"Результат {query}"

# Использование
db = Database()
print(db.execute("SELECT * FROM users"))  # Выполнит запрос
print(db.execute("SELECT * FROM users"))  # Возьмёт из кеша


Ключевые особенности использования декораторов в ORM:

валидация данных перед сохранением;

прозрачное логирование всех SQL-операций;

эффективное кеширование результатов запросов.


















Типичные ошибки
Тип ошибки 1: Отсутствие общего интерфейса для полиморфных методов

Проблема:
Если разные модели ORM используют разные структуры методов, это усложняет их использование через единый интерфейс.

Пример ошибки:

class User:
    def save(self, validate=True):  # Есть параметр validate
        pass

class Product:
    def save(self):  # Нет параметра validate
        pass

def save_all(models):
    for model in models:
        model.save()  # Ошибка, если передать User(validate=False)


Решение:
Унифицировать интерфейсы или использовать **kwargs, 
который позволяет передавать в функцию произвольное количество именованных аргументов.

class User:
    def save(self, **kwargs):
        validate = kwargs.get("validate", True)
        pass

class Product:
    def save(self, **kwargs):
        pass











Тип ошибки 2: Неправильное применение динамического полиморфизма (например, через __getattr__)

Динамический полиморфизм — это возможность изменять поведение объектов во время выполнения программы. 
В Python он реализуется через:

магические методы (__getattr__, __getattribute__, __setattr__);

динамическое создание атрибутов и методов (например, через setattr);

декораторы (например, @property), которые позволяют управлять доступом к атрибутам.

Проблема:
Динамическое разрешение атрибутов (__getattr__, __getattribute__) может усложнить отладку и привести к неявным ошибкам.

Пример ошибки:

class DynamicModel:
    def __getattr__(self, name):
        print(f"Атрибут {name} не найден, но мы его создали!")
        value = f"Значение для {name}"
        setattr(self, name, value)  # Динамически создаём атрибут
        return value

model = DynamicModel()
print(model.username)  # Атрибут username не найден, но мы его создали!
print(model.username)  # Теперь атрибут существует и возвращает "Значение для username"

Решение:
Использовать явные методы или свойства (@property).

@property — это декоратор, который превращает метод в «вычисляемый атрибут».

Преимущества перед __getattr__:

все атрибуты явно объявлены в коде;
можно добавить валидацию, ленивые вычисления, кеширование;
нет риска создать атрибут с опечаткой.

class DynamicModel:
    @property
    def username(self):
        raise AttributeError("Атрибут username не задан")
















Практикум
Задача 1: Базовый ORM-класс с полиморфным методом save()

Ситуация:
Вы работаете в команде над ORM-системой, которая сохраняет информацию о пользователя системы.

Вы и ваши коллеги обнаружили, что код дублируется при сохранении разных типов данных.

Вы решили применить свойство полиморфизма для решения обнаруженной проблемы.

Задача:

Создайте базовый класс Model, который будет содержать общую логику для всех моделей, метод save().
Класс User наследуется от Model и реализует свою версии метода save().

Шаги реализации:

Создайте базовый класс Model, содержащий метод save(), который выводит текст «Начало процесса сохранения»:
class Model:
    def save(self):
        print("Начало процесса сохранения")

Опишите дочерний класс User, который переопределяет save(), добавляя свою специфическую логику:

класс User инициализирует имя и электронную почту пользователя;

При переопределении метода save выводится текст: «Сохранение пользователя: {self.name}, email: {self.email}».

class User(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        super().save()  # Вызов базовой реализации
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")

Решение:

class Model:
    def save(self):
        print("Начало процесса сохранения")

class User(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        super().save()  # Вызов базовой реализации
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


















Задача 2: Создание нового метода ORM-класса

Ситуация:
Теперь вам необходимо добавить класс Product для разрабатываемой ORM и проверить работоспособность системы.

Задача:
Создайте класс Product, который наследуется от Model и реализует свою версию метода save().

Шаги реализации:

Опишите дочерний класс Product, который переопределяет save(), добавляя свою специфическую логику:

класс Product инициализирует название и стоимость продукта;

при переопределении метода save выводится текст: «Сохранение товара: {self.title}, цена: {self.price}».

class Product(Model):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def save(self):
        super().save()  # Вызов базовой реализации
        print(f"Сохранение товара: {self.title}, цена: {self.price}")


Проверьте работоспособность системы: инициализируйте пользователя и продукт, вызовите метод save() для двух созданных переменных.
# Использование
user = User("Иван Иванов", "ivan@example.com")
product = Product("Ноутбук", 50000)

user.save()
# Вывод:
# Начало процесса сохранения
# Сохранение пользователя: Иван Иванов, email: ivan@example.com

product.save()
# Вывод:
# Начало процесса сохранения
# Сохранение товара: Ноутбук, цена: 50000




Решение:

class Product(Model):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def save(self):
        super().save()  # Вызов базовой реализации
        print(f"Сохранение товара: {self.title}, цена: {self.price}")

# Использование
user = User("Иван Иванов", "ivan@example.com")
product = Product("Ноутбук", 50000)

user.save()
# Вывод:
# Начало процесса сохранения
# Сохранение пользователя: Иван Иванов, email: ivan@example.com

product.save()
# Вывод:
# Начало процесса сохранения
# Сохранение товара: Ноутбук, цена: 50000









Итоги:
Сегодня мы научились:

использовать один и тот же метод для разных классов с помощью свойства полиморфизма;
работать с разными типами полей (например, IntegerField, StringField) через единый интерфейс (Field);
использовать декораторы, чтобы добавлять дополнительную логику к методам ORM.