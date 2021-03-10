from django.contrib.auth import get_user_model

from community_manager.communities.models import Community
from community_manager.core.serializers import BasicSerializer

User = get_user_model()


class CommunitySerializer(BasicSerializer):
    class Meta:
        model = Community
        fields = ["id", "created", "modified", "name"]
