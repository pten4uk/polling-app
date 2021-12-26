# polling-app

Приложение предоставляет API для прохождения опросов.

## Quickstart
1. Из папки проекта: /polling-app устанавливаем виртуальное окружение:
```cmd
python -m venv venv
cd venv/Scripts
activate
cd ../..
```
2. Установка зависимостей и миграции:
```cmd
pip install -r pip.txt
cd prj
python manage.py makemigrations
python manage.py migrate
```
3. Создание суперпользователя:
```cmd
python manage.py createsuperuser
```
4. Запуск локального сервера:
```cmd
python manage.py runserver
```

## Начало работы
Взаимодействовать с приложением можно как через API, так и через Django.
 - По локальному адресу: http://127.0.0.1:8000/admin можно авторизоваться созданным ранее суперпользователем, и через административную панель создавать/изменять/удалять опросы.
 - После создания опроса, у него нельзя изменить дату старта.
 - При создании опроса можно сразу же создать текстовые вопросы к нему.
 - Чтобы создать вопросы с выбором варианта, нужно создать сначала опрос, а затем создать отдельно вопрос, выбрав созданный опрос при создании обьекта.
 - К вопросу с выбором, было добавлено поле multiple, разрешение выбирать несколько вариантов ответа у вопроса лежит на стороне фронтенда.
 
 - При переходе по главному адресу http://127.0.0.1:8000 пользователю нужно зарегистрироваться.
 - После этого вам будут доступны все активные опросы, которые можно пройти.
 - На этой странице есть также ссылка на пройденные опросы.
 
 ## Документация API
 POST - http://127.0.0.1:8000/api/auth/token/login
 - request
    ```json
    {
        "username": "",
        "password": ""
    }
    ```
 - response
    ```json
    {
        "auth_token": ""
    }
    ```
    После авторизации каждый запрос нужно делать с заголовком Authorization:
    ```json
    {
        "Authorization": "Token <auth_token>"
    }
    ```
 POST - http://127.0.0.1:8000/api/auth/token/logout
 
 GET - http://127.0.0.1:8000/api/get/active_polls/
 - request
 ```json
 {}
 ```
 - response
 ```json
 [
    {
        "title": "",
        "datetime_start": "",
        "datetime_end": "",
        "description": "",
        "text_questions": [
            {
                "pk": <number>,
                "text": ""
            }
        ],
        "choice_questions": [
            {
                "pk": <number>,
                "text": "",
                "multiple": <boolean>
            }
        ]
    }
]
```
GET - http://127.0.0.1:8000/api/get/completed_polls/
- request
```json
{}
```
-response
```json
{
    "user": <number>,
    "choice_answers": [
        {
            "poll": <number>,
            "question": <number>,
            "answer": ""
        }
    ],
    "text_answers": [
        {
            "poll": <number>,
            "question": <number>,
            "answer": ""
        }
    ]
}
```
 POST - http://127.0.0.1:8000/api/create/poll/
 - request
 ```json
 {
    "title": "",
    "datetime_start": "<YYYY-MM-DDTHH:MM>",
    "datetime_end": "<YYYY-MM-DDTHH:MM>",
    "description": ""
}
 ```
 - response
 Созданный объект
 <p> POST - http://127.0.0.1:8000/api/create/choice_question/ </p>
 - request
 ```json
 {
    "poll": "<number>",
    "text": "",
    "multiple": <boolean>,
    "choice_answers": [
        "",
        "",
        ""
    ]
}
 ```
