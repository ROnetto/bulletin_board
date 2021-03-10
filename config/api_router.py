from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from community_manager.communities.api.views import CommunityViewSet
from community_manager.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("communities", CommunityViewSet)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
