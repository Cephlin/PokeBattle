from django.db import models
from pokemon.models import Pokemon
import numpy


# Create your models here.
class Gen(models.Model):
    red_pokemon = models.ForeignKey(Pokemon, related_name='%(app_label)s_%(class)s_red_pokemon')
    blue_pokemon = models.ForeignKey(Pokemon,related_name='%(app_label)s_%(class)s_blue_pokemon')

    def get_damage(self, red_level, red_attack, blue_defence, red_move_base, red_modifier):
        damage_part1 = (2 * red_level + 10) / 250
        damage_part2 = red_attack / blue_defence
        damage = ((damage_part1 * damage_part2 * red_move_base) + 2) * red_modifier
        return damage

    def get_modifier(self, stab, type, critical, other):
        #  Other means:
        modifier = stab * type * critical * other * numpy.random.uniform(0.85, 1.0)
        return modifier

    # class Meta:
    #     abstract = True