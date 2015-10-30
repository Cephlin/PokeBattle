from django.test import TestCase
from pokemon.models import Pokemon
from player.models import Player
from battle.models import Battle
from round.models import Round
from type.models import Type
from playerpokemon.models import PlayerPokemon
from move.models import Move
from itertools import izip


class TestRound(TestCase):
    def test_fight(self):
        self.do_setup(red_attack=3, red_speed=10, blue_attack=3, blue_speed=7)

        round1 = Round(battle=self.battle, red=self.red, blue=self.blue)
        round1.save()

        red_team = PlayerPokemon.objects.filter(player=round1.red)
        blue_team = PlayerPokemon.objects.filter(player=round1.blue)

        current_red_pokemon = None
        current_blue_pokemon = None

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon

            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

            if current_red_pokemon and current_blue_pokemon:
                break

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(current_red_pokemon.hp, 18)
        self.assertEqual(current_blue_pokemon.hp, 19)

        round1.red_selected_move = current_red_pokemon.move1
        round1.blue_selected_move = current_blue_pokemon.move1
        round1.save()

        round2 = round1.advance_round()
        round2.save()

        """
        red_team = PlayerPokemon.objects.filter(player=round1.red)
        blue_team = PlayerPokemon.objects.filter(player=round1.blue)

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon
            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

        self.assertEqual(self.battle.winner, None)
        self.assertLess(current_red_pokemon.hp, 18)
        self.assertLess(current_blue_pokemon.hp, 18)

        round3 = round2.advance_round()
        round3.save()

        red_team = PlayerPokemon.objects.filter(player=round1.red)
        blue_team = PlayerPokemon.objects.filter(player=round1.blue)

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon
            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(current_red_pokemon.hp, 4)
        self.assertEqual(current_blue_pokemon.hp, 4)

        round4 = round3.advance_round()
        round4.save()

        red_team = PlayerPokemon.objects.filter(player=round4.red)
        blue_team = PlayerPokemon.objects.filter(player=round4.blue)

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon
            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

        self.assertEqual(self.battle.winner, None)
        self.assertEqual(current_red_pokemon.hp, 1)
        self.assertEqual(current_blue_pokemon.hp, 1)

        round5 = round4.advance_round()

        red_team = PlayerPokemon.objects.filter(player=round4.red)
        blue_team = PlayerPokemon.objects.filter(player=round4.blue)

        for red_pokemon, blue_pokemon in izip(red_team, blue_team):
            if red_pokemon.lead:
                current_red_pokemon = red_pokemon
            if blue_pokemon.lead:
                current_blue_pokemon = blue_pokemon

        self.assertEqual(self.battle.winner, self.red)
        self.assertEqual(current_red_pokemon.hp, 1)
        self.assertEqual(current_blue_pokemon.hp, 0)
        """

    def do_setup(self, red_attack, red_speed, blue_attack, blue_speed):
        self.create_players()
        self.create_pokemon(blue_attack, blue_speed, red_attack, red_speed)

        self.battle = Battle(red=self.red, blue=self.blue)
        self.battle.save()

    def create_players(self):
        self.red = Player(username='red')
        self.red.save()
        self.blue = Player(username='blue')
        self.blue.save()

    def create_pokemon(self, blue_attack, blue_speed, red_attack, red_speed):
        self.move_type = Type(name=Type.NORMAL)
        self.move_type.save()

        self.red_type = Type(name=Type.FIRE)
        self.red_type.save()

        self.blue_type = Type(name=Type.WATER)
        self.blue_type.save()

        self.move = Move(name='Tackle', type=self.move_type, base_power=50)
        self.move.save()

        self.red_pokemon = Pokemon(type1=self.red_type)
        self.red_pokemon.save()

        self.blue_pokemon = Pokemon(name='Squirtle', type1=self.blue_type,
                                    base_hp=44, base_attack=48, base_defence=65, base_special=50, base_speed=43)
        self.blue_pokemon.save()

        self.red_playerpokemon = PlayerPokemon(pokemon=self.red_pokemon, player=self.red,
                                               lead=True, move1=self.move)
        self.red_playerpokemon.save()
        self.blue_playerpokemon = PlayerPokemon(pokemon=self.blue_pokemon, player=self.blue,
                                                lead=True, move1=self.move)
        self.blue_playerpokemon.save()
