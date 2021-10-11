from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.news.api.serializers import (
    BuildingNewsSerializer,
    CommunityNewsSerializer,
)
from bulletin_board.news.models import BuildingNews, CommunityNews


class CommunityNewsViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = CommunityNewsSerializer
    queryset = CommunityNews.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]


class BuildingNewsViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = BuildingNewsSerializer
    queryset = BuildingNews.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
