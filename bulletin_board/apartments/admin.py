from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bulletin_board.apartments.models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(ModelAdmin):
    list_display = ["building_floor", "number", "created", "modified"]
    search_fields = ["number"]
