from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.communities.models import Community


class CommunityViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = CommunitySerializer
    queryset = Community.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
