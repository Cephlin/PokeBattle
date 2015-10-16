from django.db import models

class Player():
    username = models.CharField(max_length=20)
