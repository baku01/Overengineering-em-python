
# Experimento em Overengineering: Verificador Genérico de Pontos 🧪

Este repositório representa um experimento em overengineering, onde foi criado um verificador genérico de pontos seguindo os princípios da Clean Architecture em Python. O termo "overengineering" refere-se à prática de fornecer soluções mais complexas ou elaboradas do que as necessárias para resolver um problema específico.

O código aqui presente é uma exploração intencional de implementações e estruturas complexas, buscando compreender até que ponto a aplicação dos princípios da Clean Architecture pode levar a uma arquitetura robusta e modular.

Este experimento não apenas visa criar um verificador de inconsistências nos pontos de atendimento, mas também serve como uma plataforma de aprendizado para:

- Compreender os princípios da Clean Architecture.
- Explorar a implementação de padrões em Python.
- Analisar a organização modular do código.

Sinta-se à vontade para examinar o código, fazer alterações e experimentar. Este projeto está aberto a contribuições e é um espaço para aprender e discutir sobre diferentes abordagens arquiteturais.

## Compreendendo o Funcionamento do Código:

### 1. Interface `PontoGateway`:

A interface `PontoGateway` define o contrato para procurar inconsistências nos pontos:

```python
# PontoGateway interface no pacote gateway
from abc import ABC, abstractmethod
from typing import List
from core.entity import Ponto

class PontoGateway(ABC):
    @abstractmethod
    def procurar_inconsistencias(self, ponto: Ponto) -> List[dict]:
        pass
```

### 2. Implementação `PontoGatewayImpl`:

A classe `PontoGatewayImpl` implementa a interface `PontoGateway`:

```python
# Implementação da interface no subpacote adapters.impl
from typing import List
from adapters.gateway.PontoGateway import PontoGateway
from core.entity import Ponto

class PontoGatewayImpl(PontoGateway):
    def procurar_inconsistencias(self, ponto: Ponto) -> List[dict]:
        # Implementação da lógica para procurar inconsistências
        # Use o objeto Ponto conforme necessário
        pass
```

O método `procurar_inconsistencias` nesta implementação deveria conter a lógica para procurar inconsistências nos pontos.

### 3. Entidade `Ponto`:

A entidade `Ponto` representa os pontos de um funcionário:

```python
# Definição da entidade no pacote core
class Ponto:
    def __init__(self, nome, entrada_manha, saida_manha, entrada_tarde, saida_tarde):
        self.nome = nome
        self.entrada_manha = entrada_manha
        self.saida_manha = saida_manha
        self.entrada_tarde = entrada_tarde
        self.saida_tarde = saida_tarde
```

### Overengineering:

O título "Experimento em Overengineering" sugere uma abordagem deliberadamente complexa para o problema em questão. Embora a Clean Architecture promova uma estrutura modular e de fácil manutenção, em alguns casos, um monólito pode ser mais eficaz para problemas simples ou de escala limitada.

A aplicação dos princípios de Clean Architecture é valiosa, mas é crucial equilibrar a complexidade da arquitetura com a real necessidade do projeto. Em muitos casos, um monólito pode ser mais simples e eficiente, evitando a sobrecarga associada a uma arquitetura mais complexa.

Este experimento serve como uma oportunidade de aprendizado para explorar diferentes abordagens arquiteturais e entender quando aplicar ou não os princípios de uma determinada arquitetura. A melhor escolha dependerá sempre do contexto específico do projeto e dos requisitos.
