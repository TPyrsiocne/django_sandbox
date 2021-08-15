from django.db import models


class Node(models.Model):
    points_to = models.ManyToManyField("self",symmetrical=False,through='Edge')
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.label


class Edge(models.Model):
    #not sure what 'on_delete = models.CASCADE' does
    from_node = models.ForeignKey(Node, related_name = 'from_node',on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name = 'to_node',on_delete=models.CASCADE)
    label = models.CharField(max_length = 100)

    def __str__(self):
        return self.from_node.label + " -> " + self.to_node.label



