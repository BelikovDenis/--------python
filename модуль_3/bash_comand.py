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
