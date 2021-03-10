from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApartmentsConfig(AppConfig):
    name = "community_manager.apartments"
    verbose_name = _("Apartments")

    def ready(self):
        try:
            import community_manager.apartment.signals  # noqa F401
        except ImportError:
            pass
