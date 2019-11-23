# Scrapyd-Django-Template
Basic setup to run ScrapyD + Django and save it in Django Models. You can be up and running in just a few minutes. This template includes

* Basic structure of a Django project.
* Basic structure for scrapy.
* Configuration of scrapy in order to access Django models objects.
* Basic scrapy pipeline to save crawled objets to Django models.
* Basic spider definition
* Basic demo from the oficial tutorial that crawls data from http://quotes.toscrape.com


## Setup
1 - Install requirements
````
$ pip install -r requirements.txt
````
2 - Configure the database
````
$ python manage.py migrate
````
## Start the project
In order to start this project you will need to have running Django and Scrapyd at the same time.

In order to run Django
````
$ python manage.py runserver
````
In order to run Scrapyd
````
$ cd scrapy_app
$ scrapyd
````

## Setup by Docker 
1 - Build application
````
$ docker-compose build
````
2 - Configure database and create super user  
````
$ docker-compose run django bash -c "python manage.py migrate && python manage.py createsuperuser"
````
3 - Start application
````
$ docker-compose up
````

Django is running on: http://localhost:3001
Scrapyd is running on: http://localhost:6800


At this point you will be able to send job request to Scrapyd. This project is setup with a demo spider from the oficial tutorial of scrapy. To run it you must send a http request to Scrapyd with the job info
````
curl http://localhost:6800/schedule.json -d project=default -d spider=toscrape-css
````

The crawled data will be automatically be saved in the Django models

This repo is inspired by an article from Ali Oğuzhan Yıldız, https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e
