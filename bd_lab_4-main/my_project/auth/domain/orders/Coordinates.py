from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Coordinate(db.Model):
    __tablename__ = "coordinates"

    coordinate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.String(45))
    longtitude = db.Column(db.Float, nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Coordinate':
        obj = Coordinate(
            coordinate_id=dto_dict.get("coordinate_id"),
            latitude=dto_dict.get("latitude"),
            longtitude=dto_dict.get("longtitude")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "coordinate_id": self.coordinate_id,
            "latitude": self.latitude,
            "longtitude": self.longtitude,
        }
