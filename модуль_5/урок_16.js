Урок №16. Работа с формами в JavaScript.

Учебные материалы

Представьте, что вы создаёте веб-приложение, например форму регистрации на сайте. 
Пользователь вводит имя, 
email, выбирает страну из выпадающего списка и нажимает кнопку «Отправить».

Собрать эти данные и обработать их в JavaScript помогают HTML-формы, 
и сегодня мы научимся с ними работать.

На прошлом занятии мы изучили, как обрабатывать события в JavaScript, 
включая клики и взаимодействие с элементами страницы. 
Эти знания станут основой для работы с формами, ведь формы — это не только поля для ввода данных, 
но и события, такие как отправка или изменение значений.


Сегодня мы:

узнаем, что такое HTML-формы и как они используются для сбора данных;
разберём, как обращаться к формам и их элементам с помощью свойства name и методов DOM;
научимся работать с элементами форм (input, textarea, 
    button, select) и их атрибутами (type, name, equired);
освоим обработку данных, введённых пользователем, и управление поведением кнопок в формах;
создадим интерактивную форму, используя JavaScript для обработки пользовательских данных.




Глоссарий к шестнадцатому занятию
Форма (form)
Форма — HTML-элемент <form>, предназначенный для сбора данных от пользователя и 
их отправки на сервер или обработки на стороне клиента.

Свойство (name)
Свойство — атрибут HTML-элементов формы, используемый для их идентификации в JavaScript.

Input (элемент ввода)
Input — HTML-элемент <input>, 
используемый для ввода данных пользователем (например, текст, пароль, чекбокс).

Textarea (текстовое поле)
Textarea — HTML-элемент <textarea>, предназначенный для ввода многострочного текста.

Select (выпадающий список)
Select — HTML-элемент <select>,
 позволяющий пользователю выбрать один или несколько вариантов из списка.

Button (кнопка)
Button — HTML-элемент <button> или <input type="button">, 
используемый для выполнения таких действий, как отправка формы.

Required (обязательное поле)
Required — HTML-атрибут, указывающий, 
что поле формы должно быть заполнено перед отправкой.

Type (тип)
Type — HTML-атрибут элемента <input> или <button>, 
определяющий его поведение (например, text, password, submit).






Что такое формы и какова их роль в веб-разработке
HTML-формы
Это способ взаимодействия с пользователем на веб-странице. 
Они позволяют собирать данные (имя, email или выбор опций) для дальнейшей обработки. 
Представьте, что форма — это анкета в поликлинике: вы указываете имя, возраст, выбираете врача, 
и эти данные отправляются для записи на приём. 
Формы используются повсюду: для регистрации на сайте, поиска в интернет-магазине или заполнения профиля.

На занятии по DOM мы узнали, как находить элементы на странице, 
а на занятии по событиям — как обрабатывать действия пользователя (например, клики). 
Формы объединяют эти знания, так как состоят из элементов, с которыми пользователь взаимодействует, 
и событий, которые мы можем обрабатывать с помощью JavaScript. 
Сегодня мы разберём, как создавать и использовать формы для работы с данными.

Структура формы и атрибут name
Форма создаётся с помощью HTML-тега <form>, который объединяет элементы ввода, 
такие как текстовые поля или кнопки, в одну структуру. 
Чтобы JavaScript мог найти форму, мы используем атрибут name, задающий ей уникальное имя. 
Представьте, что форма — это коробка с анкетой, 
а атрибут name — это наклейка, по которой мы понимаем, что внутри.

Пример создания формы с атрибутом name:

<form name="userForm">
  <input type="text" name="username" placeholder="Введите имя">
  <button type="button">Проверить</button>
</form>
Здесь форма имеет атрибут name="userForm", а текстовое поле — name="username". 
Чтобы получить доступ к форме в JavaScript, используем объект document.forms:

const form = document.forms.userForm;
console.log(form); // Выводит объект формы
console.log(form.username); // Выводит элемент input с name="username"


Альтернативный способ — использовать querySelector:

const form = document.querySelector('form[name="userForm"]');
console.log(form);

Атрибут name позволяет обращаться к элементам формы как к свойствам объекта, что упрощает работу с данными.


Рисунок 1
Работа с элементами форм через JavaScript
JavaScript позволяет получать данные из элементов для интерактивной работы с формами. 
Представьте, что форма — это анкета, а JavaScript — сотрудник, который читает ответы. 
На занятии по DOM мы научились находить элементы, 
а на занятии по событиям — реагировать на действия пользователя. Теперь применим это к формам.

Пример формы:

<form name="userForm">
  <input type="text" name="username" placeholder="Введите имя">
  <button type="button">Проверить</button>
</form>
Получение значения из поля username:

const form = document.querySelector('form[name="userForm"]');
const usernameInput = form.querySelector('input[name="username"]');
console.log(usernameInput.value); // Выводит введённое имя, например "Анна"
Здесь querySelector находит форму и её элементы по атрибуту name.

Обработка событий форм
Чтобы форма реагировала на действия пользователя, 
мы используем события (например, input для ввода текста или click для кнопок). 
Это делает форму динамичной и позволяет обрабатывать данные в реальном времени.

Пример формы:

<form name="inputForm">
  <input type="text" name="message" placeholder="Введите сообщение">
  <button type="button">Показать</button>
</form>
Работа с событием ввода и кнопкой:

const form = document.querySelector('form[name="inputForm"]');
const messageInput = form.querySelector('input[name="message"]');
const button = form.querySelector('button');

// Реакция на ввод текста
messageInput.addEventListener('input', () => {
  console.log(`Сообщение: ${messageInput.value}`);
});

// Реакция на клик по кнопке
button.addEventListener('click', () => {
  console.log(`Вы ввели: ${messageInput.value}`);
});
Событие input отслеживает изменения, а click выводит итоговые данные.

Работа с разными типами элементов
В формах есть чекбоксы, выпадающие списки и другие элементы, 
которые требуют разных подходов в JavaScript. 
Например, для чекбоксов мы используем свойство checked, а для <select> — value.

Пример формы:

<form name="surveyForm">
  <input type="checkbox" name="agree"> Согласен с условиями
  <select name="city">
    <option value="moscow">Москва</option>
    <option value="spb">Санкт-Петербург</option>
  </select>
  <button type="button">Проверить</button>
</form>
Обработка элементов формы:

const form = document.querySelector('form[name="surveyForm"]');
const agreeCheckbox = form.querySelector('input[name="agree"]');
const citySelect = form.querySelector('select[name="city"]');
const button = form.querySelector('button');

button.addEventListener('click', () => {
  console.log(`Согласие: ${agreeCheckbox.checked}`); // true или false
  console.log(`Город: ${citySelect.value}`); // Например, "moscow"
});
Мы проверяем, отмечен ли чекбокс, и получаем выбранный из списка город.

Динамическая проверка данных
JavaScript позволяет не только получать данные, но и проверять их. 
Например, мы можем убедиться, что email содержит @, или подсчитать символы в поле. 
Это равнозначно действиям сотрудника, который проверял бы правильность анкеты.

Пример формы:

<form name="emailForm">
  <input type="text" name="email" placeholder="Введите email">
  <button type="button">Проверить email</button>
</form>
Проверка и обработка email:

const form = document.querySelector('form[name="emailForm"]');
const emailInput = form.querySelector('input[name="email"]');
const button = form.querySelector('button');

button.addEventListener('click', () => {
  const email = emailInput.value;
  if (email.includes('@')) {
    console.log(`Email корректен: ${email}`);
  } else {
    console.log('Введите корректный email');
  }
});

// Подсчёт символов
emailInput.addEventListener('input', () => {
  console.log(`Длина email: ${emailInput.value.length}`);
});

Этот код проверяет email и отображает количество введённых символов.

Предлагаем теперь перейти к типичным ошибкам, а после вас ждет практика!






Типичные ошибки
Тип ошибки 1: Неправильный поиск элемента с помощью querySelector
Описание:

Частая ошибка — неверный селектор в querySelector. 
Из-за этого JavaScript не находит элемент формы. 
Это как искать ответ в анкете, но перепутать название поля.

Пример ошибки (код):

<form name="userForm">
  <input type="text" name="username" placeholder="Введите имя">
</form>
const form = document.querySelector('form[name="userForm"]');
const usernameInput = form.querySelector('input[name="user"]'); // Ошибка: неверное имя
console.log(usernameInput.value); // Ошибка: Cannot read property 'value' of null

Объяснение:

JavaScript не может найти элемент с name="user", 
потому что такого нет в форме. Получается null, и попытка получить value приводит к ошибке.

Решение:

const usernameInput = form.querySelector('input[name="username"]'); // Правильное имя
console.log(usernameInput.value); // Работает

Всегда проверяйте, что селектор в querySelector соответствует атрибуту name.





Тип ошибки 2: Использование value вместо checked для чекбоксов
Описание:

При работе с чекбоксами новички часто используют value вместо checked, 
что не даёт нужного результата. 
Это как читать текст галочки вместо того, чтобы проверить, отмечена ли она.

Пример ошибки (код):

<form name="surveyForm">
  <input type="checkbox" name="agree"> Согласен
</form>
const form = document.querySelector('form[name="surveyForm"]');
const agreeCheckbox = form.querySelector('input[name="agree"]');
console.log(agreeCheckbox.value); // Ошибка: выводит "on" или пустую строку
Объяснение:

value показывает значение, записанное в атрибуте, но не показывает, 
выбран ли чекбокс. Чтобы узнать, установлен ли он, нужно использовать checked.

Решение:

console.log(agreeCheckbox.checked); // true или false
Для чекбоксов используйте checked, чтобы узнать, отмечены ли они.





Тип ошибки 3: Неправильная обработка события input
Описание:

Иногда разработчики забывают, что событие input срабатывает при каждом изменении, 
и пишут код, который работает некорректно. 
Это как сотрудник, который реагирует на каждый символ в анкете, но не проверяет данные.

Пример ошибки (код):

<form name="textForm">
  <input type="text" name="message" placeholder="Введите текст">
</form>
const form = document.querySelector('form[name="textForm"]');
const messageInput = form.querySelector('input[name="message"]');
messageInput.addEventListener('input', () => {
  if (messageInput.value === 'привет') { // Ошибка: проверка точного совпадения
    console.log('Вы ввели привет');
  }
});


Объяснение:

Такой код реагирует только на строгое совпадение со словом «привет» и не работает в случае, 
когда пользователь ещё не закончил ввод.

Решение:

messageInput.addEventListener('input', () => {
  const value = messageInput.value.toLowerCase();
  if (value.includes('привет')) { // Более гибкая проверка
    console.log('Вы ввели привет');
  }
});

Проверяйте данные в обработчике input гибко, учитывая частичный ввод.







Тип ошибки 4: Игнорирование проверки существования элемента
Описание:

Если элемент не найден через querySelector, 
попытка получить его свойства вызовет ошибку. 
Это как пытаться прочитать ответ из несуществующего поля анкеты.

Пример ошибки (код):

<form name="dataForm">
  <input type="text" name="email">
</form>
const form = document.querySelector('form[name="dataForm"]');
const emailInput = form.querySelector('input[name="emailAddress"]'); // Ошибка: элемент не существует
console.log(emailInput.value); // Ошибка: Cannot read property 'value' of null

Объяснение:

JavaScript не находит элемент, потому что имя поля задано неверно. 
Это приводит к попытке обращения к null.

Решение:

const emailInput = form.querySelector('input[name="emailAddress"]');
if (emailInput) {
  console.log(emailInput.value);
} else {
  console.log('Поле email не найдено');
}

Перед доступом к свойствам элемента проверяйте, найден ли он.






Тип ошибки 5: Некорректная логика проверки данных
Описание:

При проверке данных (например, email) новички часто пишут неполные условия, 
что приводит к ошибкам. Это как сотрудник, который проверяет анкету, но упускает важные детали.

Пример ошибки (код):

<form name="emailForm">
  <input type="text" name="email" placeholder="Введите email">
  <button type="button">Проверить</button>
</form>
const form = document.querySelector('form[name="emailForm"]');
const emailInput = form.querySelector('input[name="email"]');
const button = form.querySelector('button');

button.addEventListener('click', () => {
  const email = emailInput.value;
  if (email.includes('@')) { // Ошибка: слишком простая проверка
    console.log('Email корректен');
  } else {
    console.log('Email некорректен');
  }
});

Объяснение:

Проверка по наличию только символа @ слишком слабая и может пропустить некорректные адреса.

Решение:

button.addEventListener('click', () => {
  const email = emailInput.value.trim();
  if (email.includes('@') && email.includes('.') && email.length > 5) {
    console.log('Email корректен');
  } else {
    console.log('Введите корректный email');
  }
});

Добавляйте дополнительные проверки (длина, наличие точки) для точной валидации.

В работе с формами важно всегда внимательно проверять селекторы, имена, типы данных и учитывать особенности работы событий.










Практикум
Задача 1: Вывод текста из поля

Ситуация:
Пользователь вводит текст в поле формы, и вы хотите показать этот текст в консоли по нажатию кнопки.

Задача:
Создайте форму с текстовым полем и кнопкой. При клике на кнопку выведите значение поля в консоль.

Решение:

<form class="text-form">
  <input type="text" class="text-input" placeholder="Введите текст">
  <button type="button" class="check-button">Показать</button>
</form>
const form = document.querySelector('.text-form');
const textInput = form.querySelector('.text-input');
const button = form.querySelector('.check-button');

button.addEventListener('click', () => {
  console.log(`Текст: ${textInput.value}`);
});











Задача 2: Работа с чекбоксом и выпадающим списком

Ситуация:
Пользователь заполняет форму, выбирая город из списка и отмечая согласие с условиями. 
Вы хотите проверить этот выбор по нажатию кнопки.

Задача:
Создайте форму с чекбоксом, выпадающим списком и кнопкой. 
При клике на кнопку выведите в консоль: отмечен чекбокс или нет, какой город выбран.

Решение:

<form class="survey-form">
  <input type="checkbox" class="agree-checkbox"> Согласен с условиями
  <select class="city-select">
    <option value="moscow">Москва</option>
    <option value="spb">Санкт-Петербург</option>
    <option value="kazan">Казань</option>
  </select>
  <button type="button" class="submit-button">Проверить</button>
</form>
const form = document.querySelector('.survey-form');
const agreeCheckbox = form.querySelector('.agree-checkbox');
const citySelect = form.querySelector('.city-select');
const button = form.querySelector('.submit-button');

button.addEventListener('click', () => {
  console.log(`Согласие: ${agreeCheckbox.checked}`);
  console.log(`Выбранный город: ${citySelect.value}`);
});







Итоги
На этом занятии мы:

разобрались, что такое HTML-формы и как они помогают собирать данные пользователей;
изучили, как находить элементы форм с помощью querySelector для работы с данными;
научились обрабатывать события форм, такие как ввод текста и клики по кнопкам;
освоили работу с разными элементами форм, включая чекбоксы и выпадающие списки;
узнали, как проверять данные (например, корректность email) с помощью JavaScript.
Теперь вы умеете создавать интерактивные формы, 
которые реагируют на действия пользователей и обрабатывают их данные. 
Эти навыки позволят вам разрабатывать удобные веб-приложения (например, формы регистрации или анкеты).