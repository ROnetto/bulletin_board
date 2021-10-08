from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BulletinBoardsConfig(AppConfig):
    name = "bulletin_board.bulletin_boards"
    verbose_name = _("Bulletin boards")

    def ready(self):
        try:
            import bulletin_board.bulletin_boards.signals  # noqa F401
        except ImportError:
            pass
