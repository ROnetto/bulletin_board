from rest_framework import serializers

from bulletin_board.building_floors.models import BuildingFloor
from bulletin_board.buildings.api.serializers import BuildingSerializer
from bulletin_board.core.serializers import BasicSerializer


class BuildingFloorSerializer(BasicSerializer):
    building_id = serializers.IntegerField(write_only=True)
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
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:buildingfloor-detail", "lookup_field": "uuid"}
        }
