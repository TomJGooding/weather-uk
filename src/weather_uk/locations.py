from dataclasses import dataclass


@dataclass
class UserGeolocation:
    city: str
    region: str
    country: str
    latitude: str
    longitude: str

    @classmethod
    def from_dict(cls, data: dict):
        coordinates: str = data["loc"]
        latitude, longitude = coordinates.split(",")
        return cls(
            city=data["city"],
            region=data["region"],
            country=data["country"],
            latitude=latitude,
            longitude=longitude,
        )
