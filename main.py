# main.py by GISGINIS MICHAIL

from tsp_bfs import bfs_tsp
from tsp_ucs import least_cost_search_tsp
from tsp_astar import a_star_tsp
from tsp_utils import generate_random_distance_matrix
import time

def run_experiments():
    num_cities_list = [4, 8, 12]
    
    for num_cities in num_cities_list:
        print(f"Running experiments for {num_cities} cities...")
        distances = generate_random_distance_matrix(num_cities)
        
        # BFS
        start_time = time.time()
        bfs_path, bfs_cost = bfs_tsp(distances)
        bfs_time = time.time() - start_time
        
        # Least-Cost Search
        start_time = time.time()
        ucs_path, ucs_cost = least_cost_search_tsp(distances)
        ucs_time = time.time() - start_time
        
        # A* Search
        start_time = time.time()
        astar_path, astar_cost = a_star_tsp(distances)
        astar_time = time.time() - start_time
        
        print(f"\nResults for {num_cities} cities:")
        print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}, Time: {bfs_time:.4f}s")
        print(f"UCS Path: {ucs_path}, Cost: {ucs_cost}, Time: {ucs_time:.4f}s")
        print(f"A* Path: {astar_path}, Cost: {astar_cost}, Time: {astar_time:.4f}s")
        print("-" * 50)

if __name__ == "__main__":
    run_experiments()
