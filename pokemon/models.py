from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50, default='Charmander')

    type1 = models.ForeignKey('type.Type', related_name='%(app_label)s_%(class)s_type1')
    type2 = models.ForeignKey('type.Type', related_name='%(app_label)s_%(class)s_type2', null=True, blank=True)

    base_hp = models.IntegerField(default=39)
    base_attack = models.IntegerField(default=52)
    base_defence = models.IntegerField(default=43)
    base_special = models.IntegerField(default=50)
    base_speed = models.IntegerField(default=65)

    def __unicode__(self):
        return self.name
