from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.buildings.models import Building

User = get_user_model()


class BuildingViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
