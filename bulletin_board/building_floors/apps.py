from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BuildingFloorsConfig(AppConfig):
    name = "bulletin_board.building_floors"
    verbose_name = _("Building floors")

    def ready(self):
        try:
            import bulletin_board.building_floors.signals  # noqa F401
        except ImportError:
            pass
