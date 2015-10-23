from django.db import models
from pokemon.models import Pokemon


class Player(models.Model):
    username = models.CharField(max_length=20)
    team = models.ForeignKey(Pokemon)  # This is just a single okemon until teams are added
    usable_pokemon = 1 # Just a single Pokemon at the moment

    def get_and_update_usable_pokemon(self):
        usable_pokemon = 0
        #for pokemon in self.team:
        #    if not pokemon.feinted:
        #        usable_pokemon += 1
        if not self.team.fainted:
            usable_pokemon += 1

        self.usable_pokemon = usable_pokemon

    def __unicode__(self):
        return self.username