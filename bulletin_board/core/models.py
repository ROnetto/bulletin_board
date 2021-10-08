import uuid

from django.db.models.fields import UUIDField
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BasicUserModel(TimeStampedModel):
    uuid = UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class BasicModel(TimeStampedModel, SoftDeletableModel):
    uuid = UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
