from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from community_manager.apartments.api.serializers import ApartmentSerializer
from community_manager.apartments.models import Apartment

User = get_user_model()


class ApartmentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
