import pytest
from django.urls import resolve, reverse

from bulletin_board.building_floors.models import BuildingFloor

pytestmark = pytest.mark.django_db


def test_building_floor_detail(building_floor: BuildingFloor):
    assert (
        reverse("api:buildingfloor-detail", kwargs={"uuid": building_floor.uuid})
        == f"/api/building_floors/{building_floor.uuid}/"
    )
    assert (
        resolve(f"/api/building_floors/{building_floor.uuid}/").view_name
        == "api:buildingfloor-detail"
    )


def test_building_list():
    assert reverse("api:buildingfloor-list") == "/api/building_floors/"
    assert resolve("/api/building_floors/").view_name == "api:buildingfloor-list"
