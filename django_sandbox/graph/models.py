from django.db import models


class Node(models.Model):
    """points_to = models.ManyToManyField("self", symmetrical=False)"""
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.label


"""class Edge(models.Model):
    label = models.CharField(max_length = 100)
"""


