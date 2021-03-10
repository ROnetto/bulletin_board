from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

from django.utils.translation import gettext_lazy as _

from community_manager.communities.models import Community
from community_manager.core.models import BasicModel


class Building(BasicModel):
    community = ForeignKey(Community, verbose_name=_("community"), on_delete=PROTECT)
    name = CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return f"[{self.community.name}] {self.name}"

    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")
