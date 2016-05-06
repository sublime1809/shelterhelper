from api.views import base_pet_views

from pets.models.dog_models import Dog


class DogIndexView(base_pet_views.PetIndexView):
    model = Dog


class DogListView(base_pet_views.PetListView):
    model = Dog


class DogQueryView(base_pet_views.PetQueryView):
    model = Dog
