from django.test import TestCase
from mock import patch
from genx.models import Gen
from pokemon.models import Pokemon
from player.models import Player
from battle.models import Battle


class TestType(TestCase):
    @patch('genx.models.Gen', return_value=1)
    def test_get_damage(self):
        red_level = 1
        red_attack = 1
        blue_defence = 1
        red_move_base = 1
        red_modifier = Gen.get_modifier()
        damage = Gen.get_damage(self, red_level, red_attack, blue_defence, red_move_base, red_modifier)
        self.assertEqual(damage, 50)

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