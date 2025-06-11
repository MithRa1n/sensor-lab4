from __future__ import annotations
from typing import Dict, Any
from my_project import db

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    locations_locations_id = db.Column(db.Integer, db.ForeignKey("locations.locations_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "locations_locations_id": self.locations_locations_id,
        }
