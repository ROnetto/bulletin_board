import pytest
from django.urls import resolve, reverse

from bulletin_board.apartments.models import Apartment

pytestmark = pytest.mark.django_db


def test_apartment_detail(apartment: Apartment):
    assert (
        reverse("api:apartment-detail", kwargs={"uuid": apartment.uuid})
        == f"/api/apartments/{apartment.uuid}/"
    )
    assert (
        resolve(f"/api/apartments/{apartment.uuid}/").view_name
        == "api:apartment-detail"
    )


def test_building_list():
    assert reverse("api:apartment-list") == "/api/apartments/"
    assert resolve("/api/apartments/").view_name == "api:apartment-list"
