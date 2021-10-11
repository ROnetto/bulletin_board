from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from bulletin_board.communities.models import Community


@admin.register(Community)
class CommunityAdmin(ModelAdmin):
    list_display = ["name", "created", "modified"]
    search_fields = ["name"]
