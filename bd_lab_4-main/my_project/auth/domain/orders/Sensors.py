from __future__ import annotations
from typing import Dict, Any
from my_project import db
from datetime import datetime



class Sensor(db.Model):
    __tablename__ = "sensors"

    sensor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    installation_date = db.Column(db.Date)
    FK_sensor_type_id = db.Column(db.Integer, db.ForeignKey("sensors_type.sensor_type_id"), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Sensor':
        obj = Sensor(
            sensor_id=dto_dict.get("sensor_id"),
            installation_date=datetime.strptime(dto_dict.get("installation_date"), "%Y-%m-%d").date() if dto_dict.get("installation_date") else None,
            FK_sensor_type_id=dto_dict.get("FK_sensor_type_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "installation_date": str(self.installation_date),
            "FK_sensor_type_id": self.FK_sensor_type_id,
        }
