from django.db import models

# Create your models here.


class Instrument(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Musician(models.Model):
    name = models.CharField(max_length = 100)
    can_play = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name


class Good_Musician(Musician):
    has_donated = models.IntegerField(default=0)