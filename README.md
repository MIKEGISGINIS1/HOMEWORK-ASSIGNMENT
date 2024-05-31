# HOMEWORK-ASSIGNMENT by GISGINIS MICHAIL CEN2.2A

## Overview
This project is all about finding the shortest route that visits a given list of cities exactly once and returns to the starting point. We tackle this classic problem using three different algorithms: Breadth-First Search (BFS), Least-Cost (Uniform Cost) Search, and A* Search. 

## Project Structure
The project is organized into multiple modules to keep things clean and manageable. Here’s a quick overview of what each module does:

* tsp_bfs.py # Contains the BFS implementation for TSP
* tsp_ucs.py # Contains the Least-Cost (Uniform Cost) Search implementation for TSP
* tsp_astar.py # Contains the A* Search implementation for TSP
* tsp_utils.py # Utility functions for path cost calculation, heuristic, and generating random distances
* main.py # Runs experiments and compares the algorithms



## Installation
Before you start, make sure you have Python installed. You can install the required libraries using pip:

```bash
pip install numpy


Usage
To run the experiments and compare the algorithms, simply execute the main.py script. This script will generate random distance matrices for different numbers of cities and solve the TSP using BFS, Least-Cost Search, and A* Search.

python main.py
