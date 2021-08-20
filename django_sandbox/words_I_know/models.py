from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    known_by = models.ManyToManyField(User)
    word_txt = models.CharField(max_length = 100)
    pronunciation = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 1000)

    def __str__(self):
        return self.word_txt