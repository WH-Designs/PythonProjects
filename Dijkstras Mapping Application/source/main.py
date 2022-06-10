from graph import Graph
from PIL import Image


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)


        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1


        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def main():
    """

    - Take in a starting location and an end location from the user

    - Use Dijkstra's algorithm to calculate the shortest path from those
      two locations

        - use the graph of the campus

    - Print out instructions on how to get to the desired end location:
        - names of buildings
        - distance for the entire walk

    ** add ons after the bare minimum is working **

    + add an interactive map with a gui
    + show a line from the start to end on a visual map
    + only show path from the start to end and not from building to building

    """
    # locations = ['Western University Center', 'Maaske Hall', 'Winters', 'Hamersly Library', 'Student Succes Center',
    #              'Intructional Techonology Center', 'Richard Woodcock Education Center',
    #              'Student Health and Counsling Center',
    #              'Ackerman Hall', 'Heritage Hall', 'Landers Hall', 'Barnum Hall', 'Gentle Hall',
    #              'Residential Service Center', 'Valsetz Dining Hall', 'Lieuallen Admin',
    #              'Todd Hall', 'Campbell Hall', 'WOU Welcome Center', 'Belamy Hall', 'Natural Sciences',
    #              'Academic Programs and Support Center',
    #              'Health and Wellness Center', 'New P.E', 'Computing Services', 'Arbor Park Apartments']
    #
    # print('Locations on Campus')
    # number_location = 1
    # for location in locations:
    #     print(f'{number_location} : {location}')
    #     number_location += 1
    #
    # print()
    #
    # starting_location = int(input('Enter the location number of where you are:\n'))
    #
    # print()
    #
    # for i in range(len(locations)):
    #     if starting_location - 1 == i:
    #         print('\033[1m' + f'Starting Location: {locations[i]}\n')
    #         break
    #     else:
    #         continue
    # locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    #
    # graph = Graph(8, locations)
                   # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
    # graph._graph = [[0, 1, 0, 0, 4, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 8, 0, 0],
    #                 [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 1, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [4, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0],
    #                 [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 2, 0],
    #                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    #                 [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [8, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # graph._graph = [[0, 0, 7, 21, 0, 0, 0, 18],
    #                 [0, 32, 0, 0, 40, 0, 0, 24],
    #                 [7, 32, 0, 12, 0, 0, 0, 0],
    #                 [21, 0, 12, 0, 26, 0, 0, 0],
    #                 [0, 40, 0, 26, 0, 0, 9, 0],
    #                 [0, 0, 0, 0, 0, 0, 18, 14],
    #                 [0, 0, 0, 0, 9, 18, 0, 0],
    #                 [18, 24, 0, 0, 0, 14, 0, 0]]
    #
    # graph.dijkstra_shortest_path(0)

    # img = Image.open('WOU_campus-map_2019.jpg')
    # img.show()

    # Code to print the list

    arr = [10, 80, 30, 90, 40, 50, 70]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

if __name__ == '__main__':
    main()
