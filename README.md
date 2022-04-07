# WebUI-Python

Python Django Web Application Guide

 1. install vm env

        pip install virtualenv

 2. create and cd to project directory
 3. create vm env

	    python -m virtualenv venv
#venv is folder store module python

 4. run env

	    .\venv\scripts\activate
>(venv) C:/.......
 
 5. install django module in vm

	    pip install django

 6. create project django

	    django-admin startproject {name_project}

 7. cd {name_project}
 8. run project

	    python manage.py runserver

 9. create app

	    python manage.py startapp {name_app}
 10. migrate app

	     python manage.py migrate
 11. create admin

	      python manage.py createsuperuser

##Design Web Application
 if have Form create fill and change models.py
 
 12. create models db

            python manage.py makemigrations
 13. verify db

            python manage.py migrate
