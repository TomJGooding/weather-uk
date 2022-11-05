import json

import pytest

from weather_uk.locations import UserGeolocation, haversine


@pytest.fixture()
def mock_ipinfo_data():
    with open("tests/resources/mock_ipinfo.json") as f:
        return json.load(f)


def test_user_geolocation_class(mock_ipinfo_data):
    user_geolocation = UserGeolocation.from_dict(mock_ipinfo_data)
    assert user_geolocation.city == "London"
    assert user_geolocation.region == "England"
    assert user_geolocation.country == "GB"
    assert user_geolocation.latitude == 51.5085
    assert user_geolocation.longitude == -0.1257


def test_haversine():
    """Test based on the distance between Lyon and Paris
    example provided by https://github.com/mapado/haversine"""
    lat1 = 45.7597
    long1 = 4.8422
    lat2 = 48.8567
    long2 = 2.3508

    distance = haversine(lat1, long1, lat2, long2)
    assert distance == 392.2172595594006
