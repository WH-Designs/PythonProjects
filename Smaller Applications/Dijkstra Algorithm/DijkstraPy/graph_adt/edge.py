from typing import Any

from DijkstraPy.graph_adt.iedge import IEdge
from DijkstraPy.graph_adt.ivertex import IVertex


class Edge(IEdge):
    def __init__(self, data: Any, weight: float, destination: IVertex):
        self._data = data
        self._weight = weight
        self._destination = destination

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def data(self) -> Any:
        return self._data

    @property
    def destination(self) -> IVertex:
        return self._destination

    def __str__(self) -> str:
        return f'{self.data}'

    def __eq__(self, other) -> bool:
        if other is not None and isinstance(other, Edge):
            return self.data == other.data and self.weight == other.weight and self.destination == other.destination

