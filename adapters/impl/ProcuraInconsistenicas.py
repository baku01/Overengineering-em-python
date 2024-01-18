from typing import List

from adapters.gateway.PontoGatway import PontoGateway
from core.entity import Ponto

class PontoGatewayImpl(PontoGateway):
    def procurar_inconsistencias(self, ponto: Ponto) -> List[dict]:
        # Implemente a lógica para procurar inconsistências aqui
        # Use o objeto Ponto conforme necessário
        pass
