from factory import Faker
from factory.django import DjangoModelFactory

from bulletin_board.communities.models import Community


class CommunityFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    name = Faker("name")

    class Meta:
        model = Community
        django_get_or_create = ["uuid"]
