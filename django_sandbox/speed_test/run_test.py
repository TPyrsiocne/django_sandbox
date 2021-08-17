from speed_test.models import Person
import random


def rand_string(n):
    str = ""
    for i in range(n):
        str = str + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    return str

for i in range(1000)
    Person(identification_string = rand_string(50)).save()