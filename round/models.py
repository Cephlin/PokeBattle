from django.db import models
from random import random
from playerpokemon.models import PlayerPokemon
from genx.models import Gen
from itertools import izip

class Round(models.Model):
    battle = models.ForeignKey('battle.Battle')

    red = models.ForeignKey('player.Player', related_name='%(app_label)s_%(class)s_red')
    blue = models.ForeignKey('player.Player', related_name='round-blue+')
    # gold and silver for 4 players

    turn = models.IntegerField(default=1)

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
        red_team = PlayerPokemon.objects.filter(player=self.red)
        blue_team = PlayerPokemon.objects.filter(player=self.blue)

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            # Blue is quicker
            if blue_pokemon.speed > red_pokemon.speed:
                # damage = Gen.get_damage()
                red_pokemon.take_damage(blue_pokemon.attack)
                if not self.get_winner():
                    blue_pokemon.take_damage(red_pokemon.attack)
            elif red_pokemon.speed > blue_pokemon.speed:  # Red is quicker
                blue_pokemon.take_damage(red_pokemon.attack)
                if not self.get_winner():
                    red_pokemon.take_damage(blue_pokemon.attack)
            else:  # Speed is equal
                if random() < 0.5:
                    blue_pokemon.take_damage(red_pokemon.attack)
                    if not self.get_winner():
                        red_pokemon.take_damage(blue_pokemon.attack)
                else:
                    red_pokemon.take_damage(blue_pokemon.attack)
                    if not self.get_winner():
                        blue_pokemon.take_damage(red_pokemon.attack)

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