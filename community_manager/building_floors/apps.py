from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BuildingFloorsConfig(AppConfig):
    name = "community_manager.building_floors"
    verbose_name = _("Building floors")

    def ready(self):
        try:
            import community_manager.building_floors.signals  # noqa F401
        except ImportError:
            pass
