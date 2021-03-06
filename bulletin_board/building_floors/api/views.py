from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from bulletin_board.building_floors.api.serializers import BuildingFloorSerializer
from bulletin_board.building_floors.models import BuildingFloor

User = get_user_model()


class BuildingFloorViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = BuildingFloorSerializer
    queryset = BuildingFloor.objects.all()
