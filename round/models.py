from django.db import models
from player.models import Player


# Create your models here.
class Round(models.Model):
    round = models.IntegerField(default=0)

    red = models.ForeignKey(Player, related_name='red')
    blue = models.ForeignKey(Player, related_name='blue')
    # gold and silver for 4 players

    started_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(auto_now_add=False, blank=True)

    def do_moves(self):
        self.red.pokemon1.take_damage(self.blue.pokemon1.attack)
        self.blue.pokemon1.take_damage(self.red.pokemon1.attack)

    def check_usable_pokemon(self):
        self.red.check_usable_pokemon()
        self.blue.check_usable_pokemon()

    def check_for_winner(self):
        if  self.red.usable_pokemon <= 0:
            return self.blue
        elif self.blue.usable_pokemon <= 0:
            return self.red
        else:
            return None


    # red_move = models.BooleanField(default=False
    # blue_move = models.BooleanField(default=False)