from dataclasses import dataclass

from weather_uk.weather_type import WeatherType


@dataclass
class ForecastWeatherData:
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
