from django.test import TestCase
from playerpokemon.models import PlayerPokemon
from pokemon.models import Pokemon
from type.models import Type
from move.models import Move
import genx.models as gen


class TestPlayerPokemon(TestCase):
    def setUp(self):
        self.type = Type(name=Type.NORMAL)
        self.type.save()

        self.move = Move(name='Tackle', type=self.type, base_power=50)
        self.move.save()

        self.pokemon = Pokemon(type1=self.type)
        self.pokemon.save()

        self.player_pokemon = PlayerPokemon(pokemon=self.pokemon, base_pbv_value=5, level=50, move1=self.move)
        self.player_pokemon.save()

    def test_pokemon_can_take_damage(self):
        self.player_pokemon.take_damage(90)

        self.assertEqual(self.player_pokemon.hp, 9)  # 10 - 5 = 5
        self.assertEqual(self.player_pokemon.fainted, False)

    def test_pokemon_can_faint(self):
        self.assertEqual(self.player_pokemon.hp, 99)
        self.assertEqual(self.player_pokemon.fainted, False)

        self.player_pokemon.take_damage(99)

        self.assertEqual(self.player_pokemon.hp, 0)
        self.assertEqual(self.player_pokemon.fainted, True)

    def test_get_pbv_value(self):
        self.assertEqual(self.player_pokemon.get_pbv_value(), 25)

    def test_set_stats(self):
        calc_hp = gen.calc_hp(base_stat=self.pokemon.base_hp, iv=0, ev=0, level=50)
        self.assertEqual(calc_hp, self.player_pokemon.hp)

