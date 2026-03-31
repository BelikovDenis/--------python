Сегодня мы углубимся в тему классов и ООП (объектно-ориентированного программирования)
и изучим абстрактные классы и методы, которые позволяют создавать более гибкие и структурированные программы.



На занятии мы:

научимся использовать абстрактные классы и методы для проектирования абстрактных структур;

поймём, как использовать абстрактные классы для создания интерфейсов;

применим абстрактные методы для определения обязательных функций в подклассах;

создадим абстрактные классы для управления данными.



Абстрактные классы представляют собой своеобразный способ документирования кода.
Они нужны для задания статичного поведения классов: мы изначально знаем,
какие методы у них точно будут, однако не ограничиваем их.


Пример абстрактного класса

Верхняя красная фигура представляет абстрактный класс, 
который задаёт общие правила. У него есть методы: формулы для площади (S) и периметра (P), но они не определены.

Синие круг и квадрат — это конкретные классы,
которые наследуются от абстрактного и реализуют свои версии методов для вычисления площади и периметра.

Давайте разберёмся, как их использовать и для чего они нужны.



Абстрактные классы в Python
Абстрактные классы — это классы, 
которые не могут быть инстанцированы (созданы как объекты) и используются как шаблоны для других классов.


Они позволяют определить общий интерфейс для группы подклассов, 
что делает код более структурированным и удобным для расширения.

Для работы с абстрактными классами в Python используется модуль abc (Abstract Base Classes).

Для чего нужны абстрактные классы?

Помогают избежать дублирования кода, определяя общие методы и свойства для группы классов.

Обеспечивают соблюдение контракта:
подклассы обязаны реализовать все абстрактные методы, что делает код более предсказуемым.

Упрощают проектирование сложных систем, позволяя разделить общую логику и конкретные реализации.

Рассмотрим на примерах, как это работает в Python.

Пример: Создание абстрактного класса




from abc import ABC, abstractmethod

class Shape(ABC):
    pass # сообщаем, что никаких действий выполняться не будет

class Circle(Shape):
   pass


class Square(Shape):
    pass


circle = Circle()
square = Square()



Объяснение:

Класс Shape является абстрактным, так как он наследуется от ABC.
Классы Circle и Square наследуются от абстрактного класса Shape 
и позволяют реализовать логику для этих конкретных классов.
Пока не совсем понятно: создали мы абстрактный класс, его потомков, а для чего это вообще нужно?

Давайте рассмотрим абстрактные методы и свойства — то, ради чего и пишут абстрактные классы.

Абстрактные методы
Абстрактные методы — это методы, которые объявлены в абстрактном классе, но не имеют реализации.

Они должны быть реализованы в подклассах. 
Если подкласс не реализует абстрактный метод, это приведёт к ошибке.

Пример: Использование абстрактных методов



from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return self.width * 4

circle = Circle(5)
print("Площадь круга:", circle.area())  # 78.5

square = square(6)
print("Площадь квадрата:", square.area())  # 36
print("Периметр квадрата:", square.perimeter())  # 24



Объяснение:

Класс Shape определяет абстрактный метод area.
Подклассы Circle и Square реализуют этот метод, 
предоставляя конкретную логику для вычисления площади круга и квадрата соответственно.
Обратим внимание, что класс Square также реализует метод perimeter.
Это говорит о том, что потомки абстрактных классов могут иметь не только абстрактные методы, 
но и свои собственные.



Если подкласс не реализует хотя бы один абстрактный метод, Python выдаст ошибку.
У класса могут быть не только абстрактные методы, но и свойства.

К примеру, создавая абстрактный класс Animal, 
у его потомков (например, Cat и Dog) точно будут возраст, рост и т.д. Рассмотрим подробнее.

Абстрактные свойства
Абстрактные свойства позволяют определить обязательные атрибуты для подклассов.

Рассмотрим на примерах.

Пример: Абстрактное свойство

from abc import ABC, abstractmethod

class Person(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Student(Person):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("Иван")
print(student.name)  # Иван





Объяснение:

Класс Person определяет абстрактное свойство name, которое должно быть реализовано в подклассах.
Подкласс Student реализует это свойство, предоставляя конкретную логику для получения имени.
С помощью этих средств можно строго задавать структуру объектов в Python, 
что часто применяется и в других объектно-ориентированных языках программирования,
например, в C и C++. Профессиональный разработчик регулярно сталкивается с такими способами задания объектов.

Эти знания нам особенно пригодятся,
когда мы будем писать масштабные проекты на Python, где будут встречаться похожие структуры.





Типичные ошибки
Тип ошибки 1: Попытка инстанцировать абстрактный класс

Абстрактные классы не могут быть инстанцированы напрямую. Попытка сделать это приведёт к ошибке.

Пример ошибки:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

animal = Animal()  # Ошибка: TypeError: Can't instantiate abstract class Animal with abstract method make_sound
Решение:

создаём подкласс и реализуем абстрактные методы.

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

dog = Dog()
print(dog.make_sound())  # Гав!
Тип ошибки 2: Не реализован абстрактный метод в подклассе

Если подкласс не реализует все абстрактные методы, это приведёт к ошибке.

Пример ошибки:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

circle = Circle(5)  # Ошибка: TypeError: Can't instantiate abstract class Circle with abstract method area



Решение:

реализуем абстрактный метод в подклассе.

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5







Практикум
Задание 1. Создание абстрактного класса для управления данными

Ситуация: мы пишем программу и вносим в неё функционал, 
позволяющий работать с файлами. Для этого нам нужно создать две новые структуры.

Задача — написать программу,
которая создаёт абстрактный класс DataManager и два подкласса: FileDataManager и DatabaseDataManager.

Шаги реализации

Импортируем модуль для работы с абстрактными классами:

используем модуль abc, чтобы создать абстрактный класс.
from abc import ABC, abstractmethod

2. Создаём абстрактный класс DataManager:

определяем абстрактные методы save и load.
class DataManager(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

3. Создаём подкласс FileDataManager:

реализуем методы для сохранения и загрузки данных из файла.
class FileDataManager(DataManager):
    def save(self, data):
        with open('data.txt', 'w') as file:
            file.write(data)

    def load(self):
        with open('data.txt', 'r') as file:
            return file.read()

4. Создаём подкласс DatabaseDataManager:

реализуем методы для сохранения и загрузки информации из базы данных (в данном примере просто имитируем работу с базой данных).
class DatabaseDataManager(DataManager):
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data

5. Тестируем программу:

создаём объекты подклассов и тестируем их методы.
file_manager = FileDataManager()
file_manager.save("Пример данных в файле")
print(file_manager.load())  # Пример данных в файле

db_manager = DatabaseDataManager()
db_manager.save("Пример данных в базе данных")
print(db_manager.load())  # Пример данных в базе данных
Реализация:

# Импорт модуля для работы с абстрактными классами
from abc import ABC, abstractmethod

# Создание абстрактного класса DataManager
class DataManager(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

# Создание подкласса FileDataManager
class FileDataManager(DataManager):
    def save(self, data):
        with open('data.txt', 'w') as file:
            file.write(data)

    def load(self):
        with open('data.txt', 'r') as file:
            return file.read()

# Создание подкласса DatabaseDataManager
class DatabaseDataManager(DataManager):
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data

# Тестирование программы
file_manager = FileDataManager()
file_manager.save("Пример данных в файле")
print(file_manager.load())  # Пример данных в файле

db_manager = DatabaseDataManager()
db_manager.save("Пример данных в базе данных")
print(db_manager.load())  # Пример данных в базе данных



Задание 2. Создание абстрактного класса для генерации отчётов

Ситуация: мы находимся в отделе разработки консалтинговой фирмы.
Нам необходимо создать интерфейс для генерации и сохранения отчётов.

Задача — написать программу, которая реализует абстрактный класс ReportGenerator,
определяющий интерфейс для генерации и сохранения отчётов.
Подклассы должны реализовать методы для создания отчётов в различных форматах (PDF, Excel, HTML) и их сохранения.

Шаги реализации

Импортируем модуль для работы с абстрактными классами:

используем модуль abc, чтобы создать абстрактный класс.
from abc import ABC, abstractmethod

2. Создаём абстрактный класс ReportGenerator:

определяем абстрактные методы generate_report (генерация отчёта) и save_report (сохранение отчёта).
class ReportGenerator(ABC):
 @abstractmethod
 def generate_report(self, data):
     pass

 @abstractmethod
 def save_report(self, filename):
     pass

3. Создаём подкласс PDFReportGenerator:

реализуем методы для генерации PDF-отчёта и его сохранения.
class PDFReportGenerator(ReportGenerator):
 def generate_report(self, data):
     return f"PDF Report Content: {data}"

 def save_report(self, filename):
     print(f"Saving PDF report to {filename}.pdf")

4. Создаём подкласс ExcelReportGenerator:

реализуем методы для генерации Excel-отчёта и его сохранения.
class ExcelReportGenerator(ReportGenerator):
 def generate_report(self, data):
     return f"Excel Report Content: {data}"

 def save_report(self, filename):
     print(f"Saving Excel report to {filename}.xlsx")

5. Создаём подкласс HTMLReportGenerator:

реализуем методы для генерации HTML-отчёта и его сохранения.
class HTMLReportGenerator(ReportGenerator):
 def generate_report(self, data):
     return f"<html><body>{data}</body></html>"

 def save_report(self, filename):
     print(f"Saving HTML report to {filename}.html")

6. Тестируем программу:

создаём объекты подклассов и проверяем их работу.
# Пример работы с PDF
pdf_gen = PDFReportGenerator()
pdf_content = pdf_gen.generate_report("Sales Data")
pdf_gen.save_report("sales_report")
# Пример работы с Excel
excel_gen = ExcelReportGenerator()
excel_content = excel_gen.generate_report("Inventory List")
excel_gen.save_report("inventory_report")
# Пример работы с HTML
html_gen = HTMLReportGenerator()
html_content = html_gen.generate_report("User Statistics")
html_gen.save_report("user_stats")
Реализация:

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass

    @abstractmethod
    def save_report(self, filename):
        pass

class PDFReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f"PDF Report Content: {data}"

    def save_report(self, filename):
        print(f"Saving PDF report to {filename}.pdf")

class ExcelReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f"Excel Report Content: {data}"

    def save_report(self, filename):
        print(f"Saving Excel report to {filename}.xlsx")

class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f"<html><body>{data}</body></html>"

    def save_report(self, filename):
        print(f"Saving HTML report to {filename}.html")

# Тестирование
pdf_gen = PDFReportGenerator()
pdf_content = pdf_gen.generate_report("Sales Data")
pdf_gen.save_report("sales_report")

excel_gen = ExcelReportGenerator()
excel_content = excel_gen.generate_report("Inventory List")
excel_gen.save_report("inventory_report")

html_gen = HTMLReportGenerator()
html_content = html_gen.generate_report("User Statistics")
html_gen.save_report("user_stats")



Итоги:
На этом занятии мы:

изучили абстрактные классы и методы в Python;
использовали абстрактные классы для создания интерфейсов;
применили абстрактные методы для определения обязательных функций в подклассах;
создали абстрактные классы для управления данными.
Эти знания и навыки помогут нам легко и быстро задавать похожие структуры
и очень пригодятся в дальнейшей разработке, когда мы будем создавать комплексные объекты.