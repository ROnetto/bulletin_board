from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.buildings.models import Building


class BuildingViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = BuildingSerializer
    queryset = Building.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
