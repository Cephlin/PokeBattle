from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    attack = models.IntegerField()

    def __unicode__(self):
        return self.name