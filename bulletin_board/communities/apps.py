from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommunitiesConfig(AppConfig):
    name = "bulletin_board.communities"
    verbose_name = _("Communities")

    def ready(self):
        try:
            import bulletin_board.communities.signals  # noqa F401
        except ImportError:
            pass
