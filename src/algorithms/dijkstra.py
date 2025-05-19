"""
Algorithme de Dijkstra
---------------------
Trouve le plus court chemin entre deux nœuds
dans un graphe pondéré.

Exemple de graphe:
A --4-- B
|      /|
|    /  |
6  2    3
|/      |
C --1-- D
"""

from heapq import heappush, heappop
import sys

def dijkstra(graph, start, end):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heappop(pq)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heappush(pq, (distance, neighbor))

    return distances[end], previous

def main(graph=None, start='A', end='D'):
    if graph is None:
        graph = {
            'A': {'B': 4, 'C': 6},
            'B': {'A': 4, 'C': 2, 'D': 3},
            'C': {'A': 6, 'B': 2, 'D': 1},
            'D': {'B': 3, 'C': 1}
        }
    
    distance, previous = dijkstra(graph, start, end)

    # Reconstituer le chemin
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    # Store the path for visualization
    global _last_path
    _last_path = path

    return f"Plus court chemin de {start} à {end}:\nDistance: {distance}\nChemin: {' -> '.join(path)}"

def get_result_path():
    if '_last_path' in globals():
        return _last_path
    return []

if __name__ == "__main__":
    print(main())
