from django.db import models


class PlayerPokemon(models.Model):
    pokemon = models.ForeignKey('pokemon.Pokemon', null=True, blank=True)
    player = models.ForeignKey('player.Player', null=True, blank=True)

    move1 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move1', null=True, blank=True)
    move2 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move2', null=True, blank=True)
    move3 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move3', null=True, blank=True)
    move4 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move4', null=True, blank=True)

    nickname = models.CharField(max_length=20, null=True, blank=True)

    level = models.IntegerField(default=5)

    hp = models.IntegerField(default=10)
    attack = models.IntegerField(default=3)
    defence = models.IntegerField(default=10)
    special = models.IntegerField(default=10)
    # special_attack = models.IntegerField(default=10)
    # special_defence = models.IntegerField(default=10)
    speed = models.IntegerField(default=10)

    lead = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    fainted = models.BooleanField(default=False)
    base_pbv_value = models.IntegerField(default=23) # This would have an actual value of 115 PBV since we work in 5's

    def get_pbv_value(self):
        return self.base_pbv_value * 5

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.fainted = True
            self.hp = 0
        self.save()