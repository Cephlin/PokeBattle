from django.db import models
import genx.models as gen


class PlayerPokemon(models.Model):
    pokemon = models.ForeignKey('pokemon.Pokemon', null=True)
    player = models.ForeignKey('player.Player', null=True, blank=True)

    move1 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move1')
    move2 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move2', null=True, blank=True)
    move3 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move3', null=True, blank=True)
    move4 = models.ForeignKey('move.Move', related_name='%(app_label)s_%(class)s_move4', null=True, blank=True)

    nickname = models.CharField(max_length=20, null=True, blank=True)

    level = models.IntegerField(default=5)

    hp = models.IntegerField(default=10)
    attack = models.IntegerField(default=5)
    defence = models.IntegerField(default=5)
    special = models.IntegerField(default=5)
    speed = models.IntegerField(default=5)

    iv = models.IntegerField(default=0)
    ev= models.IntegerField(default=0)

    lead = models.BooleanField(default=False)
    modifier = models.FloatField(default=0.0)
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

    def set_stats(self):
        if not self.pk:
            self.hp = gen.calc_hp(base_stat=self.pokemon.base_hp, iv=self.iv, ev=self.ev, level=self.level)
            self.attack = gen.calc_other_stat(base_stat=self.pokemon.base_attack, iv=self.iv, ev=self.ev, level=self.level)
            self.defence = gen.calc_other_stat(base_stat=self.pokemon.base_attack, iv=self.iv, ev=self.ev, level=self.level)
            self.special = gen.calc_other_stat(base_stat=self.pokemon.base_attack, iv=self.iv, ev=self.ev, level=self.level)
            self.speed = gen.calc_other_stat(base_stat=self.pokemon.base_attack, iv=self.iv, ev=self.ev, level=self.level)

            if self.pk:
                self.save()

    def save(self, *args, **kwargs):
        if not self.pk:  # object is being created, thus no primary key field yet
           self.set_stats()
        super(PlayerPokemon, self).save(*args, **kwargs)