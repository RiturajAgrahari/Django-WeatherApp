# Django-WeatherApp
This is my own personal project to learn django.

## Project contains:
* Checking weather of city.
* Comparing weather of 2 cities.

## Technologies Used:
* Python
* Django
* Javascript
* HTML
* CSS

## Additional Python Modules Required:
* django
* requests
* python-dotenv

## Usage:
```
python Django-CRUD-WebApp/manage.py makemigrations
python Django-CRUD-WebApp/manage.py migrate
python Django-CRUD-WebApp/manage.py runserver
```

In your web browser enter the address: http://localhost:8000 or http://127.0.0.1:8000/


## Note:
In your project you have to make sure about these things:
### .env:
Create a .env folder in root file, and use your api token into it.

Get your api token : https://openweathermap.org
```
TOKEN = 'your_token_here'
```

### settings.py:
```
from pathlib import Path
import os
```
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weather_app'  # or your app_name if any
]
```
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'weather_app/static')]
```

### urls.py:
```
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),
]
```

## Bie...
