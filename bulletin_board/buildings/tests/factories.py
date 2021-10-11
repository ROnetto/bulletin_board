from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bulletin_board.buildings.models import Building
from bulletin_board.communities.tests.factories import CommunityFactory


class BuildingFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    name = Faker("name")
    address = Faker("address")

    community = SubFactory(CommunityFactory)

    class Meta:
        model = Building
        django_get_or_create = ["uuid"]
