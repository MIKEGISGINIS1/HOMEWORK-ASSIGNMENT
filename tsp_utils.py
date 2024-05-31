# tsp_utils.py by GISGINIS MICHAIL

import numpy as np

def calculate_path_cost(path, distances):
    """
    Calculate the total cost of a given path based on the distance matrix.
    """
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[path[i]][path[i + 1]]
    cost += distances[path[-1]][path[0]]  # Returning to the starting city
    return cost

def calculate_heuristic(path, distances):
    """
    Calculate a simple heuristic for the A* search.
    Here we use the minimum spanning tree (MST) heuristic.
    """
    remaining_cities = set(range(len(distances))) - set(path)
    if not remaining_cities:
        return 0
    
    last_city = path[-1]
    min_edge_cost = min(distances[last_city][city] for city in remaining_cities)
    return min_edge_cost

def generate_random_distance_matrix(num_cities):
    """
    Generate a random distance matrix for a given number of cities.
    """
    distances = np.random.randint(1, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distances, 0)
    return distances
