import json

import pytest

from weather_uk.forecasts import ForecastSingleDate, ForecastWeatherData, forecast_table


@pytest.fixture()
def mock_forecast_data():
    with open("tests/resources/mock_3hourly_forecast.json") as f:
        return json.load(f)


def test_forecast_weather_data(mock_forecast_data):
    weather_location = mock_forecast_data["SiteRep"]["DV"]["Location"]
    weather_periods = weather_location["Period"]
    weather_data = weather_periods[0]["Rep"][0]
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


def test_forecast_single_date(mock_forecast_data):
    forecast_location = mock_forecast_data["SiteRep"]["DV"]["Location"]
    forecast_periods = forecast_location["Period"]
    forecast_day = forecast_periods[0]

    forecast_single_date = ForecastSingleDate.from_dict(forecast_day)

    assert str(forecast_single_date.date) == "2022-11-05"
    assert len(forecast_single_date.forecast) == 6


def test_forecast_table(mock_forecast_data):
    forecast_location = mock_forecast_data["SiteRep"]["DV"]["Location"]
    forecast_periods = forecast_location["Period"]
    forecast_day = forecast_periods[0]

    forecast = ForecastSingleDate.from_dict(forecast_day)
    table = forecast_table(forecast)

    assert table.count("+") == 21
    assert table.count("%") == 6
    assert "06:00" in table
    assert "09:00" in table
    assert "Heavy rain" in table
    assert "9(7) °C" in table
    assert "9 mph" in table
    assert "97%" in table
