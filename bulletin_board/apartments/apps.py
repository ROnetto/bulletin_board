from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApartmentsConfig(AppConfig):
    name = "bulletin_board.apartments"
    verbose_name = _("Apartments")

    def ready(self):
        try:
            import bulletin_board.apartment.signals  # noqa F401
        except ImportError:
            pass
