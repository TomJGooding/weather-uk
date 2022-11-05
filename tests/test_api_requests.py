import json
from http import HTTPStatus

import pytest
import responses

from weather_uk.api_requests import (
    create_forecast_endpoint,
    create_url_from_endpoint,
    get_data,
    requests_adapter,
)


@pytest.fixture()
def mock_forecast_data():
    with open("tests/resources/mock_forecast.json") as f:
        return json.load(f)


def test_create_url_from_endpoint():
    url = create_url_from_endpoint(
        endpoint="val/wxfcs/all/json/3840?res=3hourly",
        apikey="01234567-89ab-cdef-0123-456789abcdef",
    )
    assert url == (
        "http://datapoint.metoffice.gov.uk/public/data/"
        "val/wxfcs/all/json/3840?res=3hourly"
        "&key=01234567-89ab-cdef-0123-456789abcdef"
    )


def test_create_forecast_endpoint():
    location_id = "3840"
    time_step = "3hourly"
    endpoint = create_forecast_endpoint(location_id, time_step)
    assert endpoint == "val/wxfcs/all/json/3840?res=3hourly"


@responses.activate
def test_get_data_using_adapter(mock_forecast_data):
    def mock_adapter(url):
        return mock_forecast_data

    endpoint = "val/wxfcs/all/json/3840?res=3hourly"
    apikey = "01234567-89ab-cdef-0123-456789abcdef"
    data = get_data(endpoint, apikey, adapter=mock_adapter)
    assert data == mock_forecast_data


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
