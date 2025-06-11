from dataclasses import dataclass
from typing import Optional

@dataclass
class SensorCoordinates:
    sensors_coordinates_id: int
    sensor_id: int
    coordinates_id: int

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorCoordinates':
        obj = SensorCoordinates(
            sensors_coordinates_id=dto_dict.get("sensors_coordinates_id"),
            sensor_id=dto_dict.get("sensor_id"),
            coordinates_id=dto_dict.get("coordinates_id")
        )
        return obj

    def put_into_dto(self) -> dict:
        return {
            "sensors_coordinates_id": self.sensors_coordinates_id,
            "sensor_id": self.sensor_id,
            "coordinates_id": self.coordinates_id
        } 