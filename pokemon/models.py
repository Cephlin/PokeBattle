from django.db import models


class Pokemon(models.model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField(max_length=4)
    attack = models.IntegerField(max_length=4)

