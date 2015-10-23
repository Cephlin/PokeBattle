from django.db import models
from player.models import Player


class Battle(models.Model):
    red = models.ForeignKey(Player, related_name='red')
    blue = models.ForeignKey(Player, related_name='blue')
    round = models.IntegerField(default=1)
    winner = models.ForeignKey(Player, default=None)

    def battle_ended(self):
        if self.red.get_and_update_usable_pokemon() == 0:
            self.winner = self.red
        elif self.blue.get_and_update_usable_pokemon() == 0:
            self.winner = self.blue
