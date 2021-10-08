from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BuildingsConfig(AppConfig):
    name = "bulletin_board.buildings"
    verbose_name = _("Buildings")

    def ready(self):
        try:
            import bulletin_board.buildings.signals  # noqa F401
        except ImportError:
            pass
