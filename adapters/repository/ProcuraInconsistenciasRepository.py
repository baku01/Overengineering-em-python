from adapters.impl.ProcuraInconsistenicas import PontoGatewayImpl
import pandas as pd

# Leitura dos dados do arquivo CSV
planilha1 = pd.read_csv('pontos1.csv')

# Criação da instância do PontoGateway
ponto_gateway_impl = PontoGatewayImpl()

# Exemplo de uso do método procurar_inconsistencias
inconsistencias = ponto_gateway_impl.procurar_inconsistencias(planilha1)

# Faça algo com as inconsistências encontradas
print(inconsistencias)
