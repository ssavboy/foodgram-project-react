<img src="https://github.com/ssavboy/foodgram-project-react/actions/workflows/main.yml/badge.svg">

# Foodgram
<b>Foodgram, «Продуктовый помощник».</b>

<p>На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.</p>

## Технологии

### Backend
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

### Frontend
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E})
![image](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB})

# Развертка приложения Foodgram в Docker

## Шаблон заполения .env

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
```

## Описание команд для запуска приложения
Клонировать репозиторий
```
git@github.com:ssavboy/foodgram-project-react.git
```
Перейти в директорию infra
```
cd infra
```
Запустить docker-compose
```
docker-compose up
```
Создать и выполнить миграции
```
docker-compose exec backend python manage.py makemigrations users recipes
docker-compose exec backend python manage.py migrate
```
Опионально подгрузить ингредиенты и теги
```
docker-compose exec backend python manage.py load_data
```
Собрать статику
```
docker-compose exec web python manage.py collectstatic --no-input 
```
Перейти по адрессу
```
http://localhost/
```
### Ссылка на вход [Kirill Molchanov](http://62.84.121.132/signin)
### Автор [Kirill Molchanov](https://github.com/ssavboy)
