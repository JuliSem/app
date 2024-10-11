## Описание задачи:

Создание следующего модуля:
- REST API, который принимает в параметрах json (с любой фиксированной 
структурой) и файл (любой);
- файл переименовывается в уникальное имя и сохраняется в какую-нибудь 
доступную модулю папку;
- данные json, оригинальное имя файла и ссылка на новый файл записываются 
в базу данных (PostgreSQL);
- на отдельной странице выводится список всех файлов в таблице по 20 записей 
с оригинальным названием (из базы данных), а при нажатии файл скачивается и 
открывается. 

### Стек технологий:

- Python
- Django
- Django REST Framework
- DRF Spectacular
- PostgreSQL

### Как запустить проект:

<br>1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone "адрес клонируемого репозитория"
```

<br>2. В **settings.py** приложения **app** укажите переменные для 
подключения к БД:

# Пременные для СУБД PostgreSQL:
POSTGRES_USER # Имя пользователя
POSTGRES_PASSWORD # Пароль пользователя
POSTGRES_DB # Имя базы даных

# Переменные для Django-проекта:
DB_HOST # Адрес, по которому Django будет соединяться с базой данных
DB_PORT # Порт, по которому Django будет обращаться к БД. Для PostgreSQL порт по умолчанию 
          5432
```

<br>3. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    venv\Scripts\activate
    ```

<br>4. Установить и обновить пакетный менеджер:

```
python -m pip install --upgrade pip
```

<br>5. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

<br>6. В каталоге **app**(где находится файл manage.py)  
выполнить миграции:

```
python manage.py migrate
```
```
python manage.py makemigrations
```

<br>7. Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

<br>1. Создание файла (POST-запрос):

```
http://127.0.0.1:8000/api/v1/files/
```

```json
{
  "title": "string",
  "description": "string",
  "file": "string"
}
```

<br>2. Получение списка файлов (GET-запрос):

```
http://127.0.0.1:8000/api/v1/files/
```

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "origin_filename": "string",
      "file": "string"
    }
  ]
}
```

<br>3. Получение определенного файла по его id (GET-запрос):

```
http://127.0.0.1:8000/api/v1/files/{id}/
```

```json
{
  "origin_filename": "string",
  "file": "string"
}
```

<br>4. Скачивание конкретного файла (GET-запрос):

```
http://127.0.0.1:8000//api/v1/files/{id}/download/
```

```json
{
  "origin_filename": "string",
  "file": "string"
}
```

> Подробнее можно ознакомится в документации Swagger http://127.0.0.1:8000/api/v1/schema/swagger/
