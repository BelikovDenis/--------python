На прошлом занятии мы познакомились с тем, как работают REST API,
какие HTTP-методы (GET, POST, PUT, DELETE) используются для обращения к серверу,
и научились выполнять базовые запросы с помощью библиотеки requests.
Мы также разобрали основные коды ответа сервера (например, 200 — OK,
    404 — Not Found, 500 — Internal Server Error) и научились обрабатывать успешные ответы.



Сегодня мы сделаем следующий шаг и изучим продвинутые возможности requests,
которые позволяют не только отправлять запросы, но и работать с более сложными и реальными сценариями.

Мы научимся:

использовать HTTP-заголовки для указания формата данных и авторизации;

подключать API-ключи для работы с защищёнными API;

правильно обрабатывать ошибки и исключения, возникающие при получении ответов с кодами 4xx и 5xx;

указывать тайм-ауты для предотвращения зависаний при работе с медленными или недоступными сервисами.




Глоссарий к пятнадцатому занятию

Обработка ошибок (Error Handling)
Обработка ошибок – механизм реагирования на HTTP-статусы, указывающие на сбой (например, 404 Not Found, 500 Server Error).

Аутентификация (Authentication)
Authentication – процесс проверки прав доступа к API.

Тайм-ауты (Timeouts)
Тайм-аут – максимальное время ожидания ответа от сервера. Защищает программу от зависания.





Сегодня мы освоим работу с инструментами,
которые позволят нам профессионально взаимодействовать с API:
обрабатывать сложные сценарии, оптимизировать производительность и безопасно работать с данными.


HTTP-заголовки

HTTP-заголовки — это метаданные,
которые передаются вместе с запросом или ответом и содержат служебную информацию. Например, они позволяют:

указывать тип данных (Content-Type),

передавать токены авторизации (Authorization).

Рассмотрим работу с ключевыми HTTP-заголовками в библиотеке requests.

Заголовок Content-Type

Заголовок Content-Type сообщает серверу, в каком формате передаются данные в теле запроса.

Примеры значений, которые может принимать заголовок Content-Type:

application/json — для данных в формате JSON,

application/xml — для XML-данных,

text/html — для HTML-контента,

multipart/form-data — для загрузки файлов,

application/x-www-form-urlencoded — для стандартных форм.



Пример использования заголовка Content-Type:

import requests

headers = {
    "Content-Type": "application/json"
}
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data,
    headers=headers
)

print(response.status_code)
print(response.json())
# 201
# {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}


Этот код:

Отправляет POST-запрос к тестовому API JSONPlaceholder.

Создает новую запись (post) с заголовком foo и текстом bar.

API всегда возвращает статус 201 (Created) и имитирует успешное создание объекта.


Заголовок Authorization

Заголовок Authorization используется для аутентификации и авторизации запросов.
Он передает токены для доступа к данным.

Часто токены используются для получения доступа к API. Рассмотрим пример работы с OpenWeatherMap API.

Получение API-ключа (токена):

Перейдите на OpenWeatherMap.
Зарегистрируйтесь (Sign Up → Free).

После входа в аккаунт найдите API-ключ на странице API Keys.

Скопируйте ключ.
Важно:

Ключ активируется не сразу, иногда требуется 10–30 минут после регистрации.
Если запрос возвращает ошибку 401 (Unauthorized), это означает, что:
ключ не активирован (попробуйте позже),
ключ введен неправильно (проверьте опечатки),
истек срок действия ключа (нужно обновить в личном кабинете).
Рассмотрим пример запроса с авторизацией:

import requests

access_key = 'cd0b91f4-fcfb-4b51-97b2-1c18adc0140a'

headers = {
    'X-Yandex-Weather-Key': access_key
}

# Координаты Евпатории
latitude = 45.1906
longitude = 33.3677

# Правильный URL для REST API v2 (включает параметры lat, lon и lang)
url = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&lang=ru_RU'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Погода в Евпатории:")
    # Извлекаем основные данные
    temp = data['fact']['temp']
    feels_like = data['fact']['feels_like']
    condition = data['fact']['condition']
    humidity = data['fact']['humidity']
    
    print(f"Температура: {temp}°C")
    print(f"Ощущается как: {feels_like}°C")
    print(f"Условия: {condition}")
    print(f"Влажность: {humidity}%")
else:
    print(f"Ошибка HTTP: {response.status_code}")
    print(response.text)


Указания по работе с API-ключами:

Храните API-ключ в безопасности: используйте переменные окружения (.env) или секреты, а не прописывайте их напрямую в коде.
Проверяйте HTTPS: убедитесь, что API использует защищённое соединение.

Не публикуйте ключи в открытых репозиториях (например, на GitHub).

Обработка ошибок

Почему важно производить обработку ошибок в HTTP-запросах?

Поддержка стабильности приложения: обработка ошибок необходима для предотвращения аварийного завершения программы.
Повышение предсказуемости работы программы: приложение должно корректно реагировать на проблемы сети или сервера.
Возможность показать пользователю понятное сообщение об ошибке.
Логирование проблем для последующего анализа и исправления.
Основные типы исключений в библиотеке requests:

ConnectionError – проблемы с подключением к серверу.
HTTPError – ошибки HTTP (4xx – клиентские, 5xx – серверные).
Timeout – истекло время ожидания ответа.
RequestException – базовый класс для всех исключений библиотеки.


Рассмотрим базовый пример с обработкой основных ошибок:

import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Проверяет статус код
    data = response.json()
except HTTPError as http_err:
    print(f"HTTP ошибка: {http_err}")
except ConnectionError:
    print("Не удалось подключиться к серверу")
except Timeout:
    print("Превышено время ожидания")
except RequestException as err:
    print(f"Ошибка при выполнении запроса: {err}")

Рассмотрим этот пример пошагово:

Импорт библиотек и исключений.
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
requests – основная библиотека для HTTP-запросов.
Импортируем конкретные исключения для точной обработки ошибок:
RequestException – базовый класс всех исключений requests,
HTTPError – для HTTP-ошибок (4xx, 5xx),
ConnectionError – проблемы с подключением,
Timeout – превышение времени ожидания.
Блок try: попытка выполнить запрос.
try:
response = requests.get('https://api.example.com/data', timeout=5)
Пытаемся выполнить GET-запрос к указанному URL.
Параметр timeout=5 устанавливает максимальное время ожидания ответа (5 секунд).
Проверка HTTP-статуса.
response.raise_for_status()  # Проверяет статус-код
Метод raise_for_status() вызывает исключение HTTPError, если статус-код ответа:
4xx (ошибки клиента, например 404 Not Found),
5xx (ошибки сервера, например 500 Internal Server Error).
Если статус-код в диапазоне 200–299, исключение не генерируется.
Парсинг JSON-ответа.
data = response.json()
Если запрос успешен (raise_for_status() не вызвал исключение), парсим JSON-ответ в переменную data.
Блок except: обработка ошибок.
a. Обработка HTTP-ошибок (4xx, 5xx):

except HTTPError as http_err:
    print(f"HTTP ошибка: {http_err}")
Срабатывает, если raise_for_status() обнаружил статус 4xx или 5xx.
Выводим сообщение об ошибке (например, 404 Client Error: Not Found).
b. Обработка проблем с подключением:

except ConnectionError:
    print("Не удалось подключиться к серверу")
Срабатывает при:
проблемах с DNS (неверный домен),
недоступности сервера (отказал в подключении).
сетевых проблемах (например, нет интернета).
c. Обработка тайм-аута:

except Timeout:
    print("Превышено время ожидания")
Сервер не ответил за указанное время (timeout=5).
d. Общая обработка других ошибок:

except RequestException as err:
    print(f"Ошибка при выполнении запроса: {err}")

Ловит все остальные ошибки requests, не попавшие в предыдущие блоки:
например, некорректный URL, слишком много редиректов (TooManyRedirects).
Важные замечания:

Порядок except имеет значение:
сначала выполняются конкретные исключения (HTTPError), потом общие (RequestException).
Использование timeout обязательно: 
без него запрос может висеть бесконечно.
Для production-кода (так называется код, который работает в реальной рабочей среде (production environment),
        а не в тестовой или в среде разработчика) лучше использовать логирование (logging) вместо print.

Преимущества методов и инструментов для продвинутой работы в библиотеке requests

HTTP-заголовки:

позволяют явно указывать тип данных (Content-Type);
обеспечивают безопасную авторизацию (Authorization).
Авторизация через API-ключи:

простая интеграция с сервисами (OpenWeatherMap, GitHub API и др.);
ключи можно передавать в заголовках или параметрах URL;
использование ключей повышает безопасность использования программного обеспечения:
ключи можно отозвать при утечке данных.

Обработка ошибок в requests:
устойчивость к сбоям (тайм-ауты, недоступность сервера);
сообщения об ошибках для отладки;
предотвращение аварийного завершения программы.










Типичные ошибки
Тип ошибки 1: Отсутствие заголовка Content-Type

Проблема:
Сервер может не распознать формат данных и вернуть ошибку 415 Unsupported Media Type (если ожидает JSON, а получает текст).

Пример ошибки:

# API ждет JSON, но заголовок не указан
requests.post("https://api.example.com", data={"key": "value"})
# Сервер отвечает: 415 (т. к. данные ушли как form-data, а не JSON)

Решение:
Всегда указывать Content-Type, если API требует конкретный формат.

requests.post(
    "https://api.example.com",
    json={"key": "value"},
    headers={"Content-Type": "application/json"}  # Теперь сервер поймет данные
)









Тип ошибки 2: Передача API-ключа в URL вместо заголовка

Если указать API-ключ в URL вместо заголовка в headers:

ключ останется в логах сервера и истории браузера (это небезопасно!);
некоторые API отклонят такие запросы с ошибкой 403 Forbidden.
Пример ошибки:

# Ключ в URL — уязвимость безопасности!
requests.get("https://api.example.com/data?api_key=123")

Решение:
Передавать ключ в заголовке Authorization (или как указано в документации API).

requests.get(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer YOUR_API_KEY"}  # Безопасный способ
)

Тип ошибки 3: Игнорирование тайм-аута (timeout)

Запрос может висеть бесконечно, если сервер не отвечает, что приведет к зависанию программы.

Пример ошибки:

# Без timeout программа может зависнуть
requests.get("https://api.example.com/slow-endpoint")  # Ждет вечно...
Решение:
Всегда устанавливать разумный timeout (например, 5–10 секунд):

requests.get("https://api.example.com/slow-endpoint", timeout=5)
# Через 5 сек. выбросится исключение Timeout





Тип ошибки 4: Отсутствие обработки ошибок 4xx/5xx

Программа прервет свою работу при получении ошибки сервера (например, 404 Not Found или 500 Internal Server Error).

Пример ошибки:

response = requests.get("https://api.example.com/invalid-url")
data = response.json()  # Ошибка, если response.status_code == 404

Решение:
Использовать raise_for_status() или проверять статус вручную:

response = requests.get("https://api.example.com/invalid-url")
if response.status_code == 200:
    data = response.json()
else:
    print(f"Ошибка {response.status_code}: {response.text}")












Практикум
Задача 1: Анализ погоды через OpenWeatherMap API

Ситуация:

Вы разрабатываете консольный инструмент для получения и анализа текущей погоды в любом городе мира. Инструмент должен:

запрашивать у пользователя название города,

делать запрос к OpenWeatherMap API,

выводить основную информацию о погоде,

сохранять историю запросов в JSON-файл.

Используйте следующий код для тестирования инструмента:

if __name__ == "__main__":
    weather_app = WeatherAPI()
    city = input("Введите город: ")
    weather_data = weather_app.get_weather(city)

    if weather_data:
        print(f"\nПогода в {city}:")
        print(f"Температура: {weather_data['temp']}°C")
        print(f"Ощущается как: {weather_data['feels_like']}°C")
        print(f"Влажность: {weather_data['humidity']}%")

        weather_app.save_to_json(weather_data)
    else:
        print("Не удалось получить данные о погоде.")
Задача:

Создайте класс WeatherAPI.

Шаги реализации:

Импортируйте библиотеки:
import requests
import json
from datetime import datetime
Создайте класс WeatherAPI с конструктором:
Инициализируйте base_url для API OpenWeatherMap: «https://api.openweathermap.org/data/2.5/weather».

Добавьте атрибут api_key (ваш ключ от OpenWeatherMap).

Совет: лучше хранить ключ в переменной окружения (os.getenv(«OWM_API_KEY»)).

class WeatherAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key
Решение:

import requests
import json
from datetime import datetime

class WeatherAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key






Задача 2: Реализация метода get_weather

Ситуация:
Вы продолжаете разрабатывать класс для получения информации о погоде. 
Теперь вам предстоит разработать метод, который принимает название города и возвращает словарь с данными:

{
    "city": "Москва",
    "temp": 25.3,
    "feels_like": 27.0,
    "humidity": 65,
    "description": "ясно"
}
Задача:
Реализуйте метод и добавьте обработку ошибок:

«Некорректный API-ключ» (401),

«Город не найден» (404),

«Проблемы с сетью» (тайм-аут 5 сек.).

Шаги реализации:

Подготовка параметров запроса.
params = {
    "q": city,            # Название города для поиска
    "appid": self.api_key, # API-ключ для аутентификации
    "units": "metric",     # Единицы измерения (°C, м/с)
    "lang": "ru"           # Язык ответа (русский)
}
Отправка HTTP-запроса.
Отправляется GET-запрос к API погоды с указанными параметрами.

timeout=5 — если сервер не ответит за 5 секунд, выбросится исключение.

response = requests.get(
    self.base_url,  # Базовый URL API (например, "https://api.openweathermap.org/data/2.5/weather")
    params=params,   # Параметры из предыдущего шага
    timeout=5        # Максимальное время ожидания ответа (5 сек.)
)
Проверка ответа сервера.
Если сервер вернул код ошибки (404, 500 и др.), метод выведет HTTPError, например при неверном API-ключе или несуществующем городе.
response.raise_for_status()  # Проверка кода статуса (4xx/5xx)
Парсинг JSON-ответа.
API возвращает данные в формате JSON, которые конвертируются в словарь.
data = response.json()  # Преобразует JSON-ответ в словарь Python
Форматирование результата.
return {
    "city": city,                     # Название города
    "temp": data["main"]["temp"],      # Температура (°C)
    "feels_like": data["main"]["feels_like"],  # Ощущаемая температура
    "humidity": data["main"]["humidity"],      # Влажность (%)
    "description": data["weather"][0]["description"]  # Описание ("ясно", "дождь")
}
Обработка ошибок.
Ошибки HTTP (4xx/5xx):

except requests.exceptions.HTTPError as e:
    if response.status_code == 404:
        print(f"Город '{city}' не найден.")  # Например, если в названии города опечатка
    else:
        print(f"Ошибка API: {e}")  # Другие ошибки (например, 401 при неверном API-ключе)
Тайм-аут соединения:

except requests.exceptions.Timeout:
    print("Сервер не ответил за 5 секунд.")  # API перегружен или нет интернета
Прочие ошибки сети:

except requests.exceptions.RequestException as e:
    print(f"Ошибка подключения: {e}")  # DNS-проблемы, обрыв соединения и т. д.
Возврат None при ошибке:

return None  # Указывает на неудачный запрос
Решение:

def get_weather(self, city):
    params = {
        "q": city,
        "appid": self.api_key,
        "units": "metric",  # Для температуры в °C
        "lang": "ru"        # Описание погоды на русском
    }

    try:
        response = requests.get(self.base_url, params=params, timeout=5)
        response.raise_for_status()  # Проверка на 4xx/5xx
        data = response.json()

        return {
            "city": city,
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Город '{city}' не найден.")
        else:
            print(f"Ошибка API: {e}")
    except requests.exceptions.Timeout:
        print("Сервер не ответил за 5 секунд.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")

    return None





Итоги:
Сегодня мы научились:

обрабатывать HTTP-заголовки для указания типов данных и обеспечения авторизации;
использовать API-ключи для получения доступа к API-сервисам;
обрабатывать ошибки,
чтобы получать сообщения для отладки и предотвращать непредвиденное завершение работы программы во время работы с HTTP-запросами.