from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.SensorsType import SensorType

class SensorTypeDAO(GeneralDAO):
    _domain_type = SensorType

    def create(self, sensor_type: SensorType) -> None:
        self._session.add(sensor_type)
        self._session.commit()

    def find_all(self) -> List[SensorType]:
        return self._session.query(SensorType).all()

    def find_by_id(self, sensor_type_id: int) -> Optional[SensorType]:
        return self._session.query(SensorType).filter(SensorType.sensor_type_id == sensor_type_id).first()
