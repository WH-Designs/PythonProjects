from DijkstraPy.pathfinding.dijkstra import Dijkstra
from city import City
from highway import Highway
from DijkstraPy.graph_adt.graph import Graph


def main():
    graph = Graph()

    print('0: Find the smallest path via distance\n1: Find the smallest path via time')

    path_finding_option = int(input('Enter what option you would like to do:\n'))

    with open("MapDataNew.txt") as file:
        lines = file.readlines()

        for line in lines:
            data = (line.split(','))
            city_1 = City(data[0], 0)
            city_2 = City(data[1], 0)

            graph.add_vertex(city_1)
            graph.add_vertex(city_2)

            highway_1 = Highway(data[2], int(data[4]))

            graph.add_edge(city_1, city_2, highway_1, float(data[3]))
            graph.add_edge(city_2, city_1, highway_1, float(data[3]))

    graph.print_vertices()

    starting_city = int(input("Pick a starting city:\n"))

    destination_city = int(input("Pick a destination city:\n"))

    print()

    dijkstra = Dijkstra(graph)

    if path_finding_option == 0:
        shortest_path_distance_starting_city_to_ending_city = dijkstra.dijkstra_shortest_path_distance(starting_city, destination_city)
    elif path_finding_option == 1:
        shortest_path_time_starting_city_to_ending_city = dijkstra.dijkstra_shortest_path_time(starting_city, destination_city)


if __name__ == "__main__":
    main()
