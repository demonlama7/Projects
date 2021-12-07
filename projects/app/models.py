from django.db import models

# Create your models here.

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    creator = models.CharField(max_length=30,)
    url = models.CharField(max_length=30)

    WEBSITE = 'W'
    WEBGL_GAME = 'G'
    REPL = 'R'

    types = [
        ('WEBSITE', 'Website'),
        ('WEBGL_GAME', 'WebGL Game'),
        ('REPL', 'repl'),
    ]

    project_type = models.CharField(
        max_length=20,
        choices=types,
        default=REPL,
    )


    def __str__(self):
        return self.title


# class Student(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     GRADUATE = 'GR'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#         (GRADUATE, 'Graduate'),
#     ]
#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )


