<img src="https://github.com/ssavboy/foodgram-project-react/actions/workflows/main.yml/badge.svg">

# Foodgram
<b>Foodgram, «Продуктовый помощник».</b>

<p>На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.</p>

# Развертка приложения Foodgram в Docker

<b>Шаблон заполения .env</b>

```
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=postgres
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=postgres
- DB_HOST=db
- DB_PORT=5432 
```

<b>Описание команд для запуска приложения в контейнерах</b>
```
- docker-compose exec web python manage.py makemigrations users recipes
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser
- docker-compose exec web python manage.py load_data
- docker-compose exec web python manage.py collectstatic --no-input
```

<b><a href='http://62.84.121.132/signin'>Ссылка на вход</a></b>