from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)

    type1 = models.ForeignKey('type.Type', related_name='%(app_label)s_%(class)s_type1', null=True, blank=True)
    type2 = models.ForeignKey('type.Type', related_name='%(app_label)s_%(class)s_type2', null=True, blank=True)

    base_hp = models.IntegerField(default=10)
    base_attack = models.IntegerField(default=10)
    base_defence = models.IntegerField(default=10)
    base_special_attack = models.IntegerField(default=10)
    base_special_defence = models.IntegerField(default=10)
    base_speed = models.IntegerField(default=10)

    def __unicode__(self):
        return self.name
