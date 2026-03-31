Урок №15. События в JavaScript.

Учебные материалы

Сегодня мы разберём одну из ключевых тем в JavaScript — обработку событий.

События происходят повсюду: сработал будильник — вы встаёте, 
наступил день рождения — приходят гости и дарят подарки. Эти действия — реакция на событие.

То же самое происходит и в цифровом мире. Нажали на кнопку смартфона — экран включился. 
Вызвали лифт — он поехал.

Наши сайты тоже должны уметь реагировать: на клик, движение мыши, ввод текста. 
Без специальной настройки элементы страницы останутся «глухими»: никакие действия пользователя не вызовут ответа.

На этом занятии вы узнаете, как сделать сайт интерактивным и «научить» его реагировать на действия пользователя.

Сегодня мы:

разберёмся, как подписываться на события (клики, наведение мыши и другие) и зачем это нужно;
узнаем, что такое всплытие (event bubbling) 
и погружение (event capturing) событий и как они влияют на обработку действий пользователя;
научимся отменять стандартное поведение элементов (например, 
    делать так, чтобы форма не перезагружала страницу при отправке);
поймём, как и зачем останавливать всплытие событий, если оно мешает корректной работе приложения.



Глоссарий к пятнадцатому занятию
Event (Событие)
Event — действие пользователя или браузера (клик, наведение мыши, отправка формы).

Event Handler (Обработчик события)
Event Handler — функция, которая выполняется при наступлении события.

Bubbling (Всплытие)
Bubbling — процесс, когда событие «всплывает» от целевого элемента вверх по DOM-дереву.

Capturing (Погружение)
Capturing — процесс, когда событие «погружается» от корня документа к целевому элементу.

PreventDefault (Отменить действие по умолчанию)
PreventDefault — метод, отменяющий стандартное поведение элемента (например, переход по ссылке).

StopPropagation (Остановка распространения)
StopPropagation — метод, останавливающий всплытие события.


Создание обработчика события
Чтобы элемент на странице реагировал на действия пользователя (например, на клик мышью), 
нужно создать функцию-обработчик события и подписать её на нужное событие.

Подписка
Это процесс прикрепления обработчика к DOM-элементу. При наступлении события (клика, наведения и т. д.) эта функция будет вызвана автоматически.
Существует три способа подписки на событие.

Способ 1: создать атрибут в HTML

<button onclick="alert('Клик!')">Нажми меня</button>
Этот способ очень прост и может показаться удобным, 
так как всё в «одном месте», но именно поэтому он не рекомендуется к использованию: 
смешивание HTML и JS сложно поддерживать, к тому же так можно добавить только один обработчик.

Пример создания атрибута в HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML Attribute Event</title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background: blue;
            margin: 10px;
            cursor: pointer;
            }
    </style>
</head>
<body>


    <!-- Способ 1: обработчик прямо в HTML -->
    <div onclick="alert('Клик по синему блоку!')"></div>
</body>
</html>



Способ 2: свойство элемента в JS

const button = document.querySelector('button');
button.onclick = function()
{ console.log('Клик!'); };
В данном примере мы назначаем созданную функцию обработчиком в коде JS, 
что позволяет отделить логику от разметки, но таким способом можно назначить только один обработчик.

Пример назначения обработчика через свойство элемента

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DOM Property Event</title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background: red;
            margin: 10px;
            cursor: pointer;
            }
    </style>
</head>
<body>
    <div id="redDiv"></div>
    <script>
        const redDiv = document.getElementById('redDiv');
        redDiv.onclick = function()
        { alert('Клик по красному блоку!'); };
    </script>
</body>
</html>


Способ 3: addEventListener – назначение функции определенному событию

button.addEventListener( 'click', function() { console.log('Клик!'); } );
Именно этот способ мы рекомендуем использовать, 
потому что так можно добавлять несколько обработчиков.

Пример назначения нескольких обработчиков события

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>addEventListener Example</title>
    <style>
        div { width: 100px;
              height: 100px;
              background: green;
              margin: 10px;
              cursor: pointer;
            }
    </style>
</head>
<body>
    <div id="greenDiv"></div>

    <script>
        //Использование addEventListener
        const greenDiv = document.getElementById('greenDiv');
        // Первый обработчик
        greenDiv.addEventListener('click', function() {
            alert('Первый обработчик: клик по зелёному блоку!'); });
        // Второй обработчик (не перезаписывает первый)
        greenDiv.addEventListener('click', function() {
            console.log('Второй обработчик: клик залогирован!'); });
    </script>
</body>
</html>

Всплытие и погружение
Когда пользователь взаимодействует со страницей (например, нажимает кнопку) 
событие проходит определённый путь по DOM-дереву. 
Этот путь состоит из двух фаз: погружения (capturing) и всплытия (bubbling).

Что такое всплытие и погружение?

Погружение (capturing): событие начинает путь сверху вниз (от window → document → body → … → целевой элемент).

Фаза цели (target): событие достигает элемента, на котором оно произошло.

Всплытие (bubbling): событие поднимается снизу вверх, 
от целевого элемента к его родителям вплоть до document и window.

По умолчанию обработчики функционируют на фазе всплытия, потому что она используется чаще.

Простой пример всплытия

<div id="parent">
  <button id="child">Кнопка</button>
</div>
const parent = document.getElementById('parent');
const child = document.getElementById('child');
parent.addEventListener('click', () => console.log('Родитель сработал!'));
child.addEventListener('click', () => console.log('Кнопка сработала!'));


При клике на кнопку в консоли будет:

Кнопка сработала!
Родитель сработал! (из-за всплытия).
Как «слушать» на стадии погружения?
Для начала давайте задумаемся: что подразумевается под словом «слушать»? 
На самом деле все довольно просто. 
В JavaScript «слушать» — это зарегистрировать обработчик через метод addEventListener(), 
что переводится с английского как добавитьСлушателяСобытий().

parent.addEventListener('click', () => console.log('Погружение!'), true);
// true = слушаем на стадии погружения
Пример реализации погружения и всплытия

<!DOCTYPE html>
<html>
<head>
    <title>Всплытие и погружение</title>
    <style>
        #grandparent, #parent, #child { padding: 15px; margin: 5px; border: 1px solid #333; }
        #output { margin-top: 10px; padding: 10px; background: #eee; }
    </style>
</head>
<body>
    <button id="toggleCapturing">Вкл/Выкл погружение</button>
    <button id="toggleBubbling">Вкл/Выкл всплытие</button>
    <div id="grandparent">
        Grandparent
        <div id="parent">
            Parent <div id="child">Child (кликни)</div>
        </div>
    </div>
    <div id="output"></div>
    <script>
        const els = ['grandparent', 'parent', 'child'].map(id => document.getElementById(id));
        const [grandparent, parent, child] = els;
        const output = document.getElementById('output');
        let capturing = false;
        let bubbling = true;
        function log(el, phase) { output.innerHTML += `${phase}: ${el.id}<br>`; }
        function setupListeners() {
            els.forEach (el => {
                el.removeEventListener('click', handler, true);
                el.removeEventListener('click', handler, false);
                if (capturing) el.addEventListener('click', handler, true);
                if (bubbling) el.addEventListener('click', handler, false); } ); }
        function handler(e) {
            const phase = e.eventPhase === 1 ? 'CAPTURING' : e.eventPhase === 2 ? 'TARGET' : 'BUBBLING';
            log(this, phase); }
        document.getElementById('toggleCapturing').addEventListener('click', () =>
         { capturing = !capturing; setupListeners(); });
        document.getElementById('toggleBubbling').addEventListener('click', () =>
         { bubbling = !bubbling; setupListeners();});
        setupListeners();
    </script>
</body>
</html>


Рисунок 1
Механизм передачи событий

Рассмотрим механизм передачи событий. При клике на child-элемент:

Если включено погружение: window → document → body → grandparent → parent → child.

Фаза цели: child.

Если включено всплытие: child → parent → grandparent → body → document → window.

Структура DOM выглядит следующим образом: window -> document -> body -> div# grandparent -> div# parent -> div# child.

Отмена стандартного поведения
Перед тем как приступить к вопросу отмены стандартного поведения, 
давайте поймем, что такое стандартное поведение элементов.

Стандартное (дефолтное) поведение — это действия, 
которые браузер выполняет автоматически при определенных событиях:

- <a> — переход по ссылке,
- <form> — отправка данных и перезагрузка страницы,
- <input type="checkbox"> — изменение состояния чекбокса.
Как же мы будем отменять стандартное поведение? 
Основной способ отмены — вызов метода event.preventDefault() в обработчике события.

element.addEventListener('event', function(event)
{
event.preventDefault();
/* Дополнительные действия*/
} );
Пример:

const link = document.querySelector('a');
link.addEventListener ( 'click', (event) =>
  {
  event.preventDefault(); // отменяем переход
  console.log('Клик состоялся, но я никуда не пойду!');
  } );
Пример отмены стандартного поведения элементов

<!DOCTYPE html>
<html>
<head>
    <title>Отмена поведения элементов</title>
    <style>
        #contextDiv { padding: 20px; background: #eee; margin: 10px 0; }
        #output { margin-top: 20px; padding: 10px; background: #f5f5f5; }
    </style>
</head>
<body>
    <div>
        <a href="https://google.com" id="normalLink">Обычная ссылка</a><br>
        <a href="https://google.com" id="preventedLink">Ссылка с preventDefault()</a>
    </div>
    <div id="contextDiv">Правый клик в этой области</div>
    <div id="output"></div><!-- Вывод информации -->
    <script>
        const output = document.getElementById('output');
        // 1. Обработка ссылки
        document.getElementById('preventedLink').addEventListener('click', e => {
            e.preventDefault();
            output.innerHTML += 'Переход по ссылке отменен<br>'; });
        // 2. Отмена контекстного меню
        document.getElementById('contextDiv').addEventListener('contextmenu', e => {
            e.preventDefault();
            output.innerHTML += 'Контекстное меню заблокировано<br>';
        });
    </script>
</body>
</html>

Когда использовать preventDefault()

Кастомная обработка форм (AJAX вместо стандартной отправки).
Одностраничные приложения — SPA (чтобы ссылки не перезагружали страницу).
Специальные обработчики жестов (например, свайпы).
Кастомные элементы управления (свои чекбоксы, выпадающие меню).
Игровая логика (когда нужно перехватить действия пользователя).

Рисунок 2
Отличие от stopPropagation()

preventDefault() — отменяет стандартное действие браузера, 
когда нужно заменить стандартное поведение
stopPropagation() — останавливает всплытие события, 
когда нужно ограничить область срабатывания события.
// Пример совместного использования
element.addEventListener('click', function(e)
{
    e.preventDefault();  // Отменяем действие
    e.stopPropagation(); // Не пускаем событие выше
});
Не все события можно отменить — проверяйте event.cancelable:

if (event.cancelable)
{
    event.preventDefault();
}
Отмена стандартного поведения — мощный инструмент для:

создания интерактивных SPA-приложений,
реализации сложных UI-компонентов,
кастомизации пользовательского опыта.
Важно!
Отменяйте стандартное поведение только тогда, когда вы предоставляете альтернативную логику работы элемента.
Остановка всплытия
Всплытие (event bubbling) — это механизм, при котором событие сначала срабатывает на целевом элементе, 
а затем (последовательно) — на всех его родительских элементах вверх по иерархии DOM.

Если всплытие мешает, его можно остановить с помощью метода stopPropagation(). 
На промежуточном обработчике можно остановить всплытие, если дальнейшая обработка не требуется.

Когда нужно останавливать всплытие?

Когда у родительских элементов есть свои обработчики, которые мешают работе дочернего элемента.
При реализации сложных компонентов (например, выпадающих меню).
Для оптимизации производительности (чтобы не срабатывали лишние обработчики).
child.addEventListener('click', (event) =>
  {
  console.log('Кнопка сработала!');
  event.stopPropagation(); // всплытие не пойдёт дальше
  });
Теперь родительский <div> не получит событие.

Полный пример с остановкой всплытия

<!DOCTYPE html>
<html>
<head>
    <title>Всплытие событий</title>
    <style>
        #grandparent, #parent, #child { padding: 20px; margin: 10px; }
        #grandparent { background: #ffdddd; }
        #parent { background: #ddffdd; }
        #child { background: #ddddff; cursor: pointer; }
        #output { margin-top: 20px; padding: 10px; background: #f5f5f5; }
    </style>
</head>
<body>
    <button id="toggleBubbling">Включить stopPropagation</button>
    <div id="grandparent">
        Grandparent
        <div id="parent">
            Parent
            <div id="child">Child (кликни)</div>
        </div>
    </div>
    <div id="output"></div>
    <script>
        const child = document.getElementById('child');
        const output = document.getElementById('output');
        const toggleBtn = document.getElementById('toggleBubbling');
        let stopPropagation = false;
        function logEvent(element) { output.innerHTML += `Клик: ${element.id}<br>`; }
        document.getElementById('grandparent').addEventListener('click', () => logEvent(grandparent));
        document.getElementById('parent').addEventListener('click', () => logEvent(parent));
        child.addEventListener('click', function(e) {
            logEvent(child);
            if (stopPropagation) {
                e.stopPropagation();
                output.innerHTML += '--- STOPPED ---<br>';
            } });
        toggleBtn.addEventListener('click', function() {
            stopPropagation = !stopPropagation;
            this.textContent = stopPropagation
                ? 'Отключить stopPropagation'
                : 'Включить stopPropagation'; });
    </script>
</body>
</html>

Без остановки всплытия
При клике на child-элемент вывод будет таким:

[time] - Клик на: child
[time] - Клик на: parent
[time] - Клик на: grandparent

С остановкой всплытия

При клике на `child`-элемент с stopPropagation():
[time] - Клик на: child
--- Всплытие остановлено! ---
Если событие «не срабатывает» или работает неожиданно — вы не одни. 





Ниже — частые ошибки, с которыми сталкиваются многие начинающие (и не только) разработчики.





Типичные ошибки
Тип ошибки 1: Не срабатывает обработчик события
Описание:

Ошибка возникает, когда обработчик события не вызывается из-за неправильного назначения 
или ошибок в селекторе. Это как нажимать кнопку на пульте, которая не подключена к устройству.

Пример ошибки (код):

document.querySelector('.non-existent-button').addEventListener('click', () => {
  console.log('Клик!');
});
// Ошибка: Cannot read properties of null (reading 'addEventListener')
Объяснение:

JavaScript пытается добавить обработчик к несуществующему элементу (null), что вызывает ошибку.

Решение:

document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('.my-button');
  if (button) {
    button.addEventListener('click', () => {
      console.log('Клик!');
    });
  } else {
    console.log('Элемент не найден');
  }
});

Всегда Проверяйте существование элементаи перед добавлением обработчика убедитесь, что элемент найден:





Тип ошибки 2: Множественные обработчики (Event listeners stacking)
Описание:

Один и тот же обработчик добавляется несколько раз, вызывая дублирование срабатываний. 
Это как если бы сотрудник записывал ответ анкеты несколько раз подряд.

Пример ошибки (код):

function handleClick() {
  console.log('Клик!');
}
// При каждом вызове добавляется новый обработчик:
document.querySelector('.my-button').addEventListener('click', handleClick);
document.querySelector('.my-button').addEventListener('click', handleClick);
// При клике выведет дважды: "Клик!", "Клик!"
Объяснение:

Каждый вызов addEventListener добавляет новый обработчик, не удаляя старые.

Решение:

const button = document.querySelector('.my-button');
button.removeEventListener('click', handleClick); // Удаляем старый обработчик
button.addEventListener('click', handleClick);    // Добавляем новый
Всегда удаляйте старые обработчики перед добавлением новых









Тип ошибки 3: Потеря контекста this
Описание:

Стрелочные функции не имеют своего this, что приводит к неожиданному поведению. 
Это как если бы сотрудник забыл, к какой анкете относится.

Пример ошибки (код):

const user = {
  name: 'Alex',
  greet: () => {
    console.log(`Привет, ${this.name}!`); // this === window
  }
};
user.greet(); // "Привет, undefined!"

Объяснение:

Стрелочная функция берет this из внешней области (в данном случае — window).

Решение:

const user = {
  name: 'Alex',
  greet() {  // Используем обычную функцию
    console.log(`Привет, ${this.name}!`); // this === user
  }
};
user.greet(); // "Привет, Alex!"

Всегда используйте .bind(this) или сохраняйте контекст в переменную (const self = this), если нужно передать метод как колбэк.








Тип ошибки 4: Всплытие и погружение событий
Описание:

Событие всплывает до родительских элементов, вызывая ненужные обработчики. 
Это как если бы ответ на один вопрос анкеты автоматически заполнял другие.

Пример ошибки (код):

<div id="parent">
  <button id="child">Кнопка</button>
</div>

<script>
  document.getElementById('parent').addEventListener('click', () => {
    console.log('Клик по родителю!'); // Сработает даже при клике на кнопку
  });
</script>
Объяснение:

Событие клика на кнопке всплывает до родительского div.

Решение:

document.getElementById('child').addEventListener('click', (event) => {
  event.stopPropagation(); // Останавливаем всплытие
  console.log('Клик по кнопке!');
});
Всегда применяйте stopPropagation() только когда действительно нужно изолировать событие, так как это может нарушить другие обработчики.






Тип ошибки 5: Событие срабатывает только один раз
Описание:

Обработчик удаляется после первого срабатывания из-за флага { once: true }.
 Это как анкета, которая исчезает после первого ответа.

Пример ошибки (код):

button.addEventListener('click', () => {
  console.log('Клик!');
}, { once: true }); // Обработчик удалится после первого клика
Объяснение:

Флаг once: true автоматически удаляет обработчик после первого выполнения.

Решение:

button.addEventListener('click', () => {
  console.log('Клик!'); // Теперь срабатывает при каждом клике
});
Всегда проверяйте третий аргумент метода, особенно при копировании кода. Убедитесь, что там нет нежелательного { once: true }.

Всегда:

Проверяйте существование элементов.
Удаляйте старые обработчики перед добавлением новых.
Контролируйте контекст this.
Останавливайте всплытие при необходимости.
Избегайте флага once, если событие должно работать многократно.






Практикум
Задача 1: Подсчёт кликов

Ситуация:
Необходимо посчитать, сколько раз пользователь нажал на элемент (например, 
    для аналитики или игровых механик). В этой задаче мы реализуем простой счётчик кликов.

Задача:
Создать кнопку, которая при каждом клике увеличивает счётчик и выводит его значение в консоль.

Шаги реализации:

Создать переменную-счётчик (let counter = 0).
Найти кнопку в DOM.
Добавить обработчик, который увеличивает счётчик и выводит его.
Решение:

<button id="clicker">Кликни меня</button>

<script>
    const button = document.querySelector('#clicker');
    let counter = 0;

    button.addEventListener('click', () => {
        counter++;
        console.log(`Кликов: ${counter}`);
    });
</script>






Задача 2: Отмена действия по умолчанию

Ситуация:
Некоторые элементы (например, ссылки или формы) имеют стандартное поведение 
(переход по URL или отправка данных). Необходимо это поведение отменить.

Задача:
Сделать так, чтобы при клике на ссылку страница не перезагружалась, а в консоль выводилось сообщение.

Шаги реализации:

Найти ссылку в DOM.
Добавить обработчик события click.
Отменить стандартное поведение с помощью event.preventDefault().
Решение:

<a href="https://example.com" id="myLink">Не переходить</a>

<script>
    const link = document.querySelector('#myLink');
    link.addEventListener('click', (event) => {
        event.preventDefault();
        console.log('Переход отменён!');
    });
</script>

Кликните на ссылку: страница не должна перезагружаться; в консоли должно появиться сообщение.

Итоги
На этом занятии мы изучили основы работы с событиями в JavaScript:

разобрали, как подписываться на события с помощью addEventListener;
узнали о фазах событий: погружении (capturing), цели (target) и всплытии (bubbling);
научились управлять поведением событий:
отменять стандартные действия через preventDefault(),
останавливать всплытие с помощью stopPropagation();
рассмотрели примеры всплытия и погружения в DOM-дереве.
