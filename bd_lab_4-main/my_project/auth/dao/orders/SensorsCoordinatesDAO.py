from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.SensorsHasCoordinates import SensorCoordinate

class SensorsCoordinatesDAO(GeneralDAO):
    _domain_type = SensorCoordinate

    def create(self, sensor_coordinate: SensorCoordinate) -> None:
        self._session.add(sensor_coordinate)
        self._session.commit()

    def find_all(self) -> List[SensorCoordinate]:
        return self._session.query(SensorCoordinate).all()

    def find_by_id(self, sensor_coordinate_id: int) -> Optional[SensorCoordinate]:
        return self._session.query(SensorCoordinate).filter(SensorCoordinate.sensors_sensor_id == sensor_coordinate_id).first()

    def find_by_sensor_id(self, sensor_id: int) -> List[SensorCoordinate]:
        return self._session.query(SensorCoordinate).filter(SensorCoordinate.sensors_sensor_id == sensor_id).all() 