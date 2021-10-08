from django.contrib.auth import get_user_model
from rest_framework import serializers

from bulletin_board.buildings.models import Building
from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.core.serializers import BasicSerializer

User = get_user_model()


class BuildingSerializer(BasicSerializer):
    community_id = serializers.IntegerField(write_only=True)
    community = CommunitySerializer(many=False, read_only=True)

    class Meta:
        model = Building
        fields = ["id", "created", "modified", "community_id", "community", "name"]
