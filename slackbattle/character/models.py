from django.db import models

CHARACTER_TYPES = (
        ("npc", "NPC"),
        ("pc", "PC"),
        ("monster", "Monster"),
        )

class Character(models.Model):
    name = models.CharField(max_length=255)
    character_type = models.CharField(max_length=7, choices=CHARACTER_TYPES)
    hit_points = models.IntegerField()
    armor_class = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
