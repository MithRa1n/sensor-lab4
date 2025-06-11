from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.SensorsCoordinates import SensorCoordinates
from my_project.auth.service.orders.SensorsCoordinatesService import SensorsCoordinatesService

sensorscoordinates_service = SensorsCoordinatesService()
sensors_coordinates_bp = Blueprint('sensorscoordinates', __name__, url_prefix='/sensorscoordinates')

@sensors_coordinates_bp.get('')
def get_all_sensorscoordinates() -> Response:
    sensorscoordinates = sensorscoordinates_service.find_all()
    sensorscoordinates_dto = [sc.put_into_dto() for sc in sensorscoordinates]
    return make_response(jsonify(sensorscoordinates_dto), HTTPStatus.OK)

@sensors_coordinates_bp.post('')
def create_sensorscoordinates() -> Response:
    content = request.get_json()
    sensorscoordinates = SensorCoordinates.create_from_dto(content)
    sensorscoordinates_service.create(sensorscoordinates)
    return make_response(jsonify(sensorscoordinates.put_into_dto()), HTTPStatus.CREATED)

@sensors_coordinates_bp.get('/<int:sensors_coordinates_id>')
def get_sensorscoordinates(sensors_coordinates_id: int) -> Response:
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensors_coordinates_id)
    if sensorscoordinates:
        return make_response(jsonify(sensorscoordinates.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

@sensors_coordinates_bp.put('/<int:sensors_coordinates_id>')
def update_sensorscoordinates(sensors_coordinates_id: int) -> Response:
    content = request.get_json()
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensors_coordinates_id)
    if not sensorscoordinates:
        return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

    updated_sensorscoordinates = SensorCoordinates.create_from_dto(content)
    updated_sensorscoordinates.sensors_coordinates_id = sensors_coordinates_id
    sensorscoordinates_service.update(updated_sensorscoordinates)
    return make_response(jsonify(updated_sensorscoordinates.put_into_dto()), HTTPStatus.OK)

@sensors_coordinates_bp.delete('/<int:sensors_coordinates_id>')
def delete_sensorscoordinates(sensors_coordinates_id: int) -> Response:
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensors_coordinates_id)
    if not sensorscoordinates:
        return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

    sensorscoordinates_service.delete(sensors_coordinates_id)
    return make_response(jsonify({"message": "SensorsCoordinates deleted successfully"}), HTTPStatus.NO_CONTENT)
