import uuid

from django.db.models.fields import UUIDField
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BasicModel(TimeStampedModel, SoftDeletableModel):
    uuid = UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
