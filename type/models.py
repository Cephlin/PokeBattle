from django.db import models


class Type(models.Model):
    NORMAL = 'Normal'
    FIRE = 'Fire'
    WATER = 'Water'
    ELECTRIC = 'Electric'
    GRASS = 'Grass'
    ICE = 'Ice'
    FIGHTING = 'Fighting'
    POISON = 'Poison'
    GROUND = 'Ground'
    FLYING = 'Flying'
    PSYCHIC = 'Psychic'
    BUG = 'Bug'
    ROCK = 'Rock'
    GHOST = 'Ghost'
    DRAGON = 'Dragon'

    TYPES = ((NORMAL, 'Normal'),
             (FIRE, 'Fire'),
             (WATER, 'Water'),
             (ELECTRIC, 'Electric'),
             (GRASS, 'Grass'),
             (ICE, 'Ice'),
             (FIGHTING, 'Fighting'),
             (POISON, 'Poison'),
             (GROUND, 'Ground'),
             (FLYING, 'Flying'),
             (PSYCHIC, 'Psychic'),
             (BUG, 'Bug'),
             (ROCK, 'Rock'),
             (GHOST, 'Ghost'),
             (DRAGON, 'Dragon'),
             )

    name = models.CharField(max_length=10, choices=TYPES, default=NORMAL)