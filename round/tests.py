from django.test import TestCase
from pokemon.models import Pokemon
from player.models import Player
from battle.models import Battle
from round.models import Round


class TestRound(TestCase):
    def test_fight(self):
        self.do_setup(red_attack=3, red_speed=10, blue_attack=3, blue_speed=7)

        round1 = Round(battle=self.battle, red=self.red, blue=self.blue)
        round1.save()

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(self.battle.red.pokemon1.hp, 10)
        self.assertEqual(self.battle.blue.pokemon1.hp, 10)

        round2 = round1.advance_round()
        round2.save()

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(self.battle.red.pokemon1.hp, 7)
        self.assertEqual(self.battle.blue.pokemon1.hp, 7)

        round3 = round2.advance_round()
        round3.save()

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(self.battle.red.pokemon1.hp, 4)
        self.assertEqual(self.battle.blue.pokemon1.hp, 4)

        round4 = round3.advance_round()
        round4.save()

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(self.battle.red.pokemon1.hp, 1)
        self.assertEqual(self.battle.blue.pokemon1.hp, 1)

        round5 = round4.advance_round()

        self.assertEqual(self.battle.red.pokemon1.hp, 1)
        self.assertEqual(self.battle.blue.pokemon1.hp, 0)
        self.assertEqual(self.battle.winner, self.red)

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
