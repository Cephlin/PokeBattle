from django.test import TestCase
from player.models import Player
from pokemon.models import Pokemon
from playerpokemon.models import PlayerPokemon
from move.models import Move
from type.models import Type


# Create your tests here.
class TestPlayer(TestCase):
    def setUp(self):
        self.type = Type(name=Type.NORMAL)
        self.type.save()

        self.move = Move(name='Tackle', type=self.type, base_power=50)
        self.move.save()

        self.pokemon = Pokemon(name="Charmander", type1=self.type)
        self.pokemon.save()

        self.player_pokemon = PlayerPokemon(pokemon=self.pokemon, move1=self.move)
        self.player_pokemon.save()

        self.red = Player(username='red') # Will need to be changed to use a real Team
        self.red.save()

        self.player_pokemon.player = self.red
        self.player_pokemon.pokemon = self.pokemon
        self.player_pokemon.save()

    def test_get_and_update_usable_pokemon(self):
        self.red.check_usable_pokemon()

        self.assertEqual(self.red.usable_pokemon, 1)

    def test_get_and_update_usable_pokemon_when_one_faints(self):
        self.assertEqual(self.player_pokemon.player.usable_pokemon, 1)

        self.player_pokemon.take_damage(self.player_pokemon.hp)
        self.player_pokemon.player.check_usable_pokemon()

        self.assertEqual(self.player_pokemon.player.usable_pokemon, 0)
