import pytest
from django.test import RequestFactory

from bulletin_board.building_floors.api.views import BuildingFloorViewSet
from bulletin_board.building_floors.models import BuildingFloor

pytestmark = pytest.mark.django_db


class TestBuildingFloorViewSet:
    def test_get_queryset(self, building_floor: BuildingFloor, rf: RequestFactory):
        view = BuildingFloorViewSet()
        request = rf.get("/fake-url/")
        # request.user = user

        view.request = request

        assert building_floor in view.get_queryset()
