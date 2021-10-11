from rest_framework import serializers

from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.core.serializers import BasicSerializer
from bulletin_board.news.models import BuildingNews, CommunityNews


class CommunityNewsSerializer(BasicSerializer):
    community_id = serializers.IntegerField(write_only=True)
    community = CommunitySerializer(read_only=True)

    class Meta:
        model = CommunityNews
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


class BuildingNewsSerializer(BasicSerializer):
    building_id = serializers.IntegerField(write_only=True)
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = BuildingNews
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
