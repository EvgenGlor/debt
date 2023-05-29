Для запуска данного проекта, необходимо склонировать его к себе в рабочую папку, для этого вводим команду в терминале:
git clone https://github.com/EvgenGlor/debt

После чего необходимо устанивать pip, django
Для этого выполняем команды по порядку:
sudo apt install python3-pip
pip3 install django
pip3 install djangorestframework
pip install django-filter

Для запуска проекта на локальном компьютере необходимо перейти в корневую папку /mydebt/ введя команду:
cd debt
И запустить сервер командой:
python manage.py runserver

Проект поддерживает CRUD запросы:
GET — получение сущности
POST — создание новой сущности
PUT - обнавление сущности
DELETE - удалние сущности 

В БД две таблицы, связанные способом 1 ко многим.
Первая таблица является списком людей, с номером телефона
Вторая таблица человек - сумма долга