from django.test import TestCase
from mock import patch
from genx.models import Gen
from pokemon.models import Pokemon
from player.models import Player
from battle.models import Battle


class TestType(TestCase):
    #@patch('genx.models.Gen', return_value=1)
    def test_get_damage(self):
        self.red_level = 75
        self.red_attack = 123
        self.blue_defence = 163
        self.red_move_base = 65
        self.red_modifier = 6.00
        self.gen = Gen()
        damage = self.gen.get_damage(red_level=self.red_level, red_attack=self.red_attack,
                                     blue_defence=self.blue_defence, red_move_base=self.red_move_base,
                                     red_modifier=self.red_modifier)
        # (((((2 * level) + 10) / 250) * (attack / defence) * base) + 2) * modifier
        # (((((2 * 5) + 10) / 250) * (10 / 10) * 50) + 2) * 1 = ((2 /25) * 50) + 2 = 4
        self.assertEqual(int(damage), 200)

    """
    def do_setup(self, red_attack, red_speed, blue_attack, blue_speed):
        self.red_pokemon = Pokemon(name='Charmander', attack=red_attack, speed=red_speed)
        self.red_pokemon.save()
        self.blue_pokemon = Pokemon(name='Squirtle', attack=blue_attack, speed=blue_speed)
        self.blue_pokemon.save()
        self.red = Player(username='red', pokemon1=self.red_pokemon)
        self.red.save()
        self.blue = Player(username='blue', pokemon1=self.blue_pokemon)
        self.blue.save()
        self.battle = Battle(red=self.red, blue=self.blue)
        self.battle.save()
    """
