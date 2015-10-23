from django.db import models
from round.models import Round
from player.models import Player


class Battle(models.Model):
    rounds = models.ForeignKey(Round, default=None)
    winner = models.ForeignKey(Player, default=None)

    started_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(auto_now_add=False, blank=True, default=None)

    def battle_ended(self):
        if self.rounds.red.check_usable_pokemon() == 0:
            self.winner = self.rounds.red
        elif self.rounds.blue.check_usable_pokemon() == 0:
            self.winner = self.rounds.blue

    def advance_round(self):
        self.rounds.round += 1
        self.rounds.do_moves()
        self.rounds.check_usable_pokemon()

        winner = self.rounds.check_for_winner()

        if winner:
            self.winner = winner
