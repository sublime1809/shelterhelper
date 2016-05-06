from django.db import models

from pets import constants
from pets.models.pet_models import Pet


class Dog(Pet):
    breeds = models.ManyToManyField(DogBreed, null=False)


class DogBreed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=constants.SIZES)


class Walk(models.Model):
    dog = models.ForeignKey(Dog, related_name='walks')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    had_peed = models.BooleanField(default=False)
    had_pooped = models.BooleanField(default=False)
