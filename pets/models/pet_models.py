from django.db import models

from pets import constants


class Pet(models.Model):
    name = models.CharField(max_length=200)
    intake_date = models.DateTimeField()
    intake_reason = models.TextField()
    gender = models.CharField(max_length=10, choices=constants.GENDERS)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    hold_create_at = models.DateTimeField(null=True)

    is_housetrained = models.BooleanField(null=True)
    is_good_with_kids = models.BooleanField(null=True)
    is_good_with_cats = models.BooleanField(null=True)
    is_good_with_dogs = models.BooleanField(null=True)
    is_fixed = models.BooleanField(null=True)

    class Meta:
        abstract = True


class PetNote(models.Model):
    pet = models.ForeignKey(Pet, related_name='notes')
    note = models.TextField()


class PetMedia(models.Model):
    pet = models.ForeignKey(Pet, related_name='media')
    # TODO: find where to save these
    image = models.ImageField()
    video = models.FileField()
