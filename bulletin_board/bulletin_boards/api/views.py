from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.bulletin_boards.api.serializers import (
    BuildingBulletinBoardSerializer,
    CommunityBulletinBoardSerializer,
)
from bulletin_board.bulletin_boards.models import (
    BuildingBulletinBoard,
    CommunityBulletinBoard,
)


class CommunityBulletinBoardViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = CommunityBulletinBoardSerializer
    queryset = CommunityBulletinBoard.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]


class BuildingBulletinBoardViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = BuildingBulletinBoardSerializer
    queryset = BuildingBulletinBoard.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
