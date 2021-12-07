

source env/Scripts/activate

python manage.py runserver

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

username (bryson)
password (password)


(
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

)# Projects
