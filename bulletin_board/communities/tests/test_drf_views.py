import pytest
from django.test import RequestFactory

from bulletin_board.communities.api.views import CommunityViewSet
from bulletin_board.communities.models import Community

pytestmark = pytest.mark.django_db


class TestCommunityViewSet:
    def test_get_queryset(self, community: Community, rf: RequestFactory):
        view = CommunityViewSet()
        request = rf.get("/fake-url/")
        # request.user = user

        view.request = request

        assert community in view.get_queryset()
