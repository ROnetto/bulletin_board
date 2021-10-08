from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateField, TextField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from bulletin_board.communities.models import Community
from bulletin_board.core.models import BasicModel


class CommunityBulletinBoard(BasicModel):
    community = ForeignKey(Community, verbose_name=_("community"), on_delete=PROTECT)

    title = CharField(verbose_name=_("name"), max_length=255)
    text = TextField()

    expiration_date = DateField()

    def __str__(self):
        return f"[{self.community.name}] {self.title}"

    class Meta:
        verbose_name = _("Community bulletin board")
        verbose_name_plural = _("Community bulletin boards")


class BuildingBulletinBoard(BasicModel):
    building = ForeignKey(Community, verbose_name=_("building"), on_delete=PROTECT)

    title = CharField(verbose_name=_("name"), max_length=255)
    text = TextField()

    expiration_date = DateField()

    def __str__(self):
        return f"[{self.building.name}] {self.title}"

    class Meta:
        verbose_name = _("Building bulletin board")
        verbose_name_plural = _("Building bulletin boards")
