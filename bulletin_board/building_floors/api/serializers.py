from rest_framework import serializers

from bulletin_board.building_floors.models import BuildingFloor
from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.buildings.models import Building
from bulletin_board.core.serializers import BasicSerializer


class BuildingFloorSerializer(BasicSerializer):
    building_id = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all(), write_only=True
    )
    building = BuildingSerializer(many=False, read_only=True)

    class Meta:
        model = BuildingFloor
        fields = [
            "id",
            "created",
            "modified",
            "uuid",
            "building_id",
            "building",
            "number",
        ]
