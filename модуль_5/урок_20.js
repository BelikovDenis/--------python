Урок №20. Async/await. 

Учебные материалы

На прошлом занятии мы изучили промисы — эффективный инструмент для работы с асинхронными операциями, 
который помогает избегать callback hell и делает код более линейным. 
Сегодня мы познакомимся с async/await — современным синтаксисом, 
который делает асинхронный код ещё проще и читаемем, позволяя писать его так, будто он синхронный.

Представим, что вы делаете ужин: вместо того чтобы постоянно проверять, 
готова ли каждая часть блюда (как с колбэками или промисами), вы просто ждёте, 
пока каждый этап завершится, и продолжаете дальше. 
Async/await работает аналогично, позволяя приостанавливать выполнение функции до завершения асинхронной операции.

Сегодня мы:

узнаем, что такое ключевые слова async и await и как они упрощают асинхронный код;
научимся писать асинхронные функции с async/await, которые выглядят как синхронные;
разберём, как await приостанавливает выполнение асинхронной функции до завершения промиса;
освоим использование await в циклах для последовательной обработки асинхронных операций;
перепишем код на промисах с использованием async/await, чтобы сравнить подходы;
поймём, как async/await помогает окончательно избавиться от callback hell в цепочках промисов.

После занятия мы сможем писать читаемый и надёжный асинхронный код, используя современный синтаксис async/await.

Глоссарий к двадцатому занятию
Async (Асинхронный)
Async — ключевое слово, обозначающее асинхронную функцию, которая всегда возвращает промис.

Await (Ожидание)
Await — ключевое слово, используемое внутри async-функции для приостановки выполнения до завершения промиса.

Асинхронная функция
Асинхронная функция — функция, объявленная с async, которая позволяет использовать await для работы с промисами.

Try/catch (Трай кэч)
Try/catch — конструкция для обработки ошибок в async/await, аналогичная .catch() для промисов.

Callback hell (Колбэк)
Callback hell — проблема вложенных колбэков, которую async/await решает, делая код более линейным.





Что такое async/await и зачем они нужны?
Представим, что вы готовите сложный ужин: суп, основное блюдо и десерт. 
С обычными промисами из прошлого занятия вы как будто бегаете между кастрюлями, 
постоянно проверяя, готово ли содержимое, и вручную передаёте результаты дальше (через .then()). 
Это работает, но выглядит громоздко, особенно если у вас куча шагов. 
А теперь вообразим, что у вас есть суперумный помощник, который говорит: «Я сам дождусь, 
пока суп закипит, потом начну жарить мясо, а затем подам десерт». 
Вы просто даёте ему инструкции, а он всё делает по порядку и без суеты. 
Этот помощник и есть async/await — современный способ писать асинхронный код в JavaScript, 
который появился в 2017-м году и сделал жизнь разработчиков проще.

Async/await — это как обёртка вокруг промисов, которая позволяет писать код так, 
будто он синхронный, хотя на самом деле он ждёт асинхронные операции (например, 
    загрузку данных с сервера или таймер). Это не новый механизм, а удобный синтаксис, 
    чтобы не запутаться в цепочках .then() и не утонуть в callback hell — той самой «пирамиде» вложенных функций, 
    о которой мы говорили на прошлом занятии.

Для чего они нужны?
Читаемость: код выглядит как обычная последовательность шагов, без кучи .then(). 
Это как писать рассказ, а не инструкцию для робота.
Проще ловить ошибки: вместо .catch() используем try/catch, 
как в обычном коде, это интуитивно понятно.
Логичная последовательность: легко выстраивать шаги один за другим, 
особенно если одна операция зависит от другой.
Меньше callback hell: помните, как на прошлом занятии мы превратили вложенные колбэки 
в линейную цепочку промисов? Async/await делает это ещё проще.

Пример из жизни (и кода)

Допустим, вы заказываете пиццу (как на прошлом занятии). 
С колбэками вы звоните в пиццерию, потом ждёте звонка о готовности, 
затем сами проверяете статус доставки — куча вложенных функций. 
С промисами вы упростили это до цепочки .then(), 
а с async/await вы просто говорите: «Приготовь пиццу, потом доставь её, я жду».

Вот как это выглядит.

Колбэк-версия (из прошлого занятия):

orderPizza(function(pizza) {
  deliverPizza(pizza, function(delivery) {
    console.log('Пицца доставлена: ' + delivery);
  });
});

Промис-версия (из прошлого занятия):

orderPizza()
  .then(pizza => deliverPizza(pizza))
  .then(delivery => console.log('Пицца доставлена: ' + delivery))
  .catch(error => console.log('Ой, что-то пошло не так: ' + error));
Async/await-версия (сегодня):

async function getPizza() {
  try {
    const pizza = await orderPizza();
    const delivery = await deliverPizza(pizza);
    console.log('Пицца доставлена: ' + delivery);
  } catch (error) {
    console.log('Ой, что-то пошло не так: ' + error);
  }
}
getPizza();

Код с async/await читается как книга: сначала одно, потом другое, а если что-то ломается, 
ловим ошибку. Никаких вложенных функций или длинных цепочек!


Рисунок 1
Когда использовать async/await?
Когда загружаем данные с сервера (например, список друзей или вопросы для викторины).
Когда нужно выполнить несколько асинхронных операций по очереди (например, 
    проверить профиль, потом загрузить достижения).
Когда хотим, чтобы код был понятен даже новичку, который только что открыл ваш проект.
Как работает async/await?
Async/await — это не магия, а просто удобный способ работать с промисами. 
Давайте разберём, как они устроены.

async: если мы ставим это слово перед функцией, она становится асинхронной и всегда возвращает промис. 
Даже если мы вернём число или строку, JavaScript автоматически завернёт это в промис.
await: это слово можно использовать только внутри async-функций. 
Оно говорит: «Стоп, подожди, пока этот промис не завершится, 
и дай мне его результат». Если промис отклоняется, await выбросит ошибку, которую можно поймать через try/catch.
Пример: ждём пиццу

async function makePizza() {
  const pizza = await new Promise(resolve => {
    setTimeout(() => resolve('Пицца готова!'), 1000);
  });
  console.log(pizza);
}
makePizza(); // Пицца готова! (через 1 секунду)
Если бы мы написали это с .then():

new Promise(resolve => {
  setTimeout(() => resolve('Пицца готова!'), 1000);
}).then(pizza => console.log(pizza));
Код работает так же, но с async/await он короче и понятнее.

Важно
await не блокирует весь JavaScript. Пока функция ждёт, браузер может выполнять другие задачи (например, 
    реагировать на клики). Это всё ещё та же асинхронность из Занятия 18, просто в красивой обёртке.
Приостановка выполнения
Await приостанавливает только выполнение внутри async-функции, но не весь код в браузере. 
Это как если вы ждёте пиццу, а в это время можете посмотреть фильм. 
JavaScript использует очередь микрозадач (как в прошлом занятии), чтобы управлять await.

Пример:

async function waitAndShow() {
  console.log('Начали готовить');
  const result = await new Promise(resolve => {
    setTimeout(() => resolve('Еда готова!'), 1000);
  });
  console.log(result);
  console.log('Пора есть!');
}
waitAndShow();
console.log('Делаем что-то ещё');
Вывод:

Начали готовить
Делаем что-то ещё
Еда готова! (через 1 сек)
Пора есть!
Использование await в циклах
Иногда нужно обработать несколько асинхронных операций по очереди, например, 
проверить ответы на тест или загрузить данные для каждого уровня в игре. 
Await в циклах for…of позволяет ждать завершения каждой операции, прежде чем двигаться дальше.

Пример: проверка заданий

async function checkAssignments(assignments) {
  for (const assignment of assignments) {
    const result = await new Promise(resolve => {
      setTimeout(() => resolve(`Задание ${assignment} проверено`), 1000);
    });
    console.log(result);
  }
}
checkAssignments(['математика', 'русский']);
Аналогия: вы проверяете домашку по одному предмету за раз, потом ждёте оценки от учителя, 
прежде чем перейти к следующему. Если использовать forEach, 
JavaScript не будет ждать и всё пойдёт вразнобой. Об этом подробнее поговорим в «Типичных ошибках».

Сравнение с промисами:

function checkAssignmentsWithPromises(assignments) {
  let chain = Promise.resolve();
  assignments.forEach(assignment => {
    chain = chain.then(() => new Promise(resolve => {
      setTimeout(() => resolve(`Задание ${assignment} проверено`), 1000);
    }).then(result => console.log(result)));
  });
  return chain;
}
checkAssignmentsWithPromises(['математика', 'русский']);
С async/await код короче и понятнее, чем эта цепочка .then().

Обработка ошибок
Ошибки в async/await ловятся через try/catch, как в обычном синхронном коде. 
Это гораздо проще, чем добавлять .catch() к каждому .then().

Пример: ошибка при заказе

async function orderFood() {
  try {
    const food = await new Promise((resolve, reject) => {
      setTimeout(() => reject('Кухня закрыта!'), 1000);
    });
    console.log(food);
  } catch (error) {
    console.log('Ой, не вышло: ' + error);
  }
}
orderFood(); // Ой, не вышло: Кухня закрыта! (через 1 сек)
Сравнение с промисами (из прошлого занятия):

new Promise((resolve, reject) => {
  setTimeout(() => reject('Кухня закрыта!'), 1000);
}).then(food => console.log(food))
  .catch(error => console.log('Ой, не вышло: ' + error));
Переписывание промисов на async/await
Async/await создали, чтобы упростить длинные цепочки промисов. 
Давайте возьмём пример из прошлого занятия и перепишем его.

Промис-версия (из прошлого занятия):

function getProfile() {
  return new Promise(resolve => {
    setTimeout(() => resolve({ userId: 1, name: 'Anna' }), 1000);
  });
}

function getFriends(userId) {
  return new Promise(resolve => {
    setTimeout(() => resolve(['Bob', 'Clara']), 1000);
  });
}

getProfile()
  .then(profile => {
    console.log(`Пользователь: ${profile.name}`);
    return getFriends(profile.userId);
  })
  .then(friends => {
    console.log(`Друзья: ${friends.join(', ')}`);
  })
  .catch(error => console.log(`Ошибка: ${error}`));
Async/await-версия:

async function loadProfileAndFriends() {
  try {
    const profile = await getProfile();
    console.log(`Пользователь: ${profile.name}`);
    const friends = await getFriends(profile.userId);
    console.log(`Друзья: ${friends.join(', ')}`);
  } catch (error) {
    console.log(`Ошибка: ${error}`);
  }
}
loadProfileAndFriends();
Ещё пример: викторина из домашки прошлого занятия
Помните функцию checkQuizResult? Давайте перепишем её.

Промис-версия (из прошлого занятия):

function checkQuizResult(answer) {
  function getResult(ans) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (ans === "correct") {
          resolve({ score: 10 });
        } else {
          reject("Неверный ответ");
        }
      }, 1000);
    });
  }

  function getBonus() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() < 0.9) {
          resolve({ bonus: "Отличная работа!" });
        } else {
          reject("Бонус недоступен");
        }
      }, 1000);
    });
  }

  getResult(answer)
    .then(result => {
      console.log(`Баллы: ${result.score}`);
      return getBonus();
    })
    .then(bonus => {
      console.log(`Бонус: ${bonus.bonus}`);
      return { score: 10, bonus: bonus.bonus };
    })
    .then(final => {
      console.log(`Результат: ${final.score} баллов, бонус: ${final.bonus}`);
    })
    .catch(error => console.log(`Ошибка: ${error}`));
}
Async/await-версия:

async function checkQuizResultAsync(answer) {
  function getResult(ans) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (ans === "correct") {
          resolve({ score: 10 });
        } else {
          reject("Неверный ответ");
        }
      }, 1000);
    });
  }

  function getBonus() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() < 0.9) {
          resolve({ bonus: "Отличная работа!" });
        } else {
          reject("Бонус недоступен");
        }
      }, 1000);
    });
  }

  try {
    const result = await getResult(answer);
    console.log(`Баллы: ${result.score}`);
    const bonus = await getBonus();
    console.log(`Бонус: ${bonus.bonus}`);
    console.log(`Результат: ${result.score} баллов, бонус: ${bonus.bonus}`);
  } catch (error) {
    console.log(`Ошибка: ${error}`);
  }
}
checkQuizResultAsync("correct");
Что изменилось?

Код стал короче и читается как инструкция: «Получи результат, потом бонус, выведи итог».
Ошибки ловятся в одном месте, а не в конце длинной цепочки.
Легче добавить новый шаг, например, третий промис, без переписывания всей цепочки.
Почему async/await круче?
Async/await — это как перейти от письма ручкой к текстовому редактору. 
Промисы (из прошлого занятия) уже спасли нас от callback hell, но async/await делает код ещё чище, 
особенно когда операций много или они сложные. Вы пишете, как думаете: шаг за шагом, без лишних обёрток. 
Это особенно важно для школьников, которые только учатся: меньше путаницы, больше времени на творчество.

Ключевые плюсы:

Код выглядит как обычная программа, без асинхронного хаоса.
Легче отлаживать: ошибки указывают на конкретную строку с await.
Идеально для сложных задач, где требуется много шагов или циклы.
Теперь, когда мы знаем, как async/await делает жизнь проще, 
давайте попробуем применить это на практике и переписать ещё больше кода из мира 
промисов в мир синхронного стиля. Однако сперва посмотрим на типичные ошибки!






Типичные ошибки
Тип ошибки 1: Использование await вне async-функции
Описание:

Новички иногда пытаются использовать await в обычной функции, думая, 
что он сам по себе сделает код асинхронным. Это как пытаться включить микроволновку,
 не подключив её к розетке. JavaScript просто выдаст ошибку.

Пример ошибки (код):

function checkScore(score) {
  const result = await new Promise(resolve => {
    setTimeout(() => resolve(`Оценка: ${score}`), 1000);
  }); // Ошибка: SyntaxError: await is only valid in async function
  console.log(result);
}
checkScore(95);
Объяснение:

Await работает только внутри функций, помеченных как async. 
Без async JavaScript не знает, как приостановить выполнение для ожидания промиса, и выбрасывает синтаксическую ошибку.

Решение:

async function checkScore(score) {
  const result = await new Promise(resolve => {
    setTimeout(() => resolve(`Оценка: ${score}`), 1000);
  });
  console.log(result);
}
checkScore(95); // Оценка: 95 (через 1 сек)
Всегда добавляйте async перед функцией, если используете await.





Тип ошибки 2: Пропуск обработки ошибок с try/catch
Описание:

Забывая обернуть await в try/catch, разработчики оставляют код уязвимым к необработанным ошибкам. 
Это как отправиться в поход без аптечки: если что-то пойдёт не так (например, 
    сервер не ответит), программа «упадёт».

Пример ошибки (код):

async function loadGameLevel(levelId) {
  const level = await new Promise((resolve, reject) => {
    setTimeout(() => {
      if (levelId === 1) resolve('Уровень загружен');
      else reject('Уровень не найден');
    }, 1000);
  });
  console.log(level); // Если levelId !== 1, ошибка: Uncaught (in promise) Уровень не найден
}
loadGameLevel(2);
Объяснение:

Если промис отклоняется (например, из-за неверного levelId), await выбрасывает ошибку, 
но без try/catch она остаётся необработанной, и программа выдаёт ошибку в консоли.

Решение:

async function loadGameLevel(levelId) {
  try {
    const level = await new Promise((resolve, reject) => {
      setTimeout(() => {
        if (levelId === 1) resolve('Уровень загружен');
        else reject('Уровень не найден');
      }, 1000);
    });
    console.log(level);
  } catch (error) {
    console.log('Ошибка: ' + error); // Ошибка: Уровень не найден
  }
}
loadGameLevel(2);
Всегда используйте try/catch в async-функциях, чтобы ловить ошибки от отклонённых промисов.

Тип ошибки 3: Неправильное использование await в циклах с forEach
Описание:

Многие думают, что forEach с await будет ждать завершения каждой асинхронной операции, 
но это не так — все промисы запускаются одновременно, и результат может быть хаотичным. 
Это как раздать всем ученикам тесты и ждать всех ответов, не проверяя их по очереди.

Пример ошибки (код):

async function checkAnswers(answers) {
  answers.forEach(async answer => {
    const result = await new Promise(resolve => {
      setTimeout(() => resolve(`Ответ ${answer} проверен`), 1000);
    });
    console.log(result);
  });
}
checkAnswers(['A', 'B']); // Вывод в случайном порядке
Объяснение:

ForEach не приостанавливает выполнение для await, так как он не поддерживает асинхронность. 
Все промисы запускаются сразу, и результаты выводятся непредсказуемо, нарушая последовательность.

Решение:

async function checkAnswers(answers) {
  for (const answer of answers) {
    const result = await new Promise(resolve => {
      setTimeout(() => resolve(`Ответ ${answer} проверен`), 1000);
    });
    console.log(result);
  }
}
checkAnswers(['A', 'B']); // Ответ A проверен, Ответ B проверен
Для последовательной обработки асинхронных операций в цикле используйте for…of вместо forEach.






Тип ошибки 4: Возврат промиса из async-функции без await
Описание:

Если вызвать async-функцию без await, вы получите промис, а не результат, 
что может сломать логику программы. Это как попросить друга принести учебник, 
но начать писать конспект, не дождавшись книги.

Пример ошибки (код):

async function getTaskStatus(taskId) {
  return new Promise(resolve => {
    setTimeout(() => resolve(`Задача ${taskId} завершена`), 1000);
  });
}

async function showTask() {
  const status = getTaskStatus(42); // Ошибка: status — это промис
  console.log(status); // Promise {<pending>}
}
showTask();
Объяснение:

Async-функция всегда возвращает промис, и, если не использовать await, 
вы получите незавершённый промис вместо результата. Это приводит к неправильной работе кода, 
так как вы ожидаете строку, а получаете объект Promise.

Решение:

async function getTaskStatus(taskId) {
  return new Promise(resolve => {
    setTimeout(() => resolve(`Задача ${taskId} завершена`), 1000);
  });
}

async function showTask() {
  const status = await getTaskStatus(42);
  console.log(status); // Задача 42 завершена
}
showTask();
Всегда используйте await при вызове async-функций внутри другой async-функции, 
чтобы получить результат, а не промис.








Практикум
Задача 1: Проверка статуса урока
Ситуация:
Вы создаёте приложение для школы, где нужно проверить, готов ли урок для показа, 
с небольшой задержкой, как будто данные приходят с сервера.

Задача:
Напишите функцию checkLessonStatus() с использованием async/await, 
которая проверяет статус урока через промис и выводит результат в консоль. 
Промис должен через 1 секунду вернуть сообщение «Урок готов», если он доступен.

Решение:

async function checkLessonStatus() {
  try {
    const status = await new Promise(resolve => {
      setTimeout(() => resolve('Урок готов'), 1000);
    });
    console.log(status);
  } catch (error) {
    console.log('Ошибка: ' + error);
  }
}
checkLessonStatus();






Задача 2: Загрузка школьного расписания
Ситуация:
В том же школьном приложении вы хотите загрузить расписание: сначала список уроков, 
затем детали о домашнем задании для выбранного предмета.

Задача:
Перепишите следующий код на async/await, 
чтобы он загружал уроки и задание последовательно и выводил результаты в консоль.

function getLessons() {
  return new Promise(resolve => {
    setTimeout(() => resolve(['Математика', 'Русский']), 1000);
  });
}

function getHomework(lesson) {
  return new Promise(resolve => {
    setTimeout(() => resolve(`Задание по ${lesson}: решить задачи`), 1000);
  });
}

getLessons()
  .then(lessons => {
    console.log(`Уроки: ${lessons.join(', ')}`);
    return getHomework(lessons[0]);
  })
  .then(homework => {
    console.log(homework);
  })
  .catch(error => console.log(`Ошибка: ${error}`));
Решение:

async function loadSchedule() {
  try {
    const lessons = await getLessons();
    console.log(`Уроки: ${lessons.join(', ')}`);
    const homework = await getHomework(lessons[0]);
    console.log(homework);
  } catch (error) {
    console.log(`Ошибка: ${error}`);
  }
}
loadSchedule();





Итоги

Сегодня мы:

узнали, что такое ключевые слова async и await и как они упрощают работу с асинхронным кодом в JavaScript;
научились создавать асинхронные функции с async и использовать await для работы с промисами;
разобрали, как await приостанавливает выполнение асинхронной функции до завершения промиса;
освоили применение await в циклах для последовательной обработки асинхронных операций;
переписали код на промисах с использованием async/await, чтобы сравнить их с более читаемым подходом;
поняли, как async/await окончательно избавляет от проблемы callback hell, делая код похожим на синхронный.
Теперь мы можем писать асинхронный код, 
который легко читать и поддерживать, используя современный синтаксис async/await.