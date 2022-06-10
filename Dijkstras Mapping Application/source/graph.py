import math


class Graph:
    def __init__(self, vertices: int, locations: list):
        self._locations = locations
        self._vetices = vertices
        self._graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_solution(self, distance):
        print('\033[1m' + "Location : Distance from current location\n")
        for node in range(self._vetices):
            print('\033[0m' + f'{self._locations[node]} : {distance[node]}ft')

    def minimum_distance(self, distance, separate_vertices_set):
        min_index = int()
        min_distance = math.inf

        for vertice in range(self._vetices):
            if distance[vertice] <= min_distance and separate_vertices_set[vertice] == False:
                min_distance = distance[vertice]
                min_index = vertice

        return min_index

    def dijkstra_shortest_path(self, source_vertex):

        distance = [math.inf] * self._vetices
        distance[source_vertex] = 0
        separate_vertices_set = [False] * self._vetices

        for count in range(self._vetices):
            first_source = self.minimum_distance(distance, separate_vertices_set)

            separate_vertices_set[first_source] = True

            for vertice in range(self._vetices):
                if self._graph[first_source][vertice] > 0 and separate_vertices_set[vertice] == False and \
                        distance[vertice] > distance[first_source] + self._graph[first_source][vertice]:
                    distance[vertice] = distance[first_source] + self._graph[first_source][vertice]

        self.print_solution(distance)
