from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.communities.models import Community

User = get_user_model()


class CommunityViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    lookup_field = "uuid"
    serializer_class = CommunitySerializer
    queryset = Community.objects.all()
