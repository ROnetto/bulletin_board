import pytest
from django.urls import resolve, reverse

from community_manager.communities.models import Community

pytestmark = pytest.mark.django_db


def test_community_detail(community: Community):
    assert (
        reverse("api:community-detail", kwargs={"username": community.id})
        == f"/api/communities/{community.id}/"
    )
    assert resolve(f"/api/communities/{community.id}/").view_name == "api:community-detail"


def test_community_list():
    assert reverse("api:community-list") == "/api/communities/"
    assert resolve("/api/communities/").view_name == "api:community-list"
