from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bulletin_board.apartments.models import Apartment
from bulletin_board.building_floors.tests.factories import BuildingFloorFactory


class ApartmentFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    number = Faker("building_number")

    building_floor = SubFactory(BuildingFloorFactory)

    class Meta:
        model = Apartment
        django_get_or_create = ["uuid"]
