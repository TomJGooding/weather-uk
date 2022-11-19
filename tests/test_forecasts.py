import json

import pytest

from weather_uk.forecasts import ForecastWeatherData


@pytest.fixture()
def mock_forecast_data():
    with open("tests/resources/mock_3hourly_forecast.json") as f:
        return json.load(f)


def test_forecast_weather_data(mock_forecast_data):
    weather_location = mock_forecast_data["SiteRep"]["DV"]["Location"]
    weather_period = weather_location["Period"]
    weather_data = weather_period[0]["Rep"][0]
    weather = ForecastWeatherData.from_dict(weather_data)

    assert weather.mins_after_midnight == 360
    assert str(weather.weather_type) == "Heavy rain"
    assert weather.temp_c == 9
    assert weather.temp_feels_like_c == 7
    assert weather.precip_prob_pct == 97
    assert weather.wind_speed_mph == 9
    assert weather.wind_gust_mph == 11
    assert weather.wind_direction == "S"
    assert weather.uv_idx == 0
    assert weather.humidity_pct == 100
    assert weather.visibility == "MO"
