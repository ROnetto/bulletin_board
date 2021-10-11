import pytest
from django.urls import resolve, reverse

from bulletin_board.buildings.models import Building

pytestmark = pytest.mark.django_db


def test_building_detail(building: Building):
    assert (
        reverse("api:building-detail", kwargs={"uuid": building.uuid})
        == f"/api/buildings/{building.uuid}/"
    )
    assert (
        resolve(f"/api/buildings/{building.uuid}/").view_name == "api:building-detail"
    )


def test_building_list():
    assert reverse("api:building-list") == "/api/buildings/"
    assert resolve("/api/buildings/").view_name == "api:building-list"
