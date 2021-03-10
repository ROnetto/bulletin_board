from django.contrib.auth import get_user_model
from rest_framework import serializers

from community_manager.buildings.models import Building
from community_manager.communities.api.serializers import CommunitySerializer
from community_manager.core.serializers import BasicSerializer

User = get_user_model()


class BuildingSerializer(BasicSerializer):
    community_id = serializers.IntegerField(write_only=True)
    community = CommunitySerializer(many=False, read_only=True)

    class Meta:
        model = Building
        fields = ["id", "created", "modified", "community_id", "community", "name"]
