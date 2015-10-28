from django.db import models
from pokemon.models import Pokemon
import numpy


class Gen(models.Model):
    red_pokemon = models.ForeignKey(Pokemon, related_name='%(app_label)s_%(class)s_red_pokemon')
    blue_pokemon = models.ForeignKey(Pokemon,related_name='%(app_label)s_%(class)s_blue_pokemon')

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

    # class Meta:
    #     abstract = True