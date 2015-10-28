from django.db import models
from type.models import Type


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type)

    hp = models.IntegerField(default=10)
    attack = models.IntegerField(default=3)
    defence = models.IntegerField(default=10)
    special_attack = models.IntegerField(default=10)
    special_defence = models.IntegerField(default=10)
    speed = models.IntegerField(default=10)

    priority = models.IntegerField(default=1)
    fainted = models.BooleanField(default=False)
    base_pbv_value = models.IntegerField(default=23) # This would have an actual value of 115 PBV since we work in 5's

    def get_pbv_value(self):
        return self.base_pbv_value * 5

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.fainted = True
            self.hp = 0

    def __unicode__(self):
        return self.name