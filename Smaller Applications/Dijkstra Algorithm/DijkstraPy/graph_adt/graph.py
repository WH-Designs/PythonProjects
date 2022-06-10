from typing import Any

from DijkstraPy.graph_adt.ivertex import IVertex
from DijkstraPy.graph_adt.iedge import IEdge
from DijkstraPy.graph_adt.igraph import IGraph
from DijkstraPy.graph_adt.vertex import Vertex


class Graph(IGraph):
    def __init__(self):
        self._vertices: list = []

    @property
    def empty(self) -> bool:
        return len(self._vertices) == 0

    @property
    def all_vertices(self) -> list:
        return self._vertices

    def print_vertices(self):
        count = 0
        for vertex in self._vertices:
            print(f'{count} : {vertex}')
            count += 1

    def processed_vertices(self, are_processed: bool) -> list:
        vertex_array = list()

        for vertex in self._vertices:
             if vertex.processed == are_processed:
                 vertex_array.append(vertex)

        return vertex_array

    def edges(self, vertex_data: Any) -> list:
        list_of_edges = []
        for vertex in self._vertices:
            for edge in vertex.edges:
                list_of_edges.append(edge.data)

        return list_of_edges

    def add_vertex(self, vertex_data: Any) -> None:
        if not any(vertex_data == vertex.data for vertex in self._vertices):
            self._vertices.append(Vertex(vertex_data))

    def remove_vertex(self, vertex_data: Any) -> None:
        if any(vertex_data == vertex.data for vertex in self._vertices):
            self._vertices.remove(vertex_data)

    def add_edge(self, origin_vertex_data: Any, destination_vertex_data: Any, edge_data: Any, weight: float) -> None:
        origin: IVertex = next((vertex for vertex in self._vertices if vertex.data == origin_vertex_data), None)
        destination: IVertex = next((vertex for vertex in self._vertices if vertex.data == destination_vertex_data), None)

        if origin is None:
            self.add_vertex(origin)
            origin = next(vertex for vertex in self._vertices if vertex.data == origin_vertex_data)

        if destination is None:
            self.add_vertex(destination)
            destination = next(vertex for vertex in self._vertices if vertex.data == origin_vertex_data)

        origin.add_edge(edge_data, destination, weight)

    def remove_edge(self, origin_vertex_data: Any, destination_vertex_data: Any, edge_data: float) -> None:
        for vertex in self._vertices:
            for edge in vertex.edges:
                if edge.origin == origin_vertex_data:
                    if edge.destination == destination_vertex_data:
                        del edge

    def get_edge(self, origin_vertex_data: Any, destination_vertex_data: Any) -> IEdge:
        for edge in origin_vertex_data.edges:
            if edge.destination == destination_vertex_data:
                return edge

    def set_vertex_processed_state(self, vertex_data: Any, is_processed: bool) -> None:
        vertex_data.set_processed(is_processed)

    def get_vertex_processed_state(self, vertex_data: Any) -> bool:
        # for vertex in self._vertices:
        #     if vertex.data == vertex_data:
        #         return vertex
        return vertex_data.processed

    def __str__(self) -> str:
        graph_str = 'Graph Contents:\n'

        for vertex in self._vertices:
            graph_str += f'{vertex.data}\n'
            for edge in vertex.edges:
                graph_str += f'\t--> {edge.data} to {edge.destination.data}\n'

        return graph_str
