import json
from http import HTTPStatus

import pytest
import responses

from weather_uk.api_requests import (
    create_forecast_endpoint,
    create_url_from_endpoint,
    get_ip_geo_data,
    get_met_office_data,
    locations_endpoint,
    requests_adapter,
)


@pytest.fixture()
def mock_forecast_data():
    with open("tests/resources/mock_3hourly_forecast.json") as f:
        return json.load(f)


@pytest.fixture()
def mock_ipinfo_data():
    with open("tests/resources/mock_ipinfo.json") as f:
        return json.load(f)


def test_create_url_from_forecast_endpoint():
    url = create_url_from_endpoint(
        endpoint="val/wxfcs/all/json/3840?res=3hourly",
        apikey="01234567-89ab-cdef-0123-456789abcdef",
    )
    assert url == (
        "http://datapoint.metoffice.gov.uk/public/data/"
        "val/wxfcs/all/json/3840?res=3hourly"
        "&key=01234567-89ab-cdef-0123-456789abcdef"
    )


def test_create_url_from_locations_endpoint():
    url = create_url_from_endpoint(
        endpoint="val/wxfcs/all/json/sitelist",
        apikey="01234567-89ab-cdef-0123-456789abcdef",
    )
    assert url == (
        "http://datapoint.metoffice.gov.uk/public/data/"
        "val/wxfcs/all/json/sitelist"
        "?key=01234567-89ab-cdef-0123-456789abcdef"
    )


def test_create_forecast_endpoint():
    location_id = "3840"
    time_step = "3hourly"
    endpoint = create_forecast_endpoint(location_id, time_step)
    assert endpoint == "val/wxfcs/all/json/3840?res=3hourly"


def test_locations_endpoint():
    endpoint = locations_endpoint()
    assert endpoint == "val/wxfcs/all/json/sitelist"


@responses.activate
def test_get_met_office_data_using_adapter(mock_forecast_data):
    def mock_adapter(url):
        return mock_forecast_data

    endpoint = "val/wxfcs/all/json/3840?res=3hourly"
    apikey = "01234567-89ab-cdef-0123-456789abcdef"
    data = get_met_office_data(endpoint, apikey, adapter=mock_adapter)
    assert data == mock_forecast_data


@responses.activate
def test_get_ip_geo_data_using_adapter(mock_ipinfo_data):
    def mock_adapter(url):
        return mock_ipinfo_data

    data = get_ip_geo_data(adapter=mock_adapter)
    assert data == mock_ipinfo_data


@responses.activate
def test_requests_adapter(mock_forecast_data):
    url = (
        "http://datapoint.metoffice.gov.uk/public/data/"
        "val/wxfcs/all/json/3840?res=3hourly"
        "&key=01234567-89ab-cdef-0123-456789abcdef"
    )
    responses.add(
        responses.GET,
        url,
        json=mock_forecast_data,
        status=HTTPStatus.OK,
    )
    data = requests_adapter(url)
    assert data == mock_forecast_data
