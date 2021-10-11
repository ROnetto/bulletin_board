from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsConfig(AppConfig):
    name = "bulletin_board.news"
    verbose_name = _("News")

    def ready(self):
        try:
            import bulletin_board.news.signals  # noqa F401
        except ImportError:
            pass
