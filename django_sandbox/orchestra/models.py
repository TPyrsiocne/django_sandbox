from django.db import models

# Create your models here.


class Instrument(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return name



class Musician(models.Model):
    name = models.CharField(max_length = 100)
    can_play = models.ManyToManyField(Instrument)

    def __str__(self):
        return name

