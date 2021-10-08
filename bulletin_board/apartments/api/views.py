from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bulletin_board.apartments.api.serializers import ApartmentSerializer
from bulletin_board.apartments.models import Apartment


class ApartmentViewSet(ModelViewSet):
    lookup_field = "uuid"

    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

    permission_classes = [IsAuthenticated, IsAdminUser]
