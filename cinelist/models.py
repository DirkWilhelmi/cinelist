from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tid = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100, unique=True)
    length = models.PositiveIntegerField('Length in Minutes')

    def __str__(self):
        return self.title

class Screening(models.Model):
    time = models.DateTimeField('Time of Screening')
    film = models.ForeignKey(Film)
    cinema = models.ForeignKey(Cinema)

    def __str__(self):
        return 'A Screening'
