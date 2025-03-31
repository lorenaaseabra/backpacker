# Dijkstra's Algorithm for European Capitals

## Description

This project implements Dijkstra's algorithm to find the shortest path between European capitals. The program represents cities as nodes in a graph, where edges represent direct connections between cities with their respective distances in kilometers.

The algorithm identifies not only the shortest total distance between two cities but also the entire route to be taken, including all necessary intermediate cities.

## Features

- Finds the shortest path between two European capitals
- Shows the complete route, including all intermediate cities
- Calculates the total distance in kilometers
- Simple and intuitive command-line interface

## Included Cities

The graph includes the following 11 European capitals:
- Berlin
- Vienna
- Brussels
- Prague
- Copenhagen
- Paris
- Athens
- Budapest
- Rome
- Lisbon
- Madrid

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `Dijkstra.py` file
2. Ensure Python 3 is installed on your system

## How to Use

1. Run the program:
   ```
   python3 Dijkstra.py
   ```

2. When prompted, enter the name of the origin city exactly as it appears in the list

3. Next, enter the name of the destination city

4. The program will display the shortest path and the total distance in kilometers

5. To exit the program, type 'exit' when prompted for the origin city

## Usage Example

```
Available cities:
1. Berlin
2. Vienna
3. Brussels
4. Prague
5. Copenhagen
6. Paris
7. Athens
8. Budapest
9. Rome
10. Lisbon
11. Madrid

Enter the name of the origin city (or 'exit' to quit): Athens
Enter the name of the destination city: Berlin

Shortest path from Athens to Berlin:
Athens -> Budapest -> Vienna -> Berlin
Total distance: 2090 km
```

## How It Works

Dijkstra's algorithm works as follows:

1. Initializes the distance of the origin city as 0 and all other cities as infinity
2. For each iteration, selects the unvisited city with the smallest distance
3. Updates distances to all neighboring cities
4. Marks the city as visited
5. Continues until all accessible cities have been visited or until the destination city is reached
6. Reconstructs the path taken using the previous nodes

## Code Structure

- `dijkstra(graph, origin_city, destination_city, cities)`: Implementation of Dijkstra's algorithm
- `main()`: Main function that manages the user interface
- Adjacency matrix: Represents connections between cities and their distances

## Note

The distances used are approximations based on real routes between European capitals. The graph is configured so that some cities are only reachable through other intermediate cities, making the program more realistic.

## License

This project is available under the MIT license.