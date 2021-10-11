from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from bulletin_board.apartments.api.views import ApartmentViewSet
from bulletin_board.building_floors.api.views import BuildingFloorViewSet
from bulletin_board.buildings.api.views import BuildingViewSet
from bulletin_board.communities.api.views import CommunityViewSet
from bulletin_board.news.api.views import BuildingNewsViewSet, CommunityNewsViewSet
from bulletin_board.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("apartments", ApartmentViewSet)
router.register("building_floors", BuildingFloorViewSet)
router.register("buildings", BuildingViewSet)
router.register("communities", CommunityViewSet)
router.register("building_news", BuildingNewsViewSet)
router.register("community_news", CommunityNewsViewSet)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
