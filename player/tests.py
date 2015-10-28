from django.test import TestCase
from player.models import Player
from pokemon.models import Pokemon
from type.models import Type


# Create your tests here.
class TestPlayer(TestCase):
    def setUp(self):
        self.type = Type(name="Normal")
        self.type.save()

        self.pokemon = Pokemon(name="Charmander", type=self.type)
        self.pokemon.save()

        self.red = Player(username='red', pokemon1=self.pokemon) # Will need to be changed to use a real Team
        self.red.save()

    def tearDown(self):
        self.type = None
        self.pokemon = None
        self.red = None

    def test_get_and_update_usable_pokemon(self):
        self.red.check_usable_pokemon()

        self.assertEqual(self.red.usable_pokemon, 1)

    def test_get_and_update_usable_pokemon_when_one_faints(self):
        self.red.pokemon1.take_damage(10)
        self.red.check_usable_pokemon()

        self.assertEqual(self.red.usable_pokemon, 0)
