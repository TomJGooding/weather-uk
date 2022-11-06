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


@dataclass
class MetOfficeLocation:
    id: str
    name: str
    region: str
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            region=data["region"],
            latitude=float(data["latitude"]),
            longitude=float(data["longitude"]),
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


def find_nearest_met_office_location(
    lat: float,
    long: float,
    locations_data: dict,
):
    locations_list: list[dict] = locations_data["Locations"]["Location"]

    nearest_distance: float = 9999  # initialised as impossibly large distance
    nearest_location_data: dict = {}
    for location in locations_list:
        location_lat = float(location["latitude"])
        location_long = float(location["longitude"])
        distance = haversine(
            lat,
            long,
            location_lat,
            location_long,
        )
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_location_data = location

    return MetOfficeLocation.from_dict(nearest_location_data)
