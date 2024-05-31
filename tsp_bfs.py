# tsp_bfs.py by GISGINIS MICHAIL

from tsp_utils import calculate_path_cost

def bfs_tsp(distances):
    """
    Solve the TSP using Breadth-First Search algorithm.
    """
    num_cities = len(distances)
    min_cost = float('inf')
    best_path = None
    queue = [(0, [0])]  # (current_city, path)
    
    while queue:
        current_city, path = queue.pop(0)
        if len(path) == num_cities:
            cost = calculate_path_cost(path, distances)
            if cost < min_cost:
                min_cost = cost
                best_path = path
        else:
            for city in range(num_cities):
                if city not in path:
                    queue.append((city, path + [city]))
    
    return best_path, min_cost
