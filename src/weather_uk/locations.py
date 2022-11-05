from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

AVG_EARTH_RADIUS_KM = 6371.0088  # https://en.wikipedia.org/wiki/Earth_radius


@dataclass
class UserGeolocation:
    city: str
    region: str
    country: str
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, data: dict):
        coordinates: str = data["loc"]
        latitude, longitude = [float(x) for x in coordinates.split(",")]
        return cls(
            city=data["city"],
            region=data["region"],
            country=data["country"],
            latitude=latitude,
            longitude=longitude,
        )


def haversine(lat1: float, long1: float, lat2: float, long2: float) -> float:
    """The haversine formula calculates the great-circle distance
    between two points on the Earth surface
    """
    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # calculate haversine
    dlat = lat2 - lat1
    dlong = long2 - long1
    d = sin(dlat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(dlong * 0.5) ** 2
    c = 2 * asin(sqrt(d))

    return AVG_EARTH_RADIUS_KM * c
