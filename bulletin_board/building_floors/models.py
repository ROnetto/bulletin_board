from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import PROTECT
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from bulletin_board.buildings.models import Building
from bulletin_board.core.models import BasicModel


class BuildingFloor(BasicModel):
    building = ForeignKey(Building, verbose_name=_("building"), on_delete=PROTECT)
    number = IntegerField(verbose_name=_("number"))

    def __str__(self):
        return f"[{self.building.name}] {self.number}"

    class Meta:
        verbose_name = _("Building floor")
        verbose_name_plural = _("Building floors")

        constraints = [
            UniqueConstraint(
                fields=["building", "number"], name="unique building floor"
            )
        ]
