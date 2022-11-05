import json

import pytest

from weather_uk.locations import UserGeolocation


@pytest.fixture()
def mock_ipinfo_data():
    with open("tests/resources/mock_ipinfo.json") as f:
        return json.load(f)


def test_user_geolocation_class(mock_ipinfo_data):
    user_geolocation = UserGeolocation.from_dict(mock_ipinfo_data)
    assert user_geolocation.city == "London"
    assert user_geolocation.region == "England"
    assert user_geolocation.country == "GB"
    assert user_geolocation.latitude == "51.5085"
    assert user_geolocation.longitude == "-0.1257"
