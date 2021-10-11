from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bulletin_board.news.models import BuildingNews, CommunityNews


@admin.register(BuildingNews)
class BuildingNewsAdmin(ModelAdmin):
    list_display = ["building", "title", "expiration_date", "created", "modified"]
    search_fields = ["title"]


@admin.register(CommunityNews)
class CommunityNewsAdmin(ModelAdmin):
    list_display = ["community", "title", "expiration_date", "created", "modified"]
    search_fields = ["title"]
