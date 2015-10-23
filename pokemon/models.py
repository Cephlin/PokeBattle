from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    attack = models.IntegerField()
    feinted = models.BooleanField(default=False)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            feinted = True

    def __unicode__(self):
        return self.name