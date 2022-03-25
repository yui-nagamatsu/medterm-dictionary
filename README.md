# Django App

# Run Locally

To start this project, execute the command below.

```
docker compose run app django-admin startproject mysite .
```

To start server, run the next command.

```
docker compose up --detach
open open http://localhost:8000
```

To get in the server, execute the next one.

```
docker compose exec app /bin/bash
```

To connet the app to the persistent database, rewrite `DATABASES` in setting like below and delete `/src/db.sqlite3`.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'mysiteuser',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': 'test_database',
        },
    }
}
```
