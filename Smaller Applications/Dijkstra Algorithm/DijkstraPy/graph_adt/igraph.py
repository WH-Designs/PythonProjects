from abc import ABC, abstractmethod
from typing import Any

from DijkstraPy.graph_adt.iedge import IEdge

class IGraph(ABC):

    @property
    @abstractmethod
    def empty(self) -> bool:
        pass

    @property
    @abstractmethod
    def all_vertices(self) -> list:
        pass

    @abstractmethod
    def processed_vertices(self, are_processed: bool) -> list:
        pass

    @abstractmethod
    def edges(self, vertex_data: Any) -> list:
        pass

    @abstractmethod
    def add_vertex(self, vertex_data: Any) -> None:
        pass

    @abstractmethod
    def remove_vertex(self, vertex_data: Any) -> None:
        pass

    @abstractmethod
    def add_edge(self, origin_vertex_data: Any, destination_vertex_data: Any, edge_data: Any, weight: float) -> None:
        pass

    @abstractmethod
    def remove_edge(self, origin_vertex_data: Any, destination_vertex_data: Any, edge_data: float) -> None:
        pass

    @abstractmethod
    def get_edge(self, origin_vertex_data: Any, destination_vertex_data: Any) -> IEdge:
        pass

    @abstractmethod
    def set_vertex_processed_state(self, vertex_data: Any, is_processed: bool) -> None:
        pass

    @abstractmethod
    def get_vertex_processed_state(self, vertex_data: Any) -> bool:
        pass
