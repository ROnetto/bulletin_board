from rest_framework import serializers

from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.bulletin_boards.models import (
    BuildingBulletinBoard,
    CommunityBulletinBoard,
)
from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.core.serializers import BasicSerializer


class CommunityBulletinBoardSerializer(BasicSerializer):
    community_id = serializers.IntegerField(write_only=True)
    community = CommunitySerializer(read_only=True)

    class Meta:
        model = CommunityBulletinBoard
        fields = [
            "id",
            "created",
            "modified",
            "uuid",
            "community_id",
            "community",
            "title",
            "text",
            "expiration_date",
        ]


class BuildingBulletinBoardSerializer(BasicSerializer):
    building_id = serializers.IntegerField(write_only=True)
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = BuildingBulletinBoard
        fields = [
            "id",
            "created",
            "modified",
            "uuid",
            "building_id",
            "building",
            "title",
            "text",
            "expiration_date",
        ]
