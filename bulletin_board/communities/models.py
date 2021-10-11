from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _

from bulletin_board.core.models import BasicModel

User = get_user_model()


class Community(BasicModel):
    name = CharField(verbose_name=_("name"), max_length=255)

    admins = ManyToManyField(User, verbose_name=_("admins"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Community")
        verbose_name_plural = _("Communities")
