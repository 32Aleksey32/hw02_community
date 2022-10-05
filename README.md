# backend_community_homework, спринт №3 в Яндекс.Практикум



## Что реализовано в сообществе:
- Создано и зарегистрировано приложение Posts.
- Подключена база данных.
- Десять последних записей выводятся на главную страницу.
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

## Использованный стек технологий:
- atomicwrites==1.4.0
- attrs==21.4.0
- colorama==0.4.4
- Django==2.2.9
- iniconfig==1.1.1
- packaging==21.3
- pluggy==1.0.0
- py==1.11.0
- pyparsing==3.0.7
- pytest==6.2.5
- pytest-django==3.8.0
- pytest-pythonpath==0.7.3
- pytz==2021.3
- six==1.15.0
- sqlparse==0.4.2
- tomli==2.0.0

## Настройка и запуск на компьютере
Клонируем проект:
```
https://github.com/32Aleksey32/hw02_community.git
```
Переходим в папку с проектом:
```
cd hw02_community
```
Устанавливаем виртуальное окружение:
```
python -m venv venv
```
Активируем виртуальное окружение:
```
source venv/Scripts/activate
```
Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Применяем миграции:
```
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```
Создаем супер пользователя:
```
python yatube/manage.py createsuperuser
```
Запускаем проект:
```
python yatube/manage.py runserver
```
После чего проект будет доступен по адресу http://127.0.0.1/

Заходим в http://127.0.0.1/admin и создаем группы и записи. После чего записи и группы появятся на главной странице.
