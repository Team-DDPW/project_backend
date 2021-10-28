# Davee's Django Rest API Template

## Author: Davee Sok

## Links & Resources

- [Link to this Repo](https://github.com/daveeS987/template-davees-django-api)
- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Create Custom User Model](https://testdriven.io/blog/django-custom-user-model/)

## Overview/ Motivation

Starting up a Django api can be time consuming. This template is meant to get up and running fast. Once all the wiring is done, you can make modifications to your models and tests as needed.

## Tools & Dependencies

- poetry
- Django
- djangorestframework
- djangorestframework-simplejwt
- django-cors-headers
- django-environ
- gunicorn
- Docker
- ElephantSQL
- whitenoise
- Black
- psycopg2-binary

## Getting Started

#### 1. Click on "Use this template" and create your repo

#### 2. Clone your repo and install dependencies

```iterm
cd into your repo
poetry shell
poetry install
```

#### 3. Get New Django Secret Key by running the following command in the terminal:

```iterm
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

#### 4. Edit .env.txt file inside a_project folder with created Django Secret Key and Database info from Elephant Sql

```env
SECRET_KEY=django-insecure-REPLACE_THIS_AREA_WITH_DJANGO_SECRET_KEY
DEBUG=False

ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
ALLOW_ALL_ORIGINS=True
ALLOWED_ORIGINS=http://localhost:3000

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME= **Get from Elephant sql**
DATABASE_USER= **Get from Elephant sql**
DATABASE_PASSWORD= **Get from Elephant sql**
DATABASE_HOST= **Get from Elephant sql**
DATABASE_PORT=5432
```

- remember to rename .env.txt to .env

#### 5. Replace all occurences of "Xxxxx" and "xxxxx" with your new app name

- rename "xxxxx" folder to your new app name(use lower case). Example: xxxxx -> blog
- Do a global search of "Xxxxx" and replace all occurences with your app name
  - (For this step, app name needs to be a capital word) Example: Xxxxx -> Blog
  - Make sure to select "Match Case" option. [Aa]
  - (There will only be 29 matches. If you see 44, you didn't check your case)
- Do a global search of "xxxxx" and replace all occurences with your app name
  - (For this step, app name needs to be a lower cased) Example: xxxxx -> blog
  - Make sure to select "Match Case" option. [Aa]
  - (There will only be 15 matches. If you see a differnt number, you didn't check your case)

#### 6. Create requirements.txt File

```terminal
poetry export -f requirements.txt -o requirements.txt --without-hashes
```

#### 7. Create Static Files

```terminal
python manage.py collectstatic
```

#### 7. Run following commands to start Docker:

- make sure docker is running on your computer

```iterm
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

## Commands To Know

#### Docker:

```python
docker-compose -d
docker-compose up
docker-compose up --build
docker-compose down
docker-compose stop
docker-compose start
docker-compose restart
docker-compose logs
```

#### Httpie Commands through terminal:

```python

# This signs us in and grabs access and refresh tokens
http POST :8000/api/token/ email='admin@gmail.com' password='admin'

# This adds our access token to the headers in our request. Gets all blogs
http GET :8000/api/v1/blog/ 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Gets One Item with pk=4
http GET :8000/api/v1/blog/4 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Deletes One Item with pk=5
http DELETE :8000/api/v1/blog/5 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'
```

---

### Extra Notes

This project makes use of a custom user that over writes django's default user model. When you create new models that need to reference user as a foreign key, you need to make the following changes:

```python
# Old Way

from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# ----------------------------------- New Way -----------------------------------

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

```

In your tests, you would still use get_user_model()
