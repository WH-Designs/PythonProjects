from typing import Any

from DijkstraPy.graph_adt.edge import Edge
from DijkstraPy.graph_adt.ivertex import IVertex


class Vertex(IVertex):
    def __init__(self, data: Any):
        self._data = data
        self._edges = list()
        self._processed = False

    @property
    def data(self) -> Any:
        return self._data

    @property
    def edges(self) -> list:
        return self._edges

    @property
    def processed(self) -> bool:
        return self._processed

    def set_processed(self, process):
        self._processed = process

    def add_edge(self, data: Any, destination_vertex: 'IVertex', weight: float) -> None:
        self._edges.append(Edge(data, weight, destination_vertex))

    def remove_edge(self, data: Any, destination_vertex: 'IVertex') -> None:
        edge = next((edge for edge in self._edges if edge.destination == destination_vertex), None)

        if edge is not None:
            self._edges.remove(edge)

    def __eq__(self, other) -> bool:
        if other is not None and isinstance(other, Vertex):
            return self.data == other.data and self.edges == other.edges and self.processed == other.processed

        return False

    def __str__(self) -> str:
        return f'{self.data}'
