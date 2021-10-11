from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bulletin_board.building_floors.models import BuildingFloor


@admin.register(BuildingFloor)
class BuildingFloorAdmin(ModelAdmin):
    list_display = ["building", "number", "created", "modified"]
    search_fields = ["number"]
