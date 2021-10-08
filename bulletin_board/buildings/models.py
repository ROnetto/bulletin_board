from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.translation import gettext_lazy as _

from bulletin_board.communities.models import Community
from bulletin_board.core.models import BasicModel
from bulletin_board.users.models import User


class Building(BasicModel):
    TYPE_HOUSE = 0
    TYPE_APARTMENT_BUILDING = 1

    TYPE_CHOICES = (
        (TYPE_HOUSE, _("House")),
        (TYPE_APARTMENT_BUILDING, _("Apartment building")),
    )

    community = ForeignKey(Community, verbose_name=_("community"), on_delete=PROTECT)
    name = CharField(verbose_name=_("name"), max_length=255)
    address = CharField(verbose_name=_("address"), max_length=255)
    type = IntegerField(choices=TYPE_CHOICES)

    inhabitants = ManyToManyField(User, verbose_name=_("inhabitants"))

    def __str__(self):
        return f"[{self.community.name}] {self.get_type_display()} | {self.address} | {self.name}"

    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")
