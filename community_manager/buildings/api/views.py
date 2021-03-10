from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from community_manager.buildings.api.serializers import BuildingSerializer
from community_manager.buildings.models import Building

User = get_user_model()


class BuildingViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
