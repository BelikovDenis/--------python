На прошлом занятии мы разобрали,
как приложения обмениваются данными с базой данных с помощью ORM — системы,
которая переводит Python-объекты в таблицы и обратно.
Это был пример взаимодействия процессов внутри одной системы: нашего приложения и его базы данных.

Сегодня мы делаем следующий шаг: переходим к взаимодействию между разными системами. Например:

приложение запрашивает погоду с сервера метеослужбы;
бот в Telegram отправляет сообщение с помощью сервиса ChatGPT;
онлайн-магазин связывается с платёжным шлюзом, чтобы принять оплату.


Во всех этих случаях связь идёт не напрямую,
а через API (Application Programming Interface) — набор правил, по которым одни программы могут обращаться к другим.

Если ORM — это «переводчик» между Python-кодом и SQL-базой данных,
то API — это язык общения между программами через интернет.

Сегодня мы:

разберёмся, как работает протокол HTTP, лежащий в основе большинства API;
познакомимся с REST — архитектурным стилем API;
научимся отправлять HTTP-запросы с помощью библиотеки requests;
создадим простой инструмент для получения информации из GitHub API.








Глоссарий к четырнадцатому занятию
API (Application Programming Interface)
API – интерфейс программирования приложений, набор правил и протоколов, позволяющий программам взаимодействовать друг с другом.

HTTP (HyperText Transfer Protocol)
HTTP – протокол передачи данных в интернете для обмена запросами и ответами между клиентом и сервером.

REST (Representational State Transfer)
REST – архитектурный стиль построения API,
который использует стандартные HTTP-методы (GET, POST, PUT, DELETE) и работает с данными в формате JSON/XML.

Эндпоинт (Endpoint)
Эндпоинт – URL-адрес API, по которому доступен определённый ресурс или функция.

Заголовки (HTTP Headers)
Заголовки – метаданные HTTP-запроса/ответа (например, Content-Type: application/json).




Введение в работу с API

Современные приложения обмениваются данными с серверами,
сторонними сервисами и с другими приложениями. Например:

приложение для погоды получает актуальные данные с сервера метеорологической службы;

интернет-магазин обращается к банковской системе, чтобы пользователь мог совершить оплату товара;

чат-бот в Telegram делает запросы к ChatGPT.

Чтобы обеспечить безопасное и эффективное взаимодействие этих систем,
обычно используется API (Application Programming Interface), который выполняет роль моста между приложениями.

Что такое API?

API — это набор правил и инструментов, с помощью которого одна программа может запрашивать данные или функционал у другой.

Примеры популярных API:

социальные сети (например, VK API) дают доступ к публикациям,
метрикам (количеству лайков, репостов) и другим данным;

онлайн-переводчики (Google Translate API, Yandex Translate API) позволяют встраивать автоматический перевод текста в другие программы;

Telegram Bot API (подходит для создания ботов в мессенджере).

Что такое HTTP?

В основе работы с API лежит HTTP (HyperText Transfer Protocol).

HTTP — это протокол передачи данных,
который используется для обмена информацией между клиентом и сервером.
Клиентом может быть браузер или программа.

Если ваша программа делает запросы к другим приложениям или серверам,
то она использует HTTP как язык, с помощью которого ваш код общается с серверами.

Когда вы работаете с API
(например, получаете прогноз погоды, список товаров из интернет-магазина или отправляете данные),
все запросы идут через HTTP.

Все современные API («ВКонтакте», Telegram, Google Maps) используют HTTP.
Без него вы не сможете получить данные от сервера или отправить их.


REST API

REST API — это набор правил, по которым работают большинство API.

Почти все популярные сервисы, например GitHub, предоставляют REST API.

Основные принципы работы с REST API:

Каждый ресурс (например, пользователь или пост) имеет свой URL (/users, /posts).

Для работы с данными используются команды (GET, POST, PUT, DELETE),
которые представляют собой HTTP-запросы.




Основные HTTP-запросы


Примеры:
https://top-academy.site/wp-content/uploads/2025/04/1-8.png

Когда вы открываете ленту «ВКонтакте», ваш браузер делает GET /posts.

Когда вы публикуете новый пост, ваш браузер делает POST /posts.

HTTP-коды: как понять, что ответил сервер?
https://top-academy.site/wp-content/uploads/2025/04/2-8-1024x277.png




Когда вы отправляете запрос на сервер, он отвечает не только данными, но и кодом статуса.


Примеры работы с HTTP-запросами

Рассмотрим примеры работы с API на Python.
Мы будем использовать сервисы JSONPlaceholder (тестовый API для изучения известных методов) и GitHub API.

Создаем GET-запрос

создать вирт окружение
установить requests 

pip install requests


import requests

# Получаем список задач для пользователя с ID 1
response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

if response.status_code == 200:
    todos = response.json()
    for task in todos:
        print(f"Задача {task['id']}: {task['title']} - {'Выполнена' if task['completed'] else 'Не выполнена'}")
else:
    print(f"Ошибка: {response.status_code}")

Задача 1: delectus aut autem - Не выполнена
Задача 2: quis ut nam facilis et officia qui - Не выполнена
Задача 3: fugiat veniam minus - Не выполнена
Задача 4: et porro tempora - Выполнена
Задача 5: laboriosam mollitia et enim quasi adipisci quia provident illum - Не выполнена
Задача 6: qui ullam ratione quibusdam voluptatem quia omnis - Не выполнена
Задача 7: illo expedita consequatur quia in - Не выполнена
Задача 8: quo adipisci enim quam ut ab - Выполнена
Задача 9: molestiae perspiciatis ipsa - Не выполнена
Задача 10: illo est ratione doloremque quia maiores aut - Выполнена
Задача 11: vero rerum temporibus dolor - Выполнена
Задача 12: ipsa repellendus fugit nisi - Выполнена
Задача 13: et doloremque nulla - Не выполнена
Задача 14: repellendus sunt dolores architecto voluptatum - Выполнена
Задача 15: ab voluptatum amet voluptas - Выполнена
Задача 16: accusamus eos facilis sint et aut voluptatem - Выполнена
Задача 17: quo laboriosam deleniti aut qui - Выполнена
Задача 18: dolorum est consequatur ea mollitia in culpa - Не выполнена
Задача 19: molestiae ipsa aut voluptatibus pariatur dolor nihil - Выполнена
Задача 20: ullam nobis libero sapiente ad optio sint - Выполнена
Разберем этот пример пошагово.

Импортируем библиотеку requests, которая позволяет отправлять HTTP-запросы (GET, POST и др.) и работать с ответами.
import requests
Отправляем GET-запрос к URL https://jsonplaceholder.typicode.com/users/1/todos.

Этот URL ведёт к тестовому API (JSONPlaceholder), который имитирует работу с задачами (todos) пользователей.

/users/1/todos означает, что мы запрашиваем список задач пользователя с ID = 1.

response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

После получения ответа от сервера проверяем его статус.
Код 200 означает успешный запрос (OK). 
Если сервер вернул другой код, например 404 («Не найдено») или 500 («Ошибка сервера»), выполнится блок else.

if response.status_code == 200:
Если ответ успешный (status_code == 200),
преобразуем данные из JSON-формата в Python-объект (список словарей) с помощью метода .json().
todos = response.json()

Выводим задачи в консоль: перебираем все задачи в списке todos.
for task in todos:
    print(f"Задача {task['id']}: {task['title']} - {'Выполнена' if task['completed'] else 'Не выполнена'}")

Для каждой задачи выводим:

task['id'] — уникальный идентификатор задачи;

task['title'] — название задачи;

'Выполнена' if task['completed'] else 'Не выполнена' — проверяем поле completed (булево значение) и выводим статус задачи.

Производим обработку ошибок.
else:
    print(f"Ошибка: {response.status_code}")
Если статус ответа не 200, выводим код ошибки (например, 404, 500 и т. д.).

Создаем POST-запрос

new_task = {
    "userId": 1,
    "title": "Купить молоко",
    "completed": False
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/todos',
    json=new_task  # Автоматически конвертирует dict в JSON и добавляет заголовок
)

print(f"Статус: {response.status_code}")  # 201 - Created
print(response.json())  # Вернет созданную задачу с новым ID
Статус: 201
{'userId': 1, 'title': 'Купить молоко', 'completed': False, 'id': 201}

Разберём этот код пошагово — он отправляет POST-запрос для создания новой задачи (todo) на тестовом API.

Создаём новую задачу (словарь new_task).
new_task = {
    "userId": 1,           # ID пользователя, которому принадлежит задача
    "title": "Купить молоко",  # Текст задачи
    "completed": False     # Статус выполнения (не выполнена)
}

Формируем данные новой задачи в виде словаря Python:

userId — идентификатор пользователя (здесь 1),

title — название задачи,

completed — статус (False = не выполнена).

Отправляем POST-запрос.
response = requests.post(
    'https://jsonplaceholder.typicode.com/todos',  # URL API для создания задачи
    json=new_task  # Передаем данные в формате JSON
)
requests.post() — отправляет POST-запрос (используется для создания данных).

URL: https://jsonplaceholder.typicode.com/todos — эндпоинт для работы с задачами.

Параметр json=new_task:

автоматически конвертирует словарь new_task в JSON;

устанавливает заголовок Content-Type: application/json.

Проверяем статус ответа.
print(f"Статус: {response.status_code}")  # 201 - Created
response.status_code — HTTP-статус ответа сервера.

201 Created — успешное создание ресурса (ожидаемый статус для POST).

Работаем с публичным API

Рассмотрим работу с публичным API GitHub и получим информацию о репозитории.

repo_url = 'https://api.github.com/repos/requests/requests'  # Официальный репозиторий библиотеки requests

response = requests.get(repo_url)
if response.status_code == 200:
    repo_data = response.json()
    print(f"Репозиторий: {repo_data['name']}")
    print(f"Звезд: {repo_data['stargazers_count']}")
    print(f"Описание: {repo_data['description']}")
else:
    print(f"Ошибка: {response.status_code}")

Репозиторий: requests
Звезд: 52691
Описание: A simple, yet elegant, HTTP library.

Этот код получает информацию о репозитории GitHub (в данном случае — официальном репозитории библиотеки requests) и выводит основные данные.

Указываем URL репозитория.
repo_url = 'https://api.github.com/repos/requests/requests'
repo_url — ссылка на API GitHub для получения данных о репозитории.
Формат: https://api.github.com/repos/{owner}/{repo_name}
owner — владелец репозитория (requests).
repo_name — название репозитория (requests).

Отправляем GET-запрос.
response = requests.get(repo_url)
requests.get() отправляет HTTP GET-запрос к GitHub API.
Ответ сохраняется в переменной response.
Проверяем статус ответа.
if response.status_code == 200:
Проверяем, успешен ли запрос:
200 OK — данные получены.
404 Not Found — репозиторий не существует.
403 Forbidden — доступ запрещён (например, из-за ограничения API).
Извлекаем данные из JSON.
repo_data = response.json()
response.json() преобразует ответ сервера (в формате JSON) в словарь Python.

Теперь repo_data содержит информацию о репозитории.
Выводим результат запроса к API.
print(f"Репозиторий: {repo_data['name']}")
print(f"Звёзд: {repo_data['stargazers_count']}")
print(f"Описание: {repo_data['description']}")
Выводим:
название репозитория (name),
количество звёзд (stargazers_count),
описание (description).
Обрабатываем ошибки.
else:
    print(f"Ошибка: {response.status_code}")

Если статус ответа не 200, выводим код ошибки.






Преимущества использования API

API позволяют программам обмениваться данными автоматически.
Это ускоряет работу с кодом и снижает количество ошибок.

Вместо разработки сложных функций с нуля (например,
для подключения платежей или автоматического определения геолокации) можно подключить API (Stripe, Google Maps и др.).

Современные API используют авторизацию (OAuth, API-ключи) и шифрование (HTTPS), защищая данные.

Примеры применения:

платежи (Stripe, PayPal),
карты (Google Maps),
погода (OpenWeatherMap),
ИИ (OpenAI, Gemini).












Типичные ошибки
Тип ошибки 1: Отсутствие обработки HTTP-ошибок

Проблема:
Когда API возвращают HTTP-коды ошибок (4xx, 5xx) и разработчики их игнорируют,
это приводит к сбоям в работе программы.

Пример ошибки:

import requests

response = requests.get("https://api.example.com/data")
data = response.json()  # Ошибка, если response.status_code != 200

Решение:
Прописывать правила для проверки статуса ответа и обработки ошибок:

response = requests.get("https://api.example.com/data")
response.raise_for_status()  # Вызовет исключение при 4xx/5xx
data = response.json()








Тип ошибки 2: Неправильное использование заголовков (Headers)

Отсутствие заголовков при создании запроса может приводить к ошибкам в работе программы. Например:

отсутствие Content-Type для POST/PUT;

передача API-ключа не в том заголовке.

Пример ошибки:

# API ждет JSON, но заголовок не указан
requests.post(
    "https://api.example.com",
    json={"key": "value"},
    # Забыли добавить: headers={"Content-Type": "application/json"}
)

# API-ключ передается в URL, а не в headers
requests.get("https://api.example.com?api_key=123")  # Небезопасно!

Решение:
Всегда проверять требуемые заголовки, сверяться с документацией API.

requests.post(
    "https://api.example.com",
    json={"key": "value"},
    headers={
        "Content-Type": "application/json",
        "Authorization": "YOUR_API_KEY"  # Передача ключа API
    }
)















Практикум
Задача 1: Создание класса для получения информации о репозиториях на GitHub

Ситуация:

Вы разрабатываете инструмент для анализа активности разработчиков на GitHub.
Вам нужно получить список репозиториев пользователя, их описания, язык программирования и количество звёзд.

Используйте следующий код для тестирования инструмента:

# Пример использования
if __name__ == "__main__":
    github = GitHubAPI()
    username = input("Введите имя пользователя GitHub: ")
    repos = github.get_user_repos(username)

    if repos:
        print(f"Репозитории пользователя {username}:")
        for repo in repos:
            print(f"Название репозитория: {repo['name']}")
            print(f"Описание репозитория: {repo['description']}")
            print(f"Язык репозитория: {repo['language']}")
            print(f"Звёзд: {repo['stars']}")

        github.save_to_json(repos)
    else:
        print("Не удалось получить данные.")

Задача:

Создайте конструктор для класса GitHubAPI. Пропишите метод, который делает запросы к репозиториям.

Шаги реализации:

Импортируйте библиотеку requests:

import requests


Создайте класс GitHubAPI, который инициализирует атрибут base_url со значением "https://api.github.com":

class GitHubAPI:
    def __init__(self):
        self.base_url = "https://api.github.com"

Создайте метод класса get_user_repos.
Метод принимает на вход имя пользователя, для которого мы собираем статистику:

def get_user_repos(self, username):


Внутри метода создаём переменную url, которая «склеивает» ссылку для запроса через API:

url = f"{self.base_url}/users/{username}/repos"
Делаем запрос к URL через requests.get:

response = requests.get(url)
Проверяем на ошибки HTTP:

response.raise_for_status()
Получаем JSON-объект:

repos = response.json()
Добавляем обработку ошибок через requests.exceptions.RequestException.
Возвращаем информацию о репозиториях, если запрос произведен успешно.
Выводим сообщение об ошибке и возвращаем None в ином случае:
try:
    response = requests.get(url)
    response.raise_for_status()
    repos = response.json()
    return repos
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к GitHub API: {e}")
    return None

Решение:

import requests


class GitHubAPI:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_user_repos(self, username):
        url = f"{self.base_url}/users/{username}/repos"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка на ошибки HTTP
            repos = response.json()
            return repos
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к GitHub API: {e}")
            return None


if __name__ == "__main__":
    api = GitHubAPI()

    # Пример использования
    username = "torvalds"  # Можно заменить на любого пользователя
    repos = api.get_user_repos(username)

    if repos:
        print(f"Репозитории пользователя {username}:")
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print("Не удалось получить репозитории")









Задача 2: Разработка методов класса для получения информации о репозиториях на GitHub

Ситуация:
Вы продолжаете разрабатывать класс GitHubAPI.
Теперь вам необходимо добавить методы для парсинга репозиториев и сохранения информации в файл.

Задача:
Добавьте в класс GitHubAPI инкапсулированный метод, который извлекает информацию из репозиториев.
Пропишите метод для сохранения результатов в файл *.json.

Шаги реализации:

Создайте инкапсулированный метод _parse_repos, который принимает на вход информацию о репозиториях:
def _parse_repos(self, repos_data):
Метод создаёт пустой список repos_info, куда мы будем сохранять информацию из репозиториев, полученную через API:

repos_info = []
Для каждого репозитория из repos_data создается словарь repo_info, который сохраняет:

имя репозитория repo["name"];
описание репозитория, получаемое через get: repo.get("description", "No description");
язык репозитория, получаемый через get: repo.get("language", "Not specified");
количество звёзд в репозитории repo[stargazers_count].
Информация по каждому репозиторию добавляется в список repos_info:

for repo in repos_data:
    repo_info = {
        "name": repo["name"],
        "description": repo.get("description", "No description"),
        "language": repo.get("language", "Not specified"),
        "stars": repo["stargazers_count"]
    }
    repos_info.append(repo_info)
Функция возвращает список repos_info:

return repos_info

Обновите метод get_user_repos.
Вместо переменной repos метод должен возвращать результат обработки инкапсулированного метода _parse_repos:

return self._parse_repos(repos)

Импортируйте json:

import json

Создайте метод класса save_to_json, который принимает на вход данные из репозиториев и название файла,
куда будут сохраняться результаты работы вашего инструмента (по умолчанию: "github_repos.json"):
def save_to_json(self, data, filename="github_repos.json"):
Функция открывает файл с указанным именем в режиме w с кодировкой utf-8 и записывает файл с помощью библиотеки json.
В результате работы в консоль выводится текст Данные сохранены в <название файла>:

with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"Данные сохранены в {filename}")

Решение:

import requests
import json


class GitHubAPI:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_user_repos(self, username):
        url = f"{self.base_url}/users/{username}/repos"
        try:
            response = requests.get(url)
            response.raise_for_status()
            repos = response.json()
            return self._parse_repos(repos)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к GitHub API: {e}")
            return None

    def _parse_repos(self, repos_data):
        repos_info = []
        for repo in repos_data:
            repo_info = {
                "name": repo["name"],
                "description": repo.get("description", "No description"),
                "language": repo.get("language", "Not specified"),
                "stars": repo["stargazers_count"]
            }
            repos_info.append(repo_info)
        return repos_info

    def save_to_json(self, data, filename="github_repos.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {filename}")


if __name__ == "__main__":
    api = GitHubAPI()

    # Запрашиваем имя пользователя
    username = input("Введите имя пользователя GitHub: ")

    # Получаем репозитории
    repos = api.get_user_repos(username)

    if repos:
        # Выводим результаты в терминал
        print(f"\nРепозитории пользователя {username}:")
        print("=" * 50)
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo['name']}")
            print(f"   Описание: {repo['description']}")
            print(f"   Язык: {repo['language']}")
            print(f"   Звёзды: {repo['stars']}")
            print("-" * 30)

        # Сохраняем в JSON
        api.save_to_json(repos)
    else:
        print("Не удалось получить репозитории.")









Итоги:
Сегодня мы научились:

объяснять, что такое API и как работает HTTP-протокол;
отправлять запросы к REST API с помощью библиотеки requests;
использовать методы GET и POST для получения и отправки данных;
проверять коды ответа сервера и обрабатывать ошибки;
писать простой класс для работы с внешним API на примере GitHub.