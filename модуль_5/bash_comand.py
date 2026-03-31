'Команды для python'
git clone #  Клонирование проекта из репозитория

py -3.9 -m venv venv # Создание вирт. окружения с указанием версии

python -m venv venv # Создание вирт. окружения

source venv/Scripts/activate # Активация вирт. окружения

python -m pip install --upgrade pip # Обновление менеджера pip

pip install -r requirements.txt #  Установка зависимостей и файла

pip freeze > requirements.txt # Обновление (создание) файла ззависимостей

python manage.py makemigrations # Создание миграций

python manage.py migrate #  Применение миграций

python manage.py runserver #  Запуск сервера разработки

deactivate #  Девктивация вирт. окружения

rm -r venv #  Удаение вирт. окружения




'Команды для JavaScript'

npm init  


npm install prompt-sync "Импрорт prompt"


'Проверка, установлен ли Node.js:'

node --version
npm --version



"Установка TypeScript"

npm install -g typescript

'Проверим установку:'

tsc --version


'''Создаём проект
Создаём папку для проекта, например, my-school-project:'''

mkdir my-school-project
cd my-school-project


'Создаём файл package.json для управления проектом:'

npm init -y


'Настроим TypeScript'

tsc --init

'''Это создаст файл tsconfig.json

{
  "compilerOptions": {
    "target": "es6", // Компилировать в современный JavaScript
    "outDir": "./dist", // Сохранять .js файлы в папку dist
    "strict": true, // Включить строгие проверки
    "module": "commonjs" // Формат для Node.js
  },
  "include": ["*.ts"] // Компилировать все .ts файлы
}

'''

'''Создадим файл index.ts'''

'''Скомпилируем код'''

tsc


'''Запустим программу'''

node dist/index.js