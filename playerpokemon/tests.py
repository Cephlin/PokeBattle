from django.test import TestCase
from playerpokemon.models import PlayerPokemon


class TestPlayerPokemon(TestCase):
    def setUp(self):
        self.player_pokemon = PlayerPokemon(hp=10, base_pbv_value=5)
        self.player_pokemon.save()

    def tearDown(self):
        self.player_pokemon = None

    def test_pokemon_can_take_damage(self):
        self.player_pokemon.take_damage(5)

        self.assertEqual(self.player_pokemon.hp, 5)  # 10 - 5 = 5
        self.assertEqual(self.player_pokemon.fainted, False)

    def test_pokemon_can_faint(self):
        self.assertEqual(self.player_pokemon.hp, 10)
        self.assertEqual(self.player_pokemon.fainted, False)

        self.player_pokemon.take_damage(10)

        self.assertEqual(self.player_pokemon.hp, 0)
        self.assertEqual(self.player_pokemon.fainted, True)

    def test_get_pbv_value(self):
        self.assertEqual(self.player_pokemon.get_pbv_value(), 25)