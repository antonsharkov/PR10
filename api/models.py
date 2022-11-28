from django.db import models

# Create your models here.
class Zamena:
    def __init__(self, array, s1, s2, result):
        self.array = array
        self.s1 = s1
        self.s2 = s2
        self.result = result
