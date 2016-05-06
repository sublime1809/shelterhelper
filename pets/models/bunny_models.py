from django.db import models

from pets import constants
from pets.models.pet_models import Pet


class Bunny(Pet):
    breeds = models.ManyToManyField(BunnyBreed, null=False)


class BunnyBreed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=constants.SIZES)
