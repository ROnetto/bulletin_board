from django.contrib.auth import get_user_model
from rest_framework import serializers

from bulletin_board.apartments.models import Apartment
from bulletin_board.communities.api.serializers import CommunitySerializer
from bulletin_board.core.serializers import BasicSerializer
from bulletin_board.users.api.serializers import UserSerializer

User = get_user_model()


class ApartmentSerializer(BasicSerializer):
    building_floor_id = serializers.IntegerField(write_only=True)
    building_floor = CommunitySerializer(many=False, read_only=True)

    inhabitants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, many=True
    )
    inhabitants = UserSerializer(many=True, read_only=True)

    def create(self, validated_data):
        inhabitants = validated_data.pop("inhabitants_id")
        apartment = Apartment.objects.create(**validated_data)
        for user in inhabitants:
            apartment.inhabitants.add(user)
        return apartment

    class Meta:
        model = Apartment
        fields = [
            "id",
            "created",
            "modified",
            "building_floor_id",
            "building_floor",
            "number",
            "inhabitants_id",
            "inhabitants",
        ]
