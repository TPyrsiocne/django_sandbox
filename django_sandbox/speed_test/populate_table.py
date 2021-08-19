from speed_test.models import Person
import random

""" 
populate table clears table and popluates it with 10^6 randomly named people
"""

def rand_string(n):
    str = ""
    for i in range(n):
        str = str + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    return str


Person.objects.all().delete()
print("database cleared...")

for i in range(100):
    for j in range(10000):
        Person(identification_string = rand_string(50)).save()
    print(str((i+1)*10000) + " entered")