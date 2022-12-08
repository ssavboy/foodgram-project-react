<img src="https://github.com/ssavboy/foodgram-project-react/actions/workflows/main.yml/badge.svg">

# Foodgram
<b>Foodgram, «Продуктовый помощник».</b>

<p>На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.</p>

## Технологии
### Backend
![image]({https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue})
![image]({https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green})
![image]({https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white})
![image]({https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white})
![image]({https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white})
![image]({https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white})
![image]({https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white})
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

<b><a href='http://62.84.121.132/signin'>Ссылка на вход</a></b>