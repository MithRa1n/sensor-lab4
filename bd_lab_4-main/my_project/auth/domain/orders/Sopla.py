from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Sopla(db.Model):
    __tablename__ = "sopla"

    sopla_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    max_water_dlow = db.Column(db.Float)
    FK_locations_id = db.Column(db.Integer, db.ForeignKey("locations.locations_id"), nullable=False)
    FK_coordinate_id = db.Column(db.Integer, db.ForeignKey("coordinates.coordinate_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sopla_id": self.sopla_id,
            "max_water_dlow": self.max_water_dlow,
            "FK_locations_id": self.FK_locations_id,
            "FK_coordinate_id": self.FK_coordinate_id,
        }
