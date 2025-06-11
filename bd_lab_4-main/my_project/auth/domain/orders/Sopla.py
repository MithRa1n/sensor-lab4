from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Sopla(db.Model):
    __tablename__ = "sopla"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    max_water_dlow = db.Column(db.Float)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    coordinate_id = db.Column(db.Integer, db.ForeignKey("coordinates.id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "max_water_dlow": self.max_water_dlow,
            "location_id": self.location_id,
            "coordinate_id": self.coordinate_id,
        }
