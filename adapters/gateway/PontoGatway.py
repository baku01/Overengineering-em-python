from abc import ABC, abstractmethod
from typing import List
from core.entity import Ponto

class PontoGateway(ABC):
    @abstractmethod
    def procurar_inconsistencias(self, ponto: Ponto) -> List[dict]:
        pass
