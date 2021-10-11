import pytest

from bulletin_board.apartments.models import Apartment
from bulletin_board.apartments.tests.factories import ApartmentFactory
from bulletin_board.building_floors.models import BuildingFloor
from bulletin_board.building_floors.tests.factories import BuildingFloorFactory
from bulletin_board.buildings.models import Building
from bulletin_board.buildings.tests.factories import BuildingFactory
from bulletin_board.communities.models import Community
from bulletin_board.communities.tests.factories import CommunityFactory
from bulletin_board.news.models import BuildingNews, CommunityNews
from bulletin_board.news.tests.factories import (
    BuildingNewsFactory,
    CommunityNewsFactory,
)
from bulletin_board.users.models import User
from bulletin_board.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def community() -> Community:
    return CommunityFactory()


@pytest.fixture
def building() -> Building:
    return BuildingFactory()


@pytest.fixture
def building_floor() -> BuildingFloor:
    return BuildingFloorFactory()


@pytest.fixture
def apartment() -> Apartment:
    return ApartmentFactory()


@pytest.fixture
def building_news() -> BuildingNews:
    return BuildingNewsFactory()


@pytest.fixture
def community_news() -> CommunityNews:
    return CommunityNewsFactory()
