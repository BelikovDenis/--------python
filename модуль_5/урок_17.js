Урок №17. Работа с формами в JavaScript. Продолжение.

Учебные материалы

Теперь ваша задача – создать форму для отправки отзыва на сайте. 
Пользователь заполняет поля, выбирает файл, нажимает «Отправить», и данные уходят на сервер. 
Как сделать так, чтобы данные были собраны правильно и отправились без перезагрузки страницы?

На прошлом занятии мы научились работать с элементами форм, обрабатывать события и проверять данные. 
Сегодня мы пойдём дальше: разберём, как отправлять данные формы, использовать объект FormData; узнаем, 
почему современные разработчики предпочитают fetch и AJAX вместо стандартной отправки. 
Этот урок поможет вам научиться создавать современные веб-приложения с удобной отправкой данных.

На этом занятии мы:

узнаем, что такое HTML-формы и как они используются для сбора данных;
разберём, как обращаться к формам и их элементам с помощью свойства name и методов DOM;
научимся работать с элементами форм(input, textarea, button, select), включая их атрибуты (type, name, required);
освоим обработку данных, введённых пользователем, и управление поведением кнопок в формах;
создадим интерактивную форму, используя JavaScript для обработки пользовательских данных.





Глоссарий к семнадцатому занятию
Submit (отправка формы)

Submit – событие, которое происходит при отправке формы, например при нажатии кнопки <input type="submit">.

Reset (сброс формы)

Reset – событие или действие, очищающее все поля формы до начальных значений.

Action (действие формы)

Action – атрибут <form>, указывающий URL, на который отправляются данные формы.

Method (метод формы)

Method – атрибут <form>, определяющий HTTP-метод запроса (например, GET или POST).

FormData (объект формы)

FormData – JavaScript-объект, позволяющий собирать данные из формы, включая файлы, для отправки на сервер.

Fetch (метод запроса)

Fetch – современный API для выполнения HTTP-запросов, заменяющий устаревший XMLHttpRequest.

AJAX (асинхронная отправка)

AJAX – технология, позволяющая отправлять и получать данные с сервера без перезагрузки страницы.







Теоретический блок
Отправка формы: события submit и reset
HTML-формы предназначены для сбора пользовательских данных и их отправки на сервер. 
Основное событие формы — submit. Оно срабатывает, когда пользователь нажимает кнопку <input type="submit"> 
или <button type="submit">. Это событие сигнализирует, что данные формы готовы к отправке. 
Другое важное событие — reset. Оно очищает форму, возвращая все поля к их начальным значениям, 
указанным в атрибутах value или выбранным по умолчанию.

Представьте форму в виде бумажного бланка: submit — это отправка заполненного бланка в обработку, 
а reset — сброс всех введённых значений формы к исходным.

Пример формы с текстовым полем и двумя кнопками:

<form class="feedback-form">
  <input type="text" class="name-input" name="name" placeholder="Ваше имя">
  <button type="submit">Отправить</button>
  <button type="reset">Очистить</button>
</form>

Обработка события submit в JavaScript:


const form = document.querySelector('.feedback-form');
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Отменяет стандартное поведение браузера
  console.log('Форма отправлена');
});

Метод event.preventDefault() важен, так как без него браузер выполнит стандартное действие: 
отправит данные по адресу, указанному в атрибуте action, и перезагрузит страницу. Это поведение устарело и не подходит для современных приложений.

Событие reset можно обработать аналогично:

form.addEventListener('reset', (event) => {
  console.log('Форма сброшена');
});
Атрибуты action и method
Атрибут action в теге <form> задаёт URL, на который отправляются данные формы, если отправка происходит стандартным способом. Атрибут method определяет тип HTTP-запроса: GET или POST.

GET добавляет данные в строку запроса URL (например, ?email=user@example.com). Подходит для простых запросов, но небезопасен для конфиденциальных данных.
POST отправляет данные в теле запроса (предпочтительный способ для чувствительной информации и файлов).
Пример формы с атрибутами:

<form class="contact-form" action="/submit" method="POST">
  <input type="text" class="email-input" name="email" placeholder="Ваш email">
  <button type="submit">Отправить</button>
</form>
Обработка в JavaScript:

const form = document.querySelector('.contact-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const emailInput = form.querySelector('.email-input');
  const email = emailInput.value.trim();
  console.log(`Email: ${email}`);
});
Этот код позволяет получить значение поля без отправки на сервер, что удобно для валидации.

Объект FormData и его применение
Объект FormData позволяет собирать данные формы в виде пар «ключ – значение». Он автоматически извлекает значения всех элементов с атрибутом name.

Пример формы с текстовым полем и загрузкой файла:

<form class="upload-form">
  <input type="text" name="username" class="username-input" placeholder="Имя пользователя">
  <input type="file" name="photo" class="file-input">
  <button type="submit">Отправить</button>
</form>
Сбор данных с помощью FormData:

const form = document.querySelector('.upload-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  for (let [key, value] of formData.entries()) {
    console.log(`${key}: ${value}`);
  }
});
Обратите внимание: console.log(formData) не показывает содержимое. Используйте entries() или get():

const data = new FormData();
data.append('name', 'Анна');
data.append('file', document.querySelector('.file-input').files[0]);
console.log(data.get('name')); // Анна
Отправка данных с помощью fetch
Современные веб-приложения используют fetch для отправки данных без перезагрузки страницы. Это основа технологии AJAX.

Пример:

const form = document.querySelector('.upload-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  fetch('/api/submit', {
    method: 'POST',
    body: formData
  });
});
Такой подход сохраняет интерфейс активным и удобным для пользователя.

Почему ушли от стандартной отправки
Недостатки стандартной отправки:

Перезагрузка страницы и потеря состояния.
Невозможно отловить ошибки сервера.
Плохой UX: нельзя показать ошибки под полями, сохранить данные, отключить кнопку или показать спинер.
С JavaScript и fetch мы получаем полный контроль и плавный пользовательский опыт.

Валидация формы перед отправкой
Перед отправкой важно проверить корректность данных.

Пример:

const form = document.querySelector('.feedback-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const nameInput = form.querySelector('.name-input');
  const name = nameInput.value.trim();
  if (name.length < 3) {
    console.log('Ошибка: имя должно содержать минимум 3 символа');
    return;
  }
  const formData = new FormData(form);
  console.log('Данные готовы для отправки:', formData.get('name'));
});
Можно расширить валидацию:

email: содержит @ и .;
пароль: длина, символы;
файл: выбран, тип.
Такая проверка делает форму удобной для пользователя и надёжной.

Дальше вас ждут типичные ошибки по работе с формами, а затем – практика!

Типичные ошибки
Тип ошибки 1: Отсутствие event.preventDefault()
Описание:

Без вызова event.preventDefault() форма отправляется стандартно, с перезагрузкой страницы.

Пример ошибки:

const form = document.querySelector('.feedback-form');
form.addEventListener('submit', () => {
  console.log('Форма отправлена'); // Не сработает из-за перезагрузки
});
Решение:

form.addEventListener('submit', (event) => {
  event.preventDefault();
  console.log('Форма отправлена');
});
Объяснение:

Без event.preventDefault() форма отправляется по умолчанию, вызывая перезагрузку страницы. Это прерывает выполнение JavaScript-кода, и обработчик не успевает сработать.

Тип ошибки 2: Неправильное использование FormData
Описание:

Попытка получить данные из FormData без методов, таких как get() или entries().

Пример ошибки:

const formData = new FormData(form);
console.log(formData.username); // undefined
Решение:

console.log(formData.get('username')); // Работает
Объяснение:

FormData не позволяет обращаться к данным через свойства, как к объекту. Попытка получить formData.username возвращает undefined. Нужно использовать методы, такие как get() или entries(), для доступа к значениям.

Тип ошибки 3: Отсутствие атрибута name в полях
Описание:

Если у поля нет атрибута name, оно не попадёт в FormData.

Пример ошибки:

<input type="text" class="username-input">
const formData = new FormData(form);
console.log(formData.get('username')); // null
Решение:

<input type="text" name="username" class="username-input">
Объяснение:

Без атрибута name поле не включается в FormData. Попытка получить значение через formData.get('username') возвращает null, так как поле не связано с ключом.

При работе с формами важно помнить о правильной структуре, атрибутах и методах работы с данными для надёжного взаимодействия с пользователем.

Практикум
Задача 1: Отправка формы с валидацией
Ситуация:

Вы создаёте форму для получения отзывов от пользователей. Необходимо убедиться, что она работает корректно и что пользователь не сможет отправить пустое или слишком короткое имя. Также вы хотите получить доступ к введённым данным, чтобы отправить их на сервер или обработать локально.

Задача:

Создайте форму, в которой есть поле для имени (<input type="text" name="name">), поле для текста отзыва (<textarea name="message">) и кнопка отправки.

При нажатии на кнопку необходимо:

Отменить стандартную отправку формы с помощью event.preventDefault().
Проверить, что имя состоит минимум из 3 символов.
Если имя корректное — вывести имя и сообщение в консоль.
Решение (HTML-структура):

<form class="review-form">
  <input type="text" name="name" class="name-input" placeholder="Имя">
  <textarea name="message" class="message-textarea" placeholder="Отзыв"></textarea>
  <button type="submit">Отправить</button>
</form>
Решение (JavaScript):

const form = document.querySelector('.review-form');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // отменяем стандартную отправку формы

  const formData = new FormData(form); // собираем данные из формы
  const name = formData.get('name').trim(); // получаем значение поля "name"

  if (name.length < 3) {
    console.log('Ошибка: имя должно быть не короче 3 символов');
    return;
  }

  console.log('Имя:', formData.get('name'));
  console.log('Сообщение:', formData.get('message'));
});
Важно:

Без event.preventDefault() форма перезагрузит страницу.
FormData позволяет удобно получить данные.
Всегда проверяйте введённые значения перед отправкой.
Задача 2: Отправка формы с файлом через fetch
Ситуация:

Вы реализуете анкету профиля, в которую пользователь вводит имя, загружает фотографию, выбирает город и вносит информацию о себе. Все данные необходимо собрать и отправить на сервер без перезагрузки страницы.

Задача:

Создайте форму с четырьмя типами полей:

<input type="text" name="username"> — имя пользователя;
<input type="file" name="photo"> — загрузка фото;
<select name="city"> — выбор города из списка;
<textarea name="bio"> — описание пользователя.
Добавьте кнопку отправки. При нажатии:

Отмените стандартную отправку.
Используйте FormData, чтобы собрать данные, включая файл.
Отправьте данные с помощью fetch на https://httpbin.org/post.
Решение (HTML-структура):

<form class="profile-form">
  <input type="text" name="username" class="username-input" placeholder="Имя">
  <input type="file" name="photo" class="file-input">
  <select name="city" class="city-select">
    <option value="moscow">Москва</option>
    <option value="spb">Санкт-Петербург</option>
  </select>
  <textarea name="bio" class="bio-textarea" placeholder="О себе"></textarea>
  <input type="submit" value="Отправить">
</form>
Решение (JavaScript):

const form = document.querySelector('.profile-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form); // собираем все данные формы, включая файл

  fetch('https://httpbin.org/post', {
    method: 'POST',
    body: formData
  })
});
Важно:

FormData автоматически собирает все данные с атрибутами name.
fetch позволяет отправить запрос без перезагрузки.
httpbin.org/post — тестовый сервер, который покажет, какие данные вы отправили.
Итоги:
Сегодня мы:

разобрали, как отправлять данные формы с помощью JavaScript без перезагрузки страницы;
научились использовать объект FormData для сбора данных, включая файлы;
посмотрели, как работать с атрибутами action и method, и поняли, почему они устарели в SPA;
использовали API fetch для отправки формы асинхронно;
освоили базовую валидацию формы перед отправкой;
узнали, какие ошибки часто допускаются при работе с формами.
Теперь вы можете не просто создавать HTML-формы, но и управлять их отправкой программно: с валидацией, сбором данных и отправкой через fetch.