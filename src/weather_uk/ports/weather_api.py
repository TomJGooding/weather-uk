from abc import ABC, abstractmethod

from weather_uk.forecasts.models import ForecastDay
from weather_uk.locations.model import Location


class AbstractWeatherApi(ABC):
    @abstractmethod
    def check_authentication(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_locations_list(self) -> list[Location]:
        raise NotImplementedError

    @abstractmethod
    def get_forecast(self, location_id: int) -> list[ForecastDay]:
        raise NotImplementedError
