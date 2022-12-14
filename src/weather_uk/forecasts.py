from dataclasses import dataclass
from datetime import date

from prettytable import PrettyTable

from weather_uk.weather_type import WeatherType


@dataclass
class ForecastWeatherData:
    mins_after_midnight: int
    weather_type: WeatherType
    temp_c: float
    temp_feels_like_c: float
    precip_prob_pct: float
    wind_speed_mph: float
    wind_gust_mph: float
    wind_direction: str
    uv_idx: int
    humidity_pct: float
    visibility: str

    @classmethod
    def from_dict(cls, data: dict):
        weather_type_code = int(data["W"])
        weather_type = WeatherType(weather_type_code)
        return cls(
            mins_after_midnight=int(data["$"]),
            weather_type=weather_type,
            temp_c=float(data["T"]),
            temp_feels_like_c=float(data["F"]),
            precip_prob_pct=float(data["Pp"]),
            wind_speed_mph=float(data["S"]),
            wind_gust_mph=float(data["G"]),
            wind_direction=data["D"],
            uv_idx=int(data["U"]),
            humidity_pct=float(data["H"]),
            visibility=data["V"],
        )


@dataclass
class ForecastSingleDate:
    date: date
    forecast: list[ForecastWeatherData]

    @classmethod
    def from_dict(cls, data: dict):
        date_string = data["value"][:-1]
        return cls(
            date=date.fromisoformat(date_string),
            forecast=[
                ForecastWeatherData.from_dict(weather_data)
                for weather_data in data["Rep"]
            ],
        )


def forecast_table(forecast: ForecastSingleDate) -> str:
    table = PrettyTable()
    for weather in forecast.forecast:
        hours, minutes = divmod(weather.mins_after_midnight, 60)
        time = f"{hours:02d}:{minutes:02d}"
        weather_type = weather.weather_type
        temp = f"{int(weather.temp_c)}({int(weather.temp_feels_like_c)}) °C"
        precip_prob = f"{int(weather.precip_prob_pct)}%"
        wind = f"{int(weather.wind_speed_mph)} mph"

        table.add_column(
            fieldname=time,
            column=[weather_type, temp, precip_prob, wind],
        )

    return table.get_string()
