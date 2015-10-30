from django.db import models
from random import random
from playerpokemon.models import PlayerPokemon
import genx.models as gen
from itertools import izip


class Round(models.Model):
    battle = models.ForeignKey('battle.Battle')

    red = models.ForeignKey('player.Player', related_name='%(app_label)s_%(class)s_red')
    blue = models.ForeignKey('player.Player', related_name='%(app_label)s_%(class)s_blue')
    # gold and silver for 4 players

    red_selected_move = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_red_selected_move',
                                          null=True, blank=True)
    blue_selected_move = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_blue_selected_move',
                                           null=True, blank=True)

    red_damage_dealt = models.IntegerField(default=0)
    blue_damage_dealt = models.IntegerField(default=0)

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

        current_red_pokemon = None
        current_blue_pokemon = None

        blue_pokemon, current_blue_pokemon, current_red_pokemon, red_pokemon\
            = self.get_current_pokemon(blue_team, current_blue_pokemon, current_red_pokemon, red_team)

        if blue_pokemon.speed > red_pokemon.speed:  # Blue is quicker
            self.blue_attacks_first(current_blue_pokemon, current_red_pokemon)
        elif red_pokemon.speed > blue_pokemon.speed:  # Red is quicker
            self.red_attacks_first(current_blue_pokemon, current_red_pokemon)
        else:  # Speed is equal
            self.random_attacks_first(current_blue_pokemon, current_red_pokemon)

    def random_attacks_first(self, current_blue_pokemon, current_red_pokemon):
        if random() < 0.5:
            self.red_attacks_first(current_blue_pokemon, current_red_pokemon)
        else:
            self.blue_attacks_first(current_blue_pokemon, current_red_pokemon)

    def red_attacks_first(self, current_blue_pokemon, current_red_pokemon):
        self.blue_takes_damage(current_blue_pokemon, current_red_pokemon)
        if not self.get_winner():
            self.red_takes_damage(current_blue_pokemon, current_red_pokemon)

    def blue_attacks_first(self, current_blue_pokemon, current_red_pokemon):
        self.red_takes_damage(current_blue_pokemon, current_red_pokemon)
        if not self.get_winner():
            self.blue_takes_damage(current_blue_pokemon, current_blue_pokemon)

    def red_takes_damage(self, current_blue_pokemon, current_red_pokemon):
        damage = gen.get_damage(red_level=current_red_pokemon.level, red_attack=current_red_pokemon.attack,
                                blue_defence=current_blue_pokemon.defence,
                                red_move_base=self.red_selected_move.base_power,
                                red_modifier=current_red_pokemon.modifier)
        current_red_pokemon.take_damage(damage)

    def blue_takes_damage(self, current_blue_pokemon, current_red_pokemon):
        damage = gen.get_damage(red_level=current_blue_pokemon.level, red_attack=current_blue_pokemon.attack,
                                blue_defence=current_red_pokemon.defence,
                                red_move_base=self.blue_selected_move.base_power,
                                red_modifier=current_blue_pokemon.modifier)
        current_blue_pokemon.take_damage(damage)
        current_blue_pokemon.save()

    @staticmethod
    def get_current_pokemon(blue_team, current_blue_pokemon, current_red_pokemon, red_team):
        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon

            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

            if current_red_pokemon and current_blue_pokemon:
                break

        return blue_pokemon, current_blue_pokemon, current_red_pokemon, red_pokemon

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