import json

import pytest

from weather_uk.locations import (
    MetOfficeLocation,
    UserGeolocation,
    find_nearest_met_office_location,
    haversine,
)


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
    locations_list = mock_met_office_locations_data["Locations"]["Location"]
    test_location = locations_list[0]
    location = MetOfficeLocation.from_dict(test_location)

    assert location.id == "14"
    assert location.name == "Carlisle Airport"
    assert location.region == "nw"
    assert location.latitude == 54.9375
    assert location.longitude == -2.8092


def test_find_nearest_met_office_location(mock_met_office_locations_data):
    # London co-ordinates
    lat = 51.5085
    long = -0.1257

    nearest_met_office_location = find_nearest_met_office_location(
        lat, long, mock_met_office_locations_data
    )

    assert nearest_met_office_location.id == "352409"
    assert nearest_met_office_location.name == "London"
    assert nearest_met_office_location.region == "se"
    assert nearest_met_office_location.latitude == 51.5081
    assert nearest_met_office_location.longitude == -0.1248
