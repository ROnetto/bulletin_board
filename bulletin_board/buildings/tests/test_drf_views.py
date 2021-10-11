import pytest
from django.test import RequestFactory

from bulletin_board.buildings.api.views import BuildingViewSet
from bulletin_board.buildings.models import Building

pytestmark = pytest.mark.django_db


class TestBuildingViewSet:
    def test_get_queryset(self, building: Building, rf: RequestFactory):
        view = BuildingViewSet()
        request = rf.get("/fake-url/")
        # request.user = user

        view.request = request

        assert building in view.get_queryset()
