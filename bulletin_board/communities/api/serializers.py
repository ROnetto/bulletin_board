from django.contrib.auth import get_user_model
from rest_framework import serializers

from bulletin_board.communities.models import Community
from bulletin_board.core.serializers import BasicSerializer
from bulletin_board.users.api.serializers import UserSerializer

User = get_user_model()


class CommunitySerializer(BasicSerializer):
    admins_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, many=True
    )
    admins = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = [
            "id",
            "created",
            "modified",
            "uuid",
            "name",
            "admins_id",
            "admins",
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:community-detail", "lookup_field": "uuid"}
        }
