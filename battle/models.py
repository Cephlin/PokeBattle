from django.db import models
from player.models import Player


class Battle(models.Model):
    red = models.ForeignKey(Player, related_name='red')
    blue = models.ForeignKey(Player, related_name='blue')
    round = models.IntegerField(default=0)
