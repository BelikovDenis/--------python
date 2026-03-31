Урок №12. Flexbox: продвинутое использование.



Учебные материалы
Мы уже научились использовать Flexbox для создания адаптивных интерфейсов: 
выстраивать элементы в строку или колонку, управлять их размером и отступами. 
Но на практике часто возникает необходимость более точного контроля: 
выравнивания по центру, распределения элементов между собой, индивидуального позиционирования карточек.


Сегодня мы:

изучим свойства justify-content, align-item и align-content, 
предназначенные для выравнивания элементов по главной и поперечной оси;
разберёмся, как использовать order для управления порядком отображения элементов;
освоим align-self для индивидуального выравнивания конкретного элемента в контейнере;
потренируемся: создадим адаптивные галереи и каталоги с использованием продвинутых приёмов Flexbox.






Глоссарий к двенадцатому занятию
Justify-content (Выравнивание контента по главной оси)

Justify-content — свойство для выравнивания Flex-элементов вдоль главной оси. 
Например, justify-content можно использовать для расположения контейнера по центру видимой части страницы.

Align-items (Выравнивание контента по поперечной оси)

Align-items — свойство, которое задает выравнивание Flex-элементов вдоль поперечной оси.

Align-content (Выравнивание контента)

Align-content — свойство, которое управляет выравниванием Flex-элементов в контейнере.





В модели Flexbox выравнивание элементов играет ключевую роль: оно определяет, 
как объекты располагаются внутри контейнера, 
как реагируют на изменение ширины экрана и как заполняют доступное пространство.

В Flexbox используется несколько свойств для выравнивания:

justify-content — выравнивание элементов вдоль главной оси (обычно по горизонтали);
align-items — выравнивание вдоль поперечной оси (обычно по вертикали);
align-content — распределение строк внутри контейнера при использовании flex-wrap.
Каждое из этих свойств имеет несколько вариантов поведения 
и используется в разных ситуациях. Начнём с justify-content.

Свойство justify-content

Создадим три объекта box в контейнере container:

<div class="container">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
</div>

Стилизуем созданные элементы, чтобы изучить возможности justify-content:

.box {
    width: 50px;
    height: 50px;
    background-color: violet;
    border: 2px solid black;
    text-align: center;
}
Свойство justify-content определяет, как Flex-элементы распределяются вдоль главной оси внутри флекс-контейнера.

flex-start
Рассмотрим использование justify-content со значением flex-start. 
Элементы выравниваются у начала главной оси. 
Например, если ряд Flex-элементов начинается слева, будет использовано выравнивание слева направо.

.container {
    display: flex;
    justify-content: flex-start;
}

В результате применения выравнивания данного типа все элементы сжимаются к началу контейнера.

flex-end
При использовании значения flex-end элементы контейнера выравниваются у конца главной оси. 
Так, если элементы используют направление слева направо, при использовании flex-end они будут выровнены справа.

.container {
    display: flex;
    justify-content: flex-end;
}

Наши блоки теперь прижаты к противоположному краю контейнера.

center
При использовании значения center элементы располагаются по центру главной оси.

.container {
    display: flex;
    justify-content: center;
}

Теперь все элементы контейнера собираются в центре.

Мы рассмотрели значения justify-content, которые позволяют выровнять объекты. 
Теперь рассмотрим значения этого свойства, которые позволяют распределить элементы в контейнере.

space-between
При использовании этого значения первый элемент контейнера располагается у начала главной оси, 
а последний — у её конца. Промежуточные элементы распределяются в контейнере равномерно.

.container {
    display: flex;
    justify-content: space-between;
}

Нам удалось задать равные промежутки между элементами. Однако по краям контейнера пространства нет.

space-around
При использовании этого значения элементы распределяются равномерно, 
а внешние промежутки составляют половину внутреннего.

.container {
    display: flex;
    justify-content: space-around;
}

Пространство между элементами распределено равномерно, 
однако внешние промежутки меньше внутренних.

space-evenly
Пространство между элементами, а также внешние границы равны.

.container {
    display: flex;
    justify-content: space-evenly;
}

Расстояние между всеми элементами, 
а также между элементами и краями контейнера одинаковое.

Свойство align-items

Свойство align-items определяет, как Flex-элементы выравниваются вдоль поперечной оси (перпендикулярной главной оси).

stretch
Это значение применяется по умолчанию. 
Элементы растягиваются, чтобы заполнить доступное пространство вдоль поперечной оси. 
Растягивание не применяется, если для элемента задана фиксированная высота.

.container {
    display: flex;
    align-items: stretch;
}
Для демонстрации работы этого свойства изменим наш код. Добавим рамку контейнера:

.container {
    display: flex;
    align-items: stretch;
    border: 2px solid black;
    width: 150px;
    height: 150px;
}
Если для элемента указана фиксированная высота, свойство stretch не будет применено:

.box {
    width: 50px; /** Фиксированная ширина **/
    height: 50px; /** Фиксированная высота **/
    background-color: violet;
    border: 2px solid black;
    text-align: center;
}

Изменим стили элемента, уберём значение высоты элемента:

.box {
    width: 50px;
    background-color: violet;
    border: 2px solid black;
    text-align: center;
}

Элементы растянулись по контейнеру.

flex-start
Элементы выравниваются у начала поперечной оси.

.container {
    display: flex;
    align-items: flex-start;
}

Все элементы выровнены по верхнему краю.

flex-end
Элементы выравниваются у конца поперечной оси.

.container {
    display: flex;
    align-items: flex-end;
}

Все элементы прижаты к нижнему краю.

center
Элементы выравниваются по центру поперечной оси.

.container {
    display: flex;
    align-items: center;
}

Все элементы располагаются в центре поперечной оси.

baseline
Элементы выравниваются по их текстовой базовой линии. 
Это значение обычно используется при работе с текстовыми элементами или элементами с различной высотой.

Свойство align-content

Свойство align-content управляет распределением Flex-элементов вдоль поперечной оси внутри контейнера. 
Оно применяется только при использовании свойства flex-wrap.

Свойство align-content принимает аналогичные значения: stretch, flex-start, flex-end, center и другие.

Например, при использовании значений flex-start и wrap элементы, 
которые помещаются в размер контейнера, будут располагаться у начала поперечной оси, 
последний элемент будет размещен у конца оси, 
а промежутки между строками элементов будут распределены равномерно.

.container {
    display: flex;
    flex-wrap: wrap;
    align-content: space-between;
}

В этом примере блоки с числами 1 и 2 помещаются в одну строку, 
а для блока 3 места уже не хватает. 
Поскольку блок 3 является последним в контейнере, он помещается в конец оси.


В этом примере в строку может поместиться только один элемент. 
Поэтому все элементы распределяются равномерно по поперечной оси.

Свойство order

Свойство order в CSS задаёт порядок, в котором Flex-элементы располагаются внутри контейнера.

.item {
    order: <число>;
}
Как работает order:

Все элементы по умолчанию имеют order: 0.
Элементы с меньшим значением order располагаются ближе к началу.
Если значения order равны, элементы отображаются в порядке их появления в HTML.
<div class="container">
  <div class="item" style="order: 3;">Элемент 1</div>
  <div class="item" style="order: 1;">Элемент 2</div>
  <div class="item" style="order: 2;">Элемент 3</div>
</div>

<style>
  .container {
      display: flex;
      border: 1px solid black;
      gap: 10px;
  }
  .item {
      padding: 10px;
      background-color: lightblue;
      text-align: center;
  }
</style>

Элементы будут отображаться в следующем порядке: Элемент 2 → Элемент 3 → Элемент 1.

Свойство align-self

Свойство align-self позволяет изменить выравнивание для одного Flex-элемента вдоль поперечной оси. 
Оно переопределяет значение, заданное для контейнера через align-items.

<div class="container">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box" style="align-self: end;">3</div>
</div>

В этом примере мы применили align-self к третьему блоку, 
чтобы задать уникальное расположение для этого элемента.







Типичные ошибки
Тип ошибки 1: Неправильное использование свойств justify-content и align-items

Использование justify-content для вертикального выравнивания элементов 
или align-items — для горизонтального выравнивания элементов.

Пример ошибки:

.container {
  display: flex;
  justify-content: center; /* Требуется вертикальное выравнивание, но это свойство подходит для горизонтального выравнивания */
}

Решение:

Для вертикального выравнивания используйте align-items, а для горизонтального выравнивания — justify-content.

.container {
  display: flex;
  flex-direction: column; /* Установка направления flexbox на column для вертикального расположения */
  align-items: center; /* Вертикальное выравнивание элементов */
}





Тип ошибки 2: Неправильное использование align-self

Свойство align-self не будет выполнять ожидаемую функцию, 
если оно изменяет выравнивание элемента относительно перпендикулярной оси 
flex-контейнера (в данном случае — по вертикали).

Пример ошибки:

.container {
  display: flex;
  align-items: flex-start; /* Выравнивание по умолчанию для всех элементов */
}

.item {
  align-self: center; /* Попытка вертикального выравнивания одного элемента */
}

Решение:

Чтобы свойство align-self заработало в вертикальном направлении, 
контейнер должен быть переориентирован на вертикальный поток с помощью flex-direction: column.

.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Выравнивание по умолчанию для всех элементов */
}

.item {
  align-self: center; /* Вертикальное выравнивание одного элемента */
}






Практикум
Задача 1: Создание сетки галереи с использованием Flexbox

Ситуация: вы разрабатываете адаптивную галерею изображений для веб-сайта. 
Необходимо использовать Flexbox для организации элементов в виде сетки. 
Изображения должны быть равномерно распределены в контейнере 
и иметь возможность адаптации к разным размерам экрана.

Требования:

Использовать Flexbox для создания адаптивной сетки.
Настроить flex-wrap, чтобы элементы автоматически переходили на новую строку при уменьшении доступного пространства.
Применить свойства justify-content и align-content для управления выравниванием элементов в контейнере.
Добавить стили к изображениям, чтобы они оставались пропорциональными и занимали всё доступное место в карточке.
Задача: cоздайте галерею, 
в которой изображения равномерно распределены в контейнере с возможностью адаптации к разным размерам экрана. 
Добавьте примеры различных комбинаций justify-content и align-content.

Шаги реализации:

В <head> подключается внешний файл стилей styles.css. Название страницы: «Галерея изображений».
Внутри тега <body> создайте контейнер с классом gallery-container. 
Внутри контейнера добавьте 8 изображений, обёрнутых в элементы с классом gallery-item.
Пример изображений: <img src="image1.jpg" alt="Изображение 1">, <img src="image2.jpg" alt="Изображение 2"> и так далее.
Для демонстрации работы выравнивания создайте несколько секций с различными настройками justify-content и align-content.
<section>
    <h2>Justify Content: Space Between</h2>
    <div class="gallery-container space-between">
        <!-- Элементы галереи -->
    </div>
</section>
Стили для контейнера галереи:
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center; /* Горизонтальное выравнивание */
    align-content: flex-start; /* Вертикальное выравнивание */
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
}
Стили для элементов галереи:
.gallery-item {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: calc(25% - 20px); /* Четыре элемента в строке */
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
}

Реализация:

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Галерея изображений</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section>
        <h2>Justify Content: Space Between</h2>
        <div class="gallery-container space-between">
            <div class="gallery-item"><img decoding="async" src="image1.jpg" alt="Изображение 1"></div>
            <div class="gallery-item"><img decoding="async" src="image2.jpg" alt="Изображение 2"></div>
            <div class="gallery-item"><img decoding="async" src="image3.jpg" alt="Изображение 3"></div>
            <div class="gallery-item"><img decoding="async" src="image4.jpg" alt="Изображение 4"></div>
        </div>
    </section>

    <section>
        <h2>Align Content: Center</h2>
        <div class="gallery-container center">
            <div class="gallery-item"><img decoding="async" src="image5.jpg" alt="Изображение 5"></div>
            <div class="gallery-item"><img decoding="async" src="image6.jpg" alt="Изображение 6"></div>
            <div class="gallery-item"><img decoding="async" src="image7.jpg" alt="Изображение 7"></div>
            <div class="gallery-item"><img decoding="async" src="image8.jpg" alt="Изображение 8"></div>
        </div>
    </section>
</body>
</html>

/* Основные стили */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

/* Контейнер галереи */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    border-radius: 10px;
    background-color: #f9f9f9;
}

.gallery-container.space-between {
    justify-content: space-between;
}

.gallery-container.center {
    align-content: center;
}

/* Элементы галереи */
.gallery-item {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: calc(25% - 20px); /* Четыре элемента в строке */
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
}






Задача 2: Создание простого каталога товаров с использованием Flexbox

Ситуация: вы разрабатываете упрощённый адаптивный каталог товаров для интернет-магазина. 
Карточки товаров должны быть организованы с использованием Flexbox, 
равномерно распределяться в контейнере и адаптироваться к разным размерам экрана.

Требования:

Использовать Flexbox для создания адаптивного каталога.
Настроить flex-wrap, чтобы карточки автоматически переносились на новую строку при недостатке места.
Применить свойства justify-content и align-items для управления выравниванием карточек.
Упростить карточки товаров: каждая должна содержать только изображение и заголовок.
Задача: создайте каталог товаров с минималистичными карточками, 
где изображения и заголовки равномерно распределены в контейнере и адаптируются к разным экранам.

Шаги реализации:

Создайте базовую HTML-страницу с минимальной разметкой. 
Подключите внешний файл стилей для оформления. 
В контейнере разместите карточки товаров, содержащие изображение и заголовок.

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог товаров</title>
    <link rel="stylesheet" href="catalog.css">
</head>
<body>
    <h1>Каталог товаров</h1>

    <!-- Первая секция -->
    <section>
        <h2>Justify Content: Space Evenly</h2>
        <div class="catalog-container space-evenly">
            <div class="catalog-item">
                <img decoding="async" src="product1.jpg" alt="Товар 1">
                <h3>Товар 1</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product2.jpg" alt="Товар 2">
                <h3>Товар 2</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product3.jpg" alt="Товар 3">
                <h3>Товар 3</h3>
            </div>
        </div>
    </section>

    <!-- Вторая секция -->
    <section>
        <h2>Align Items: Flex-Start</h2>
        <div class="catalog-container flex-start">
            <div class="catalog-item">
                <img decoding="async" src="product4.jpg" alt="Товар 4">
                <h3>Товар 4</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product5.jpg" alt="Товар 5">
                <h3>Товар 5</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product6.jpg" alt="Товар 6">
                <h3>Товар 6</h3>
            </div>
        </div>
    </section>
</body>
</html>

Создайте файл catalog.css и добавьте стили для элементов страницы.
Добавьте стили для body и заголовков, чтобы задать фон, отступы и шрифты.
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}
h1, h2 {
    text-align: center;
    color: #333;
}
Используйте Flexbox для создания адаптивной сетки. Настройте выравнивание с помощью классов.
.catalog-container {
    display: flex;
    flex-wrap: wrap; /* Позволяет элементам переноситься на новую строку */
    gap: 20px; /* Промежуток между карточками */
    padding: 20px;
    border-radius: 10px;
    background-color: #eaeaea;
}

.catalog-container.space-evenly {
      justify-content: space-evenly; /* Равномерное распределение карточек */
}

.catalog-container.flex-start {
      align-items: flex-start; /* Вертикальное выравнивание по началу */
}
Задайте размеры карточек, цвет фона, тень и оформление текста. 
Используйте flex-basis для задания ширины карточек.
.catalog-item {
    flex-grow: 1; /* Карточки растягиваются для равномерного заполнения */
    flex-shrink: 1; /* Карточки уменьшаются при нехватке места */
    flex-basis: calc(30% - 20px); /* Задаёт ширину карточки (три на строку) */
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    padding: 10px;
}
Настройте изображения так, 
чтобы они занимали всю доступную ширину карточки и оставались пропорциональными. 
Заголовки сделайте читаемыми и стилистически оформленными.
.catalog-item img {
    width: 100%; /* Изображение занимает всю ширину карточки */
    height: auto; /* Пропорциональное масштабирование */
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
}
.catalog-item h3 {
    font-size: 1.2em;
    color: #333;
}
Реализация:

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог товаров</title>
    <link rel="stylesheet" href="catalog.css">
</head>
<body>
    <section>
        <h2>Justify Content: Space Evenly</h2>
        <div class="catalog-container space-evenly">
            <div class="catalog-item">
                <img decoding="async" src="product1.jpg" alt="Товар 1">
                <h3>Товар 1</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product2.jpg" alt="Товар 2">
                <h3>Товар 2</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product3.jpg" alt="Товар 3">
                <h3>Товар 3</h3>
            </div>
        </div>
    </section>

    <section>
        <h2>Align Items: Flex-Start</h2>
        <div class="catalog-container flex-start">
            <div class="catalog-item">
                <img decoding="async" src="product4.jpg" alt="Товар 4">
                <h3>Товар 4</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product5.jpg" alt="Товар 5">
                <h3>Товар 5</h3>
            </div>
            <div class="catalog-item">
                <img decoding="async" src="product6.jpg" alt="Товар 6">
                <h3>Товар 6</h3>
            </div>
        </div>
    </section>
</body>
</html>


/* Основные стили */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

/* Контейнер каталога */
.catalog-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    border-radius: 10px;
    background-color: #eaeaea;
}

/* Выравнивание в разных секциях */
.catalog-container.space-evenly {
    justify-content: space-evenly;
}

.catalog-container.flex-start {
    align-items: flex-start;
}

/* Карточки товаров */
.catalog-item {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: calc(30% - 20px); /* Три карточки в строке */
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    padding: 10px;
}

/* Стили для изображения */
.catalog-item img {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
}

/* Заголовок карточки */
.catalog-item h3 {
    font-size: 1.2em;
    color: #333;
}





Итоги:
На этом занятии мы изучили продвинутые возможности работы с Flexbox:

научились задавать выравнивание по главной оси с помощью justify-content;
освоили работу с align-items для выравнивания по поперечной оcи;
научились работать с align-content для выравнивания пространства между элементами внутри контейнера;
изучили свойства order для установления порядка отображения элементов в контейнере;
узнали, как использовать align-self для изменения выравнивания одного элемента Flex-контейнера.
В следующем занятии мы научимся работать с медиазапросами.