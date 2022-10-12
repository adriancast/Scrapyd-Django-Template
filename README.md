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
3 - Create superuser to login in the django admin
````
$ python manage.py createsuperuser
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

## Demo
Django is running on: http://127.0.0.1:8000
Scrapyd is running on: http://0.0.0.0:6800


At this point you will be able to send job request to Scrapyd. This project is setup with a demo spider from the oficial tutorial of scrapy. To run it you must send a http request to Scrapyd with the job info
````
curl http://127.0.0.1:6800/schedule.json -d project=default -d spider=toscrape-css
````

Now go to http://127.0.0.1:8000/admin and login using the superuser you created before. The crawled data will be automatically be saved in the Django models.

This repo is inspired by an article from Ali Oğuzhan Yıldız, https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e
