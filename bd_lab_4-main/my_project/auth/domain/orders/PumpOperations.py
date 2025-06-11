from __future__ import annotations
from typing import Dict, Any
from my_project import db


class PumpOperation(db.Model):
    __tablename__ = "pumpOperations"  # fixed typo

    pumpOperation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # fixed typo
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    water_pumped = db.Column(db.Float)
    pumps_pump_id = db.Column(db.Integer, db.ForeignKey("pumps.pump_id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "pumpOperation_id": self.pumpOperation_id,  # fixed typo
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "water_pumped": self.water_pumped,
            "pumps_pump_id": self.pumps_pump_id,
        }
