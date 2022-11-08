from weather_uk.weather_type import WeatherType


def test_weather_type_sunny_day():
    weather_type_code = 1
    weather_type = WeatherType(weather_type_code)
    assert str(weather_type) == "Sunny day"


def test_weather_type_thunder_day():
    weather_type_code = 29
    weather_type = WeatherType(weather_type_code)
    assert str(weather_type) == "Thunder shower (day)"
