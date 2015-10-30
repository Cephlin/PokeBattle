from django.db import models
from type.models import Type


class Move(models.Model):
    name = models.CharField(max_length=20)
    base_power = models.IntegerField(default=0)
    damage_dealing = models.BooleanField(default=True)
    type = models.ForeignKey(Type)
    pp = models.IntegerField(default=5)
    accuracy = models.IntegerField(default=100)
    priority = models.IntegerField(default=0)
