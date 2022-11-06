import json

import pytest

from weather_uk.locations import MetOfficeLocation, UserGeolocation, haversine


@pytest.fixture()
def mock_ipinfo_data():
    with open("tests/resources/mock_ipinfo.json") as f:
        return json.load(f)


@pytest.fixture
def mock_met_office_locations_data():
    with open("tests/resources/mock_sitelist.json") as f:
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


def test_met_office_location_class(mock_met_office_locations_data):
    all_locations = mock_met_office_locations_data["Locations"]
    location_data = all_locations["Location"][0]
    location = MetOfficeLocation.from_dict(location_data)

    assert location.id == "14"
    assert location.name == "Carlisle Airport"
    assert location.region == "nw"
    assert location.latitude == 54.9375
    assert location.longitude == -2.8092
