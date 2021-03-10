from django.contrib.auth import get_user_model

from community_manager.core.serializers import BasicSerializer

User = get_user_model()


class UserSerializer(BasicSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
