from enum import Enum, auto


class WeatherType(Enum):
    """Met Office DataPoint weather type codes:
    https://www.metoffice.gov.uk/services/data/datapoint/code-definitions
    """

    CLEAR_NIGHT = 0
    SUNNY_DAY = auto()
    PARTLY_CLOUDY_NIGHT = auto()
    PARTLY_CLOUDY_DAY = auto()
    NOT_USED = auto()
    MIST = auto()
    FOG = auto()
    CLOUDY = auto()
    OVERCAST = auto()
    LIGHT_RAIN_SHOWER_NIGHT = auto()
    LIGHT_RAIN_SHOWER_DAY = auto()
    DRIZZLE = auto()
    LIGHT_RAIN = auto()
    HEAVY_RAIN_SHOWER_NIGHT = auto()
    HEAVY_RAIN_SHOWER_DAY = auto()
    HEAVY_RAIN = auto()
    SLEET_SHOWER_NIGHT = auto()
    SLEET_SHOWER_DAY = auto()
    SLEET = auto()
    HAIL_SHOWER_NIGHT = auto()
    HAIL_SHOWER_DAY = auto()
    HAIL = auto()
    LIGHT_SNOW_SHOWER_NIGHT = auto()
    LIGHT_SNOW_SHOWER_DAY = auto()
    LIGHT_SNOW = auto()
    HEAVY_SNOW_SHOWER_NIGHT = auto()
    HEAVY_SNOW_SHOWER_DAY = auto()
    HEAVY_SNOW = auto()
    THUNDER_SHOWER_NIGHT = auto()
    THUNDER_SHOWER_DAY = auto()
    THUNDER = auto()

    def __str__(self) -> str:
        description: str = self.name.replace("_", " ").capitalize()
        substrs_to_replace: dict = {
            " day": " (day)",
            " night": "_night",
        }
        for key, value in substrs_to_replace.items():
            if description != "Sunny day":
                description = description.replace(key, value)

        return description
