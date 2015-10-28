from django.test import TestCase
from player.models import Player
from pokemon.models import Pokemon
from type.models import Type


class TestPokemon(TestCase):
    def setUp(self):
        self.type = Type(name="Normal")
        self.type.save()
        self.pokemon = Pokemon(name="Charmander", hp=10, attack=3, type=self.type)
        self.pokemon.save()

    def tearDown(self):
        self.type = None
        self.pokemon = None

    def test_pokemon_can_take_damage(self):
        self.pokemon.take_damage(5)

        self.assertEqual(self.pokemon.hp, 5)  # 10 - 5 = 5
        self.assertEqual(self.pokemon.fainted, False)

    def test_pokemon_can_faint(self):
        self.assertEqual(self.pokemon.hp, 10)
        self.assertEqual(self.pokemon.fainted, False)

        self.pokemon.take_damage(10)

        self.assertEqual(self.pokemon.hp, 0)
        self.assertEqual(self.pokemon.fainted, True)
