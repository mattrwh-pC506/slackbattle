from django.db import models

CHARACTER_TYPES = (
        ("npc", "NPC"),
        ("pc", "PC"),
        ("monster", "Monster"),
        )

class Character(models.Model):
    name = models.CharField(max_length=255)
    character_type = models.CharField(max_length=7, choices=CHARACTER_TYPES, null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)
