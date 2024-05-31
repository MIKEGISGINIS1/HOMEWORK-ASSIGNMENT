# tsp_ucs.py by GISGINIS MICHAIL

import heapq
from tsp_utils import calculate_path_cost

def least_cost_search_tsp(distances):
    """
    Solve the TSP using Least-Cost (Uniform Cost) Search algorithm.
    """
    num_cities = len(distances)
    min_cost = float('inf')
    best_path = None
    queue = [(0, [0])]  # (cost, path)
    
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
                    heapq.heappush(queue, (new_cost, path + [city]))
    
    return best_path, min_cost
