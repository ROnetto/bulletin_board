import pytest

from bulletin_board.communities.models import Community
from bulletin_board.communities.tests.factories import CommunityFactory
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
