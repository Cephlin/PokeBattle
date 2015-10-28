from django.db import models
from random import random

from player.models import Player
from battle.models import Battle


class Round(models.Model):
    battle = models.ForeignKey(Battle)
    turn = models.IntegerField(default=1)

    red = models.ForeignKey(Player, related_name='round-red+')
    blue = models.ForeignKey(Player, related_name='round-blue+')
    # gold and silver for 4 players

    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now_add=False, null=True)

    def advance_round(self):
        if not self.battle.winner:
            self.do_moves()
            self.check_usable_pokemon()

            return self.winner_or_next_turn()

    def new_round(self):
        new_round = Round(battle=self.battle, turn=self.turn+1, red=self.red, blue=self.blue)
        new_round.save()

        return new_round

    def do_moves(self):
        if self.blue.pokemon1.speed > self.red.pokemon1.speed:  # Blue is quicker
            self.red.pokemon1.take_damage(self.blue.pokemon1.attack)
            if not self.get_winner():
                self.blue.pokemon1.take_damage(self.red.pokemon1.attack)
        elif self.red.pokemon1.speed > self.blue.pokemon1.speed:  # Red is quicker
            self.blue.pokemon1.take_damage(self.red.pokemon1.attack)
            if not self.get_winner():
                self.red.pokemon1.take_damage(self.blue.pokemon1.attack)
        else:  # Speed is equal
            if random() < 0.5:
                self.blue.pokemon1.take_damage(self.red.pokemon1.attack)
                if not self.get_winner():
                    self.red.pokemon1.take_damage(self.blue.pokemon1.attack)
            else:
                self.red.pokemon1.take_damage(self.blue.pokemon1.attack)
                if not self.get_winner():
                    self.blue.pokemon1.take_damage(self.red.pokemon1.attack)

    def check_usable_pokemon(self):
        self.red.check_usable_pokemon()
        self.blue.check_usable_pokemon()

    def get_winner(self):
        self.check_usable_pokemon()
        if self.red.usable_pokemon <= 0:  # Red loses
            return self.blue
        elif self.blue.usable_pokemon <= 0:  # Blue loses
            return self.red
        else:
            return False  # No-one has lost yet

    def winner_or_next_turn(self):
        winner = self.get_winner()
        if winner:
            self.battle.winner = winner
        else:
            return self.new_round()