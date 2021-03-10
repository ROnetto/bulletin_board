from django.contrib.auth import get_user_model
from rest_framework import serializers

from community_manager.building_floors.models import BuildingFloor
from community_manager.buildings.api.serializers import BuildingSerializer
from community_manager.core.serializers import BasicSerializer

User = get_user_model()


class BuildingFloorSerializer(BasicSerializer):
    building_id = serializers.IntegerField(write_only=True)
    building = BuildingSerializer(many=False, read_only=True)

    class Meta:
        model = BuildingFloor
        fields = ["id", "created", "modified", "building_id", "building", "name"]
