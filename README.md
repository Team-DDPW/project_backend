# FastEx Backend

## Team Sith Lords

- [Daniel Dills](https://github.com/danieldills)
- [Davee Sok](https://github.com/daveeS987)
- [Prabin Singh](https://github.com/prabin544)
- [Wondwosen Tsige](https://github.com/WondwosenTsige)

## Problem Domain

In 2021 there are still regions of the world where standardized shipping is not practical, cost effective or even possible. People currently use friends/family/acquaintances to carry important documents and items. This has become a more reliable and cost effective means.

## Project Summary

Our vision was to create an app where packages can be sent to countries that lack accessible and affordable shipping methods. This app will assist in finding people traveling to desired destinations to ship apackage in a much more effective, efficient and faster way than current traditional options. It helps communities that lack options many of us take for granted on a daily basis.

## MVP

- Create profile for users
- Sign in / Sign out functionality
- CRUD functionality for request post
- Email functionality between traveler and requester
- Image upload for packages

## Links and Resources

- [FastEx site](https://fastex.netlify.app/)
- [Link to API address](https://fastex-api.herokuapp.com/)
- [Front End Repo](https://github.com/Team-DDPW/project-frontend)
- [Back End Repo](https://github.com/Team-DDPW/project_backend)
- [Trello](https://trello.com/b/rF1sdqfr/team-ddpw)
- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Create Custom User Model](https://testdriven.io/blog/django-custom-user-model/)

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

Make sure to create .env

```env
SECRET_KEY=
DEBUG=False

ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
ALLOW_ALL_ORIGINS=True
ALLOWED_ORIGINS=http://localhost:3000

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=**Get this for ElephantSQL**
DATABASE_USER=**Get this for ElephantSQL**
DATABASE_PASSWORD=**Get this for ElephantSQL**
DATABASE_HOST=**Get this for ElephantSQL**
DATABASE_PORT=5432
```
