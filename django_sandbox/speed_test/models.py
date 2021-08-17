from django.db import models

# Create your models here.

class Person(models.Model):
    identification_string = models.CharField(max_length = 100)
    def __str__(self):
        return self.identification_string