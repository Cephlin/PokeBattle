from django.db import models
from type.models import Type


class Move(models.Model):
    base_power = models.IntegerField(null=True)
    damage_dealing = models.BooleanField(default=False)
    type = models.ForeignKey(Type)
    pp = models.IntegerField(default=5)
    accuracy = models.IntegerField(default=100)