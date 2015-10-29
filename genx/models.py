from django.db import models
from playerpokemon.models import PlayerPokemon
import numpy


class Gen(models.Model):
    def get_damage(self, red_level, red_attack, blue_defence, red_move_base, red_modifier):
        # Check for doubles only
        damage_part1 = ((2.0 * float(red_level)) + 10.0) / 250.0
        damage_part2 = float(red_attack) / float(blue_defence)
        damage = ((damage_part1 * damage_part2 * float(red_move_base)) + 2.0) * float(red_modifier)

        return damage

    def get_modifier(self, stab, type, critical, other):
        #  Other means:
        modifier = stab * type * critical * other * numpy.random.uniform(0.85, 1.0)
        return modifier

    def set_stats(self, player_pokemon):
        if isinstance(player_pokemon, PlayerPokemon):
            do_stuff = "stuff"
            player_pokemon.hp = self.calc_hp(base_stat=player_pokemon.pokemon.base_hp,
                                             iv=player_pokemon.iv,
                                             ev=player_pokemon.ev,
                                             level=player_pokemon.level)

            player_pokemon.attack = self.calc_other_stat(base_stat=player_pokemon.pokemon.base_attack,
                                                         iv=player_pokemon.iv,
                                                         ev=player_pokemon.ev,
                                                         level=player_pokemon.level)

            player_pokemon.defence = self.calc_other_stat(base_stat=player_pokemon.pokemon.base_attack,
                                                          iv=player_pokemon.iv,
                                                          ev=player_pokemon.ev,
                                                          level=player_pokemon.level)

            player_pokemon.special = self.calc_other_stat(base_stat=player_pokemon.pokemon.base_attack,
                                                          iv=player_pokemon.iv,
                                                          ev=player_pokemon.ev,
                                                          level=player_pokemon.level)

            player_pokemon.speed = self.calc_other_stat(base_stat=player_pokemon.pokemon.base_attack,
                                                        iv=player_pokemon.iv,
                                                        ev=player_pokemon.ev,
                                                        level=player_pokemon.level)


    def calc_hp(self, base_stat, iv, ev, level):
        hp = int(self.calc_stat_part(base_stat, iv, ev, level) + float(level) + 10.0)
        return hp

    def calc_other_stat(self, base_stat, iv, ev, level):
        stat = int(self.calc_stat_part(base_stat, iv, ev, level) + 5.0)
        return stat

    def calc_stat_part(self, base_stat, iv, ev, level):
        sqrt_of_ev = numpy.sqrt(numpy.absolute(float(ev)))
        return (float(base_stat) + float(iv)) * 2 + (sqrt_of_ev / 4.0) * float(level) / 100.0

