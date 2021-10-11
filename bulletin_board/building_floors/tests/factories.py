from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bulletin_board.building_floors.models import BuildingFloor
from bulletin_board.buildings.tests.factories import BuildingFactory


class BuildingFloorFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    number = Faker("random_int")

    building = SubFactory(BuildingFactory)

    class Meta:
        model = BuildingFloor
        django_get_or_create = ["uuid"]
