from __future__ import annotations
from typing import Dict, Any
from my_project import db
from datetime import datetime


class SensorReading(db.Model):
    __tablename__ = "SensorReadings"

    SensorReading_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float)
    unit = db.Column(db.String(45))
    sensors_sensor_id = db.Column(db.Integer)
    sensors_FK_sensor_type_id = db.Column(db.Integer)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorReading':
        obj = SensorReading(
            SensorReading_id=dto_dict.get("SensorReading_id"),
            timestamp=datetime.fromisoformat(dto_dict.get("timestamp")) if dto_dict.get("timestamp") else None,
            value=dto_dict.get("value"),
            unit=dto_dict.get("unit"),
            sensors_sensor_id=dto_dict.get("sensors_sensor_id"),
            sensors_FK_sensor_type_id=dto_dict.get("sensors_FK_sensor_type_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "SensorReading_id": self.SensorReading_id,
            "timestamp": self.timestamp.isoformat(),
            "value": self.value,
            "unit": self.unit,
            "sensors_sensor_id": self.sensors_sensor_id,
            "sensors_FK_sensor_type_id": self.sensors_FK_sensor_type_id,
        }
