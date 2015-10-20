from django.db import models
from pokemon.models import Pokemon


class Player(models.Model):
    username = models.CharField(max_length=20)
    team = models.ForeignKey(Pokemon)  # This is just a single pokemon until teams are added

    def __unicode__(self):
        return self.username