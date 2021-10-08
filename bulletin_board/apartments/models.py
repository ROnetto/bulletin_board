from django.contrib.auth import get_user_model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.translation import gettext_lazy as _

from bulletin_board.building_floors.models import BuildingFloor
from bulletin_board.core.models import BasicModel

User = get_user_model()


class Apartment(BasicModel):
    building_floor = ForeignKey(
        BuildingFloor, verbose_name=_("building floor"), on_delete=PROTECT
    )
    number = CharField(verbose_name=_("number"), max_length=255)

    inhabitants = ManyToManyField(User, verbose_name=_("inhabitants"))

    def __str__(self):
        return f"[{self.building_floor.name}] {self.number}"

    class Meta:
        verbose_name = _("Apartment")
        verbose_name_plural = _("Apartments")
