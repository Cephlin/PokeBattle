from django.db import models
from player.models import Player


class Battle(models.Model):
    turn = models.IntegerField(default=1)
    winner = models.ForeignKey(Player, null=True)

    red = models.ForeignKey(Player, related_name='battle-red+')
    blue = models.ForeignKey(Player, related_name='battle-blue+')

    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now_add=False, null=True)
