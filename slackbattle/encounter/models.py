from django.db import models
from character.models import Character


class Encounter(models.Model):
    name = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character)
