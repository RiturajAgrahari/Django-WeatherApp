# Django-WeatherApp
This was my first personal project in order to master django.

## Project feature:
* Checking weather of a city.
* Comparing weather of 2 cities.

## Tech stack Used:
* Python
* Django
* Javascript
* HTML
* CSS

## Additional Python Modules Required:
* django
* requests
* python-dotenv

## To install the required modules and packages :
```commandline
pip install -r requirements.txt
```

## Run migrations:
```commandline
python manage.py makemigrations
python manage.py migrate
```

## Collect staticfiles :
```commandline
python manage.py collectstatic
```

## Important note:
In the project you have to make sure about few things in order to make sure it works properly:

### .env:
Create a .env folder in root file, and use your api token into it.

Get your api token from : https://openweathermap.org
```
TOKEN = 'your_token_here'
```

## Et voila!, now you can run the project locally.  

```commandline
python manage.py runserver
```

In your web browser enter the address: http://localhost:8000 or http://127.0.0.1:8000/

## Adios!
Thanks a lot for looking at my project

To keep an eye on me you can have a look at my portfolio - 


https://rituraj-agrahari.com