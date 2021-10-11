from django.contrib.auth import get_user_model
from rest_framework import serializers

from bulletin_board.buildings.models import Building
from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.core.serializers import BasicSerializer
from bulletin_board.users.api.serializers import UserSerializer

User = get_user_model()


class BuildingSerializer(BasicSerializer):
    community_id = serializers.IntegerField(write_only=True)
    community = CommunitySerializer(many=False, read_only=True)

    inhabitants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, many=True
    )
    inhabitants = UserSerializer(many=True, read_only=True)

    admins_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, many=True
    )
    admins = UserSerializer(many=True, read_only=True)

    def create(self, validated_data):
        inhabitants = []
        if "inhabitants_id" in validated_data:
            inhabitants = validated_data.pop("inhabitants_id")

        building = Building.objects.create(**validated_data)

        for user in inhabitants:
            building.inhabitants.add(user)

        return building

    class Meta:
        model = Building
        fields = [
            "id",
            "created",
            "modified",
            "uuid",
            "community_id",
            "community",
            "name",
            "type",
            "address",
            "inhabitants_id",
            "inhabitants",
            "admins_id",
            "admins",
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:building-detail", "lookup_field": "uuid"}
        }
