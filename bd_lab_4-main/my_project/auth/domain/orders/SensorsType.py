from __future__ import annotations
from typing import Dict, Any
from my_project import db



class SensorType(db.Model):
    __tablename__ = "sensors_type"

    sensor_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorType':
        obj = SensorType(
            sensor_type_id=dto_dict.get("sensor_type_id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensor_type_id": self.sensor_type_id,
            "name": self.name,
            "description": self.description,
        }
