from django.db.models.fields import CharField

from django.utils.translation import gettext_lazy as _

from community_manager.core.models import BasicModel


class Community(BasicModel):
    name = CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Community")
        verbose_name_plural = _("Communities")
