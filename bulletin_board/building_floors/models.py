from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from bulletin_board.buildings.models import Building
from bulletin_board.core.models import BasicModel


class BuildingFloor(BasicModel):
    building = ForeignKey(Building, verbose_name=_("building"), on_delete=PROTECT)
    name = CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return f"[{self.building.name}] {self.name}"

    class Meta:
        verbose_name = _("Building floor")
        verbose_name_plural = _("Building floors")
