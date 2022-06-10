import math
from sys import maxsize

from DijkstraPy.graph_adt.graph import Graph
from DijkstraPy.map.city import City


class Dijkstra:
    def __init__(self, graph: Graph):
        self._graph = graph
        self._cities = self._graph.all_vertices
        self._distances = [maxsize] * len(self._cities)
        self._predecessors = [-1] * len(self._cities)
        self._times = [maxsize] * len(self._cities)

    '''
    This function finds the minimum weight for unprocessed edges in the graph
    
    takes in the distances, current city, and the list of cities
    '''

    def find_min_index(self, distances, current_city, cities) -> int:
        lowest = maxsize
        index = current_city
        count = 0
        for i in distances:
            if cities[count].processed:
                count += 1
                continue
            if i < lowest:
                lowest = i
                index = count
            count += 1
        return index

    '''
    This function finds the smallest path for the graph, it uses recursion to go through the graph
    
    it takes in the predecessors, destination_city, and the stack 
    '''

    def find_smallest_path(self, predecessors, destination_city, stack: list):
        stack.append(destination_city)

        destination_city = predecessors[destination_city]
        if destination_city == -1:
            return
        else:
            self.find_smallest_path(predecessors, destination_city, stack)

    '''
    This is the main dijkstra algorithm that uses the two function above to calculate the shortest path for the graph
    
    this function takes in the origin_city and the destination_city which are user inputs
    
    this function also prints out the total distance in the graph for the start and end cities
    '''

    def dijkstra_shortest_path_distance(self, origin_city: int, destination_city: int):
        origin_vertex = self._cities[origin_city]
        destination_vertex = self._cities[destination_city]

        current_city = origin_vertex
        current_city_index = origin_city

        self._distances[current_city_index] = 0

        all_processed = False

        while all_processed is False:
            edges = current_city.edges

            for edge in edges:
                destination = edge.destination

                if destination.processed:
                    continue

                edge_destination_city = self._cities.index(destination)

                min_distance = self._distances[edge_destination_city]

                current_distance = edge.weight

                if current_distance < min_distance:
                    min_distance = current_distance
                    self._predecessors[edge_destination_city] = current_city_index
                    self._distances[edge_destination_city] = min_distance

            self._graph.set_vertex_processed_state(current_city, True)

            all_processed = True

            for i in self._cities:

                if not i.processed:
                    all_processed = False
                    break

            smallest_distance_vertex_index = self.find_min_index(self._distances, current_city_index, self._cities)

            current_city = self._cities[smallest_distance_vertex_index]

            current_city_index = smallest_distance_vertex_index

        direction_string = ""

        stack = []

        self.find_smallest_path(self._predecessors, destination_city, stack)

        direction_string, total_distance = self.print_stack_for_distance_algorithm(stack, direction_string)

        print(direction_string)
        print("Total distance:", total_distance, "miles")

        for vertex in self._cities:
            vertex.set_processed(False)

    def print_stack_for_distance_algorithm(self, stack, direction_string):
        total_distance = 0

        while len(stack) != 1:
            vertex = self._cities[stack.pop()]
            next_vertex = self._cities[stack[-1]]

            edge = self._graph.get_edge(vertex, next_vertex)

            print(edge.data)

            highway = edge.data

            city = next_vertex.data

            distance = edge.weight

            total_distance += distance

            direction_string += f"\nTake highway {highway.name} to {city} for {distance} miles\n"

        return direction_string, total_distance

    '''
        This is the secondary dijkstra algorithm that finds the shortest path based on the times from the file rather than the distances
        
        this also takes in an origin_city and a destination_city integer
        
        this function prints out the directions for the user and the total time it takes for the path 
    '''

    def dijkstra_shortest_path_time(self, origin_city: int, destination_city: int):
        origin_vertex = self._cities[origin_city]
        destination_vertex = self._cities[destination_city]

        current_city = origin_vertex
        current_city_index = origin_city

        self._times[current_city_index] = 0

        all_processed = False
        while all_processed is False:

            edges = current_city.edges

            for edge in edges:
                destination = edge.destination

                if destination.processed:
                    continue

                edge_destination_index = self._cities.index(destination)

                minimum_distance = self._times[edge_destination_index]

                current_hour = edge.weight / edge.data.average_mph

                if current_hour < minimum_distance:
                    minimum_distance = current_hour

                    self._predecessors[edge_destination_index] = current_city_index

                    self._times[edge_destination_index] = minimum_distance

            self._graph.set_vertex_processed_state(current_city, True)

            all_processed = True

            for i in self._cities:
                if not i.processed:
                    all_processed = False
                    break

            smallest_distance_vertex_index = self.find_min_index(self._times, current_city_index, self._cities)

            current_city = self._cities[smallest_distance_vertex_index]

            current_city_index = smallest_distance_vertex_index

        direction_string = ""

        stack = []

        self.find_smallest_path(self._predecessors, destination_city, stack)

        direction_string, total_hours = self.print_stack_for_time_algorithm(stack, direction_string)

        print(direction_string)
        print(f'Total Time: {total_hours} hours')

        for vertex in self._cities:
            vertex.set_processed(False)

    def print_stack_for_time_algorithm(self, stack, direction_string):
        total_hours = 0

        while len(stack) != 1:
            vertex = self._cities[stack.pop()]

            next_vertex = self._cities[stack[-1]]

            edge = self._graph.get_edge(vertex, next_vertex)

            highway = edge.data

            city = next_vertex.data

            hours = round(edge.weight / edge.data.average_mph, 2)

            total_hours += hours

            direction_string += f"\nTake {highway.name} to {city} for {hours} hours\n"

        return direction_string, total_hours
