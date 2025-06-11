from __future__ import annotations
from typing import Dict, Any
from my_project import db

class Pump(db.Model):
    __tablename__ = "pumps"

    pump_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Float)
    FK_locations_id = db.Column(db.Integer, db.ForeignKey("locations.locations_id"), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Pump':
        obj = Pump(
            pump_id=dto_dict.get("pump_id"),
            capacity=dto_dict.get("capacity"),
            FK_locations_id=dto_dict.get("FK_locations_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "pump_id": self.pump_id,
            "capacity": self.capacity,
            "FK_locations_id": self.FK_locations_id,
        }
