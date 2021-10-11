from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bulletin_board.buildings.tests.factories import BuildingFactory
from bulletin_board.communities.tests.factories import CommunityFactory
from bulletin_board.news.models import BuildingNews, CommunityNews


class BuildingNewsFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    title = Faker("sentence", nb_words=5)
    text = Faker("sentence", nb_words=50)
    expiration_date = Faker("date_time")

    building = SubFactory(BuildingFactory)

    class Meta:
        model = BuildingNews
        django_get_or_create = ["uuid"]


class CommunityNewsFactory(DjangoModelFactory):
    uuid = Faker("uuid4")
    title = Faker("sentence", nb_words=5)
    text = Faker("sentence", nb_words=50)
    expiration_date = Faker("date_time")

    community = SubFactory(CommunityFactory)

    class Meta:
        model = CommunityNews
        django_get_or_create = ["uuid"]
