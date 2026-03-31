Урок №21. Fetch.

Учебные материалы

Сегодня мы изучим Fetch API — современный способ выполнения HTTP-запросов в JavaScript. 
Fetch предоставляет простой и эффективный интерфейс для работы с сетевыми запросами, 
заменяя устаревший XMLHttpRequest.

Fetch позволяет не только получать данные, но и отправлять их на сервер, 
изменять заголовки и обрабатывать разные форматы ответов (JSON, текст, файлы в бинарном виде). 
В отличие от старых подходов, он более гибкий и удобный для работы с REST API.

Сегодня мы:

узнаем, что такое Fetch API и как он упрощает работу с сетевыми запросами;
научимся отправлять GET-, POST-, PUT- и DELETE-запросы с помощью Fetch;
разберём, как обрабатывать ответы сервера в разных форматах (JSON, текст, файлы);
освоим обработку ошибок сети и HTTP-статусов;
научимся отменять запросы с помощью AbortController;
поймём, как работать с CORS и куками в Fetch.
После занятия мы сможем делать HTTP-запросы к серверу и обрабатывать ответы, 
использовать Fetch для взаимодействия с API.




Глоссарий к двадцать первому занятию
HTTP/HTTPS (Протоколы передачи данных)

HTTP/HTTPS — стандартные протоколы для передачи данных в интернете. 
HTTPS является защищённой версией HTTP с использованием шифрования SSL/TLS.

REST API (Архитектурный стиль взаимодействия)

REST API — подход к проектированию веб-сервисов, 
использующий HTTP-методы для взаимодействия с ресурсами. 
Основывается на принципах единообразия интерфейса и отсутствия состояния.

GraphQL

GraphQL — язык запросов для API, позволяющий клиентам точно определять структуру требуемых данных. 
Решает проблему избыточности или недостатка данных, характерную для REST.

Pending (В ожидании)

Pending — состояние Promise, означающее, что асинхронная операция ещё не завершена. 
Promise находится в ожидании результата.

Callback Hell (Проблема вложенных колбэков)

Callback Hell — антипаттерн в JavaScript, возникающий при множественной вложенности асинхронных колбэков. 
Усложняет чтение и поддержку кода.








Что такое Fetch?
Что же такое Fetch? Это способ делать HTTP-запросы в JavaScript. 
Он позволяет получать/отправлять/обновлять/удалять данные.

Определение есть, но понятнее не стало, давайте разбираться.

Fetch простыми словами

С помощью функции fetch() можно посылать сетевые запросы на сервер получать/отправлять данные. 
Мы можем провести аналогию с браузером (программой, которая позволяет нам просматривать веб-страницы). 
Представим, что fetch — это браузер, только в коде.

После ввода URL (например, https://www.google.com/) в адресную строку браузер отправляет запрос на сервер.
Браузер получает ответ: response => “<!DOCTYPE html><head>…” Сервер присылает HTML, JSON или другой ответ.
Если сайт недоступен (ошибка 404, нет интернета), браузер покажет ошибку.
Отправка данных (POST) → как форма в браузере. 
Когда мы отправляем форму аутентификации (вводим логин/пароль и нажимаем кнопку «Войти»), 
браузер передаёт данные на сервер.
fetch ('https://www.google.com/') делает то же самое.

Ответ приходит в объекте Response, и его нужно «распаковать»:

fetch('https://www.google.com/')
.then(response => response.json())  // "Читаем" ответ как JSON (как браузер парсит HTML)
.then(data => console.log(data));   // Получаем готовые данные
В fetch ошибки ловятся через .catch():

fetch('https://api.example.com/not-found')
.then(response =>
{
  if (!response.ok) throw new Error('Ошибка загрузки!'); // Как "404 Not Found" в браузере
  return response.json();
})
.catch(err => console.error('Ой!', err)); // Покажет ошибку в консоли
Отправка данных, fetch это тоже умеет:

fetch('https://api.example.com/login',
{
method: 'POST',// Метод как у формы (GET/POST/PUT)
// Тип данных (как заголовки браузера)
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({// Данные формы, но в JSON
  user: 'admin',
  password: '123'
})
});
Что в итоге? Мы можем представить fetch как «программный браузер»:

Отправляет запросы, как ввод URL в адресную строку.

Получает ответы и преобразует их в текст.

Получает «служебные» данные, такие как статус ответа, заголовки.

Отправляет данные на сервер.

Метод fetch() возвращает объект с информацией: статус ответа, заголовки, ответ на запрос.
Fetch API — это современный интерфейс для выполнения HTTP-запросов в JavaScript. 
Он был введён в спецификации Fetch в 2015 году и предоставляет более простой 
и мощный способ работы с сетевыми запросами по сравнению с его предшественником XMLHttpRequest.

Чем Fetch лучше предшественников?
Как уже было упомянуто, раньше использовали XMLHttpRequest, Fetch решает те же задачи, но у него есть ряд преимуществ:

проще синтаксис – меньше кода;
работает с промисами – удобная обработка ответов;
современный стандарт – поддерживается всеми браузерами;
основа современного веба – используется в React/Vue/Angular;
работает с любыми API: JSON, XML, файлы;
поддерживает async/await (об этом мы говорили в Занятии 20) – делает код ещё чище.
Для чего может пригодиться Fetch?
Загрузка данных.
Отправка форм без перезагрузки страницы.
Итак, fetch — это простой, эффективный и универсальный инструмент для работы с сетью в JavaScript, 
который должен знать каждый веб-разработчик. Современный веб невозможен без взаимодействия с серверами. 
Пользователи ожидают динамической загрузки контента, быстрых обновлений и плавных взаимодействий.

Хронология эволюции сетевых запросов
Эволюция от громоздкого XMLHttpRequest до элегантного Fetch API происходила постепенно.

1. Эпоха iframe (1996-2005)
Первые асинхронные запросы делали через скрытые iframe: document.getElementById('hiddenFrame').src = 'data.json';

Недостатки:

невозможно обработать ошибки;
ограниченный контроль;
уязвимости безопасности.
2. XMLHttpRequest (2005-2015)
Революция AJAX (Asynchronous JavaScript and XML):

const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/data', true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      console.log(xhr.responseText);
    } else {
      console.error('Error:', xhr.status);
    }
  }
};
xhr.send();
Недостатки:

сложная обработка ошибок;
громоздкий синтаксис;
отсутствие стандартизации.
3. jQuery.ajax (2006-2016)
Упрощение работы с XHR:

$.ajax({
  url: '/api/data',
  method: 'GET',
  success: function(data) {
    console.log(data);
  },
  error: function(err) {
    console.error(err);
  }
});
Недостатки:

устаревшая callback-архитектура;
зависимость от jQuery;
отсутствие современных возможностей;
избыточность для простых запросов.
4. Fetch API (2015 — настоящее время)
Актуальный стандарт и тема этого занятия. Fetch был представлен в 2015 году как современная замена XHR.

fetch('/api/data')
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.error(err));
Преимущества:

чистый Promise-based API;
поддержка Streams API;
встроенная работа с CORS.
Зачем был введён Fetch?
Раньше в JavaScript для сетевых запросов использовался громоздкий и неудобный XMLHttpRequest (XHR).
Fetch был создан, чтобы устранить его основные недостатки:

1. Простота и удобство
В современной веб-разработке XMLHttpRequest (XHR) заменяется на Fetch API.

XHR:

const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data');
xhr.onload = function() {
  if (xhr.status === 200) {
    console.log(JSON.parse(xhr.response));
  }
};
xhr.send();
Fetch:

fetch('https://api.example.com/data')
.then(response => response.json())
.then(data => console.log(data));
Что изменилось?
Код стал чище и понятнее.

2. Поддержка Promise

Проблема XHR: колбэки (onload, onerror) вели к «аду» (ситуациям, 
когда код превращается во вложенные друг в друга колбэки, как матрёшка, и становится нечитаемым).

Решение Fetch: возвращает Promise, что позволяет писать цепочки .then() и использовать async/await.

// Современный стиль с async/await
async function loadData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}
Что изменилось?
Мы получили удобное использование асинхронного кода.

3. Улучшенная работа с HTTP

Проблема XHR: плохая поддержка заголовков, методов, CORS.

Решение Fetch: простая настройка headers, method, body.

fetch('https://api.example.com/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user: 'admin' })
});
Что изменилось?
Гибкость для сложных запросов.

4. Безопасность и контроль

Проблема XHR: сложно обрабатывать ошибки (например, HTTP 404).

Решение Fetch: чёткое разделение логики обработки ошибок и успешных ответов.

fetch('https://api.example.com/not-found')
.then(response => {
  if (!response.ok) throw new Error('Ошибка HTTP: ' + response.status);
  return response.json();
});
Что изменилось?
Предсказуемая обработка ошибок. Код явно проверяет свойство response.ok, 
что позволяет легко видеть, как обрабатываются различные статусы HTTP.

5. Совместимость с современными API

Fetch работает с:
• Streams API (для обработки больших данных);
• Service Workers (для офлайн-режима);
• AbortController (для отмены запросов).

Пример отмены запроса:

let controller = new AbortController();
fetch('https://api.example.com/data', { signal: controller.signal })
  .catch(err => {
    if (err.name === 'AbortError') console.log('Запрос отменён!');
  });
// Отменяем через 2 секунды
setTimeout(() => controller.abort(), 2000);
Что изменилось?
Интеграция с новыми возможностями браузеров.

Почему в итоге Fetch заменил XHR?
Проще — меньше кода, больше ясности.
Современнее — Promise, async/await.
Безопаснее — чёткие ошибки, CORS.
Гибче — настройка запросов «под ключ».
Будущее — совместимость с новыми API.
Fetch — это эволюция сетевых запросов в JavaScript, сделавшая их такими же простыми, 
как document.querySelector() после getElementById.

Использование Fetch API для создания HTTP-запросов
Базовый пример использования Fetch

Базовый пример использования fetch для отправки запроса выглядит следующим образом:

fetch(url, [options])
.then(response =>
{
  // Обработка успешного ответа
})
.catch(error =>
{
  // Обработка ошибок сети или запроса
});
fetch(url, [options])
  .then(response => {// Обработка ответа})
  .catch(error => {// Обработка ошибок});
•	url — адрес запроса (строка или объект URL)
•	options (необязательный) — объект с настройками запроса
GET-запрос (Получение данных)
GET — это один из основных HTTP-методов, предназначенный для получения данных с сервера. 
Он используется, когда нужно запросить информацию (например, список пользователей, 
  новости, товары) без изменения состояния сервера.
Давайте рассмотрим пример GET-запроса. Он содержит функцию fetchData(), 
которая делает GET-запрос к тестовому API, обрабатывает успешный ответ, отлавливает возможные ошибки.

fetch('https://api.example.com/data')
.then(res => res.json())
.then(data => console.log(data));
POST-запрос (Отправка данных)
POST — это HTTP-метод, предназначенный для отправки данных на сервер. 
В отличие от GET, который только запрашивает данные, POST используется, когда нужно:

• создать новый ресурс (например, добавить запись в базу данных);

• отправить данные формы (логин, регистрацию, загрузка файлов);

• выполнить действие с побочными эффектами (например, оплату).

Основные особенности POST-запросов
Отправка данных в теле запроса:
— данные не видны в URL (в отличие от GET);

— могут передаваться в разных форматах: JSON, XML, FormData.

Неидемпотентность (различный результат при повторении одного и того же действия):
— повторный POST-запрос может создавать дублирующиеся ресурсы.

Нет ограничения размера данных:
— в отличие от GET, где данные передаются в URL.

Используется для изменений на сервере:
— добавление, обновление или удаление данных.

fetch('https://jsonplaceholder.typicode.com/posts',
{
 method: 'POST',
 headers: { 'Content-Type': 'application/json' },
 body: JSON.stringify({ title: 'Новый пост', body: 'Содержание поста', userId: 1 })
})
 .then(res => res.json())
 .then(data => console.log('Ответ сервера:', data))
 .catch(err => console.error('Ошибка:', err));
PUT-запрос (Обновление данных)
PUT — это HTTP-метод, предназначенный для обновления ресурса на сервере. 
Если ресурса не существует, PUT может создать его с указанным идентификатором.

Основные моменты:

Используем метод PUT вместо POST.
В URL указываем ID изменяемого ресурса.
В теле запроса отправляем только изменяемые поля.
Сервер возвращает обновлённую версию ресурса.
async function updatePost(postId, newData)
{
  const response = await fetch(`https://api.example.com/posts/${postId}`,
   {
    method: 'PUT',  // метод **PUT**
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newData)  // Новые данные для обновления
   });
  return await response.json();
}
const updatedPost = await updatePost(123,
 { title: 'Обновленный заголовок', content: 'Новое содержание поста' });
DELETE-запрос (Удаление данных)
Данный HTTP-запрос DELETE используется для удаления данных на сервере. 
В контексте Fetch API (современного JavaScript-интерфейса для работы с HTTP-запросами) 
DELETE-запросы отправляются с помощью метода fetch() с указанием опций, включая метод DELETE.

Особенности DELETE-запросов:

Не требует тела запроса (обычно передаётся только ID в URL).
Стандартные коды ответа: 200/204 — при успешном удалении, 404 — если ресурс не найден.
Часто требует авторизации (JSON Web Token, API-ключ).
Идемпотентен — повторные запросы дают тот же результат.
fetch(`https://api.example.com/posts/123`, { method: 'DELETE' })
.then(res => res.ok || Promise.reject('Ошибка удаления'))
.then(() => console.log('Удалено'));
Обработка ответов и ошибок
При работе с HTTP-запросами (включая DELETE) важно правильно обрабатывать ответы от сервера и возможные ошибки. 
Это помогает обеспечить стабильность приложения и корректное взаимодействие с пользователем.

const response = await fetch('https://api.example.com/data');
if (response.status === 401)
{ throw new Error('Требуется авторизация'); }
else if (response.status === 404)
{ throw new Error('Данные не найдены'); }
else if (!response.ok)
{ throw new Error(`Ошибка сервера: ${response.status}`); }
//if (response.ok) // Проверяет статусы 200-299
Этот код обеспечивает чёткую и структурированную обработку различных возможных исходов HTTP-запроса. 
Он позволяет отлавливать ошибки и реагировать на них соответствующим образом, 
что делает приложение более надёжным и удобным для пользователя.

Проверка статуса ответа
При работе с HTTP-запросами важно правильно анализировать статус ответа сервера, 
чтобы корректно обрабатывать успешные и ошибочные сценарии.

Сервер возвращает код состояния (status code), который указывает на результат запроса:


Свойство response.ok возвращает true только для статусов 200-299.

Для всех остальных статусов (404, 500 и др.) — false.

Пример кода, который демонстрирует обработку различных статусов HTTP-ответов:

fetch('https://api.example.com/data')
.then(response => {
  switch (response.status)
  {
    case 200:
      return response.json();
    case 400:
      throw new Error('Неверный запрос (400)');
    case 401:
      throw new Error('Не авторизован (401)');
    case 404:
      throw new Error('Ресурс не найден (404)');
    case 500:
      throw new Error('Сервер сломался (500)');
    default:
      throw new Error(`Неизвестная ошибка: ${response.status}`);
  } });
Работа с разными форматами данных

Пример кода, который реализует обработку разных HTTP-статусов на практике:

const response = await fetch('https://api.example.com/data');
const contentType = response.headers.get('content-type');

if (contentType.includes('application/json'))
  { return response.json(); }
else if (contentType.includes('text/html'))
  { return response.text(); }
else
  { return response.blob(); }
Отмена запроса (Класс AbortController)
Иногда нужно прервать HTTP-запрос (например, если пользователь ушёл со страницы или запрос выполняется слишком долго). 
Для этого в JavaScript есть AbortController — класс в JS, который позволяет отменить запрос.

Типичные сценарии:

Пользователь ушёл со страницы (переход по ссылке/закрытие вкладки).

Новый запрос отменил предыдущий (например, поиск с автодополнением).

Таймаут выполнения (сервер не отвечает слишком долго).

Отмена по действию пользователя (кнопка «Отменить загрузку»).

Без отмены:

Движок браузера продолжает обработку ненужного запроса.

Утечки памяти в SPA-приложениях.

Конфликты данных (например, старый и новый ответы поиска).

Пример работы отмены запроса:

let controller = new AbortController();

// Запускаем запрос с возможностью отмены
fetch('https://api.example.com/data',
 { signal: controller.signal })
  .then(response => response.json())
  .catch(error =>
   { if (error.name === 'AbortError') { console.log('Запрос отменен'); } });
// Отменяем запрос через 2 секунды
setTimeout( () => controller.abort(), 2000 );
Настройка CORS и кук
При работе с межсайтовыми запросами (CORS) и аутентификацией через куки важно 
правильно настроить как клиентскую часть (JavaScript), так и сервер. Рассмотрим ключевые моменты.
CORS — механизм, который разрешает или запрещает запросы между разными доменами.
Сервер должен явно разрешить запросы с вашего домена.

fetch('https://api.example.com/data',
 {
  credentials: 'include', // Отправляем куки
  headers: { 'Content-Type': 'application/json' }
})
  .then(response => response.json())
  .then(data => console.log(data));













  Типичные ошибки
Тип ошибки 1: Необработанная ошибка сети (TypeError: Failed to fetch)
Описание:
Возникает при проблемах с соединением или неверном URL. Аналогично попытке позвонить по несуществующему номеру.

Нет интернет-соединения.
URL не существует.
Сервер не отвечает.
Пример ошибки (код):

fetch('https://несуществующий-сайт.рф')
.then(response => response.json())
.then(data => console.log(data));
Объяснение:

Главная проблема — отсутствие обработки ошибок через .catch(), 
из-за чего приложение «падает» при возникновении любых сетевых проблем.

Решение:

fetch('https://jsonplaceholder.typicode.com/posts/9999')
.then(response => {
  if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
  return response.json();
})
.catch(error => console.error('Ошибка:', error.message));
Не забываем про обработку ошибок.







Тип ошибки 2: Отсутствие заголовка Content-Type
Описание:
Сервер не понимает формат данных без заголовка. 
Заголовки — это «инструкция по сборке» для сервера. 
Без них данные есть, но они бесполезны, как детали Lego без инструкции по сборке.

Пример ошибки (код):

fetch('https://example.com/api', {
  method: 'POST',
  body: JSON.stringify({ name: 'John' }) // Заголовок не указан
});
Объяснение:

Сервер не принимает данные или возвращает 400 Bad Request.

Возникает, когда:

отправляется JSON без указания headers.

Решение:

fetch('https://example.com/api', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }, // Важно!
  body: JSON.stringify({ name: 'John' })
});
Явно указываем тип контента для JSON-данных.







Тип ошибки 3: Неправильная обработка ответа
Описание:

Попытка прочитать HTML как JSON. Аналогично попытке прочитать рецепт как ноты.

Пример ошибки (код):

fetch('https://example.com') .then(response => response.json()); // Ошибка, если ответ не JSON
Объяснение:

Ошибка: SyntaxError: Unexpected token < in JSON at position 0

Возникает, когда:

сервер возвращает HTML/текст, а вы пытаетесь вызвать .json().

Решение:

fetch('https://example.com')
.then(response => {
  const contentType = response.headers.get('content-type');
  if (contentType.includes('application/json')) {
    return response.json();
  } else {
    return response.text(); // Или другой формат
  }
});
Проверяем Content-Type ответа.









Тип ошибки 4: Утечка памяти при отмене запроса
Описание:
Неочищенный AbortController занимает память. Как незакрытый кран.

Пример ошибки (код):

let controller = new AbortController();
fetch('https://example.com', { signal: controller.signal });
controller.abort(); // Запрос отменён, но controller не очищен
Объяснение:
Запрос продолжает висеть в памяти после отмены.

Решение:

let controller = new AbortController();
fetch('https://example.com', { signal: controller.signal })
  .catch(err => {
    if (err.name === 'AbortError') console.log('Запрос отменён');
  });
controller.abort();
controller = null; // Очистка
Явно обнуляем контроллер после использования (удаляйте ссылки на AbortController).












Практикум
Задача 1: Получение списка задач
Ситуация:

Вы разрабатываете приложение для управления задачами. 
Нужно получить список задач с тестового API и отобразить их на странице. 
Сервер может вернуть ошибку, если список недоступен.

Задача:

Сделать GET-запрос к https://jsonplaceholder.typicode.com/todos.
Вывести список задач в консоль в формате: [ID] Название задачи (Статус: завершено/не завершено).
Обработать ошибки.
Решение:

async function fetchTasks() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos');

    if (!response.ok) {
      throw new Error(`Ошибка загрузки: ${response.status}`);
    }

    const tasks = await response.json();
    tasks.forEach(task => {
      console.log(`[${task.id}] ${task.title} (Статус: ${task.completed ? 'завершено' : 'не завершено'})`);
    });
  } catch (error) {
    console.error(error.message.includes('status') ? error.message : 'Сервер недоступен');
  }
}

fetchTasks();









Задача 2: Отправка комментария
Ситуация:

В вашем блоге нужно реализовать форму добавления комментариев. 
Пользователь вводит имя и текст, данные отправляются на сервер. 
Сервер может отвергнуть некорректные данные.

Задача:

Создать HTML-форму с полями: name (обязательное, минимум 2 символа), comment (обязательное, минимум 10 символов).
Отправить POST-запрос на https://jsonplaceholder.typicode.com/comments.
Вывести ответ сервера или ошибку.
Решение:

html
<form id="commentForm">
  <input type="text" id="name" placeholder="Ваше имя" required minlength="2">
  <textarea id="comment" placeholder="Текст комментария" required minlength="10"></textarea>
  <button type="submit">Отправить</button>
</form>
<div id="result"></div>

<script>
  document.getElementById('commentForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const comment = document.getElementById('comment').value;
    const resultDiv = document.getElementById('result');

    if (name.length < 2 || comment.length < 10) {
      resultDiv.textContent = 'Проверьте длину имени (от 2 символов) и комментария (от 10 символов)';
      return;
    }

    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, body: comment })
      });

      if (!response.ok) throw new Error(`Ошибка: ${response.status}`);

      const data = await response.json();
      resultDiv.innerHTML = `
        <p>Комментарий отправлен!</p>
        <p>ID: ${data.id}</p>
        <pre>${JSON.stringify(data, null, 2)}</pre>
      `;
    } catch (error) {
      resultDiv.textContent = error.message;
    }
  });
</script>





Итоги:
Сегодня мы:

— узнали, что такое Fetch API и как он упрощает сетевые запросы по сравнению с XMLHttpRequest;

— научились отправлять GET-, POST-, PUT- и DELETE-запросы с помощью Fetch;

— поработали с разными форматами ответов;

— освоили обработку ошибок сети и HTTP-статусов;

— научились отменять запросы с помощью AbortController;

— поработали с CORS и куками в Fetch.

Теперь мы можем делать HTTP-запросы к серверу и обрабатывать ответы, использовать Fetch в для взаимодействия с API.