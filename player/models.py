from django.db import models
from playerpokemon.models import PlayerPokemon


class Player(models.Model):
    username = models.CharField(max_length=20)
    team = models.ManyToManyField('pokemon.Pokemon', through='playerpokemon.PlayerPokemon')
    usable_pokemon = 1 # Just a single Pokemon at the moment

    def check_usable_pokemon(self):
        usable_pokemon = 0
        for player_pokemon in PlayerPokemon.objects.filter(player=self):
            if not player_pokemon.fainted:
                usable_pokemon += 1

        self.usable_pokemon = usable_pokemon
        self.save()

    def __unicode__(self):
        return self.username