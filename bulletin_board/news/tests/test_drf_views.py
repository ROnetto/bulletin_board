import pytest
from django.test import RequestFactory

from bulletin_board.apartments.api.views import ApartmentViewSet
from bulletin_board.apartments.models import Apartment

pytestmark = pytest.mark.django_db


class TestApartmentViewSet:
    def test_get_queryset(self, apartment: Apartment, rf: RequestFactory):
        view = ApartmentViewSet()
        request = rf.get("/fake-url/")
        # request.user = user

        view.request = request

        assert apartment in view.get_queryset()
