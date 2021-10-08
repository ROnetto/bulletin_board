from django.contrib.auth import get_user_model

from bulletin_board.communities.models import Community
from bulletin_board.core.serializers import BasicSerializer

User = get_user_model()


class CommunitySerializer(BasicSerializer):
    class Meta:
        model = Community
        fields = ["id", "created", "modified", "name"]
