import pytest
from django.urls import resolve, reverse

from bulletin_board.news.models import BuildingNews, CommunityNews

pytestmark = pytest.mark.django_db


def test_building_news_detail(building_news: BuildingNews):
    assert (
        reverse("api:buildingnews-detail", kwargs={"uuid": building_news.uuid})
        == f"/api/building_news/{building_news.uuid}/"
    )
    assert (
        resolve(f"/api/building_news/{building_news.uuid}/").view_name
        == "api:buildingnews-detail"
    )


def test_building_news_list():
    assert reverse("api:buildingnews-list") == "/api/building_news/"
    assert resolve("/api/building_news/").view_name == "api:buildingnews-list"


def test_community_news_detail(community_news: CommunityNews):
    assert (
        reverse("api:communitynews-detail", kwargs={"uuid": community_news.uuid})
        == f"/api/community_news/{community_news.uuid}/"
    )
    assert (
        resolve(f"/api/community_news/{community_news.uuid}/").view_name
        == "api:communitynews-detail"
    )


def test_community_news_list():
    assert reverse("api:communitynews-list") == "/api/community_news/"
    assert resolve("/api/community_news/").view_name == "api:communitynews-list"
