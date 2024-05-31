# tsp_astar.py by GISGINIS MICHAIL

import heapq
from tsp_utils import calculate_path_cost, calculate_heuristic

def a_star_tsp(distances):
    """
    Solve the TSP using A* Search algorithm.
    """
    num_cities = len(distances)
    min_cost = float('inf')
    best_path = None
    queue = [(0, [0])]  # (cost + heuristic, path)
    
    while queue:
        cost, path = heapq.heappop(queue)
        if len(path) == num_cities:
            total_cost = calculate_path_cost(path, distances)
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path
        else:
            for city in range(num_cities):
                if city not in path:
                    new_cost = cost + distances[path[-1]][city]
                    heuristic_value = calculate_heuristic(path + [city], distances)
                    heapq.heappush(queue, (new_cost + heuristic_value, path + [city]))
    
    return best_path, min_cost
