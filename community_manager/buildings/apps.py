from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BuildingsConfig(AppConfig):
    name = "community_manager.buildings"
    verbose_name = _("Buildings")

    def ready(self):
        try:
            import community_manager.buildings.signals  # noqa F401
        except ImportError:
            pass
