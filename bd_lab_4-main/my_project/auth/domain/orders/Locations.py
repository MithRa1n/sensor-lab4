from __future__ import annotations
from typing import Dict, Any
from my_project import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(45))
    street = db.Column(db.String(45))
    street_num = db.Column(db.Integer)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "country": self.country,
            "street": self.street,
            "street_num": self.street_num,
        }
