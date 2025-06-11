from __future__ import annotations
from typing import Dict, Any
from my_project import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'User':
        obj = User(
            user_id=dto_dict.get("user_id"),
            username=dto_dict.get("username"),
            email=dto_dict.get("email"),
            password_hash=dto_dict.get("password_hash"),
            role=dto_dict.get("role", "user")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        } 