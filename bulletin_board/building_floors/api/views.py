from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.building_floors.api.serializers import BuildingFloorSerializer
from bulletin_board.building_floors.models import BuildingFloor


class BuildingFloorViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = BuildingFloorSerializer
    queryset = BuildingFloor.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
