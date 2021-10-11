from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bulletin_board.buildings.models import Building


@admin.register(Building)
class BuildingAdmin(ModelAdmin):
    list_display = ["community", "name", "created", "modified"]
    search_fields = ["name"]
