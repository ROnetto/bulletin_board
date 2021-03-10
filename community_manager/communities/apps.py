from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommunitiesConfig(AppConfig):
    name = "community_manager.communities"
    verbose_name = _("Communities")

    def ready(self):
        try:
            import community_manager.communities.signals  # noqa F401
        except ImportError:
            pass
