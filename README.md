
_Репозиторий на Github [ссылка](https://github.com/JuliaBars/microservices)._

## Microservices with Django and DRF

**Создаем посты и комментарии**

Посты живут отдельно от комментариев, сервисы взаимодействуют по АПИ.

---
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

---


Установите зависимости.
Запустите один сервис на 8000 порту, второй на 8001
```
python manage.py runserver 8001
```
Выполните миграции, создайте пару постов, для одного создайте комментарий.
Все необходимые поля для успешного запроса можно получить, отправив пустой POST запрос на http://127.0.0.1:8000/api/posts/ и http://127.0.0.1:8000/api/comments/.

GET запрос на http://127.0.0.1:8000/api/posts/ вернет результат взаимодействия микросервисов.
```
[
    {
        "id": 1,
        "title": "New post",
        "description": "very good",
        "comments": [
            {
                "id": 1,
                "post_id": 1,
                "text": "new comment"
            }
        ]
    },
    {
        "id": 2,
        "title": "second post",
        "description": "new post without comments",
        "comments": []
    }
]
```


_автор Юлия Орлова_
