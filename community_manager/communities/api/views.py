from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from community_manager.communities.api.serializers import CommunitySerializer
from community_manager.communities.models import Community

User = get_user_model()


class CommunityViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = CommunitySerializer
    queryset = Community.objects.all()
