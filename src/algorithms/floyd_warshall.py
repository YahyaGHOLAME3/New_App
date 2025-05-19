"""
Algorithme de Floyd-Warshall
---------------------------
Trouve les plus courts chemins entre toutes les paires
de sommets dans un graphe pondéré.

Exemple de graphe:
A ---4--- B
|\\       /|
| \\     / |
6  2   3  1
|   \\ /   |
C ---1--- D
"""

def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    dist = {i: {j: float('infinity') for j in nodes} for i in nodes}

    # Initialize distances
    for i in nodes:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def main(start='A', end='D'):
    graph = {
        'A': {'B': 4, 'C': 6, 'D': 2},
        'B': {'A': 4, 'C': 3, 'D': 1},
        'C': {'A': 6, 'B': 3, 'D': 1},
        'D': {'A': 2, 'B': 1, 'C': 1}
    }

    distances = floyd_warshall(graph)
    return f"Distance minimale de {start} à {end}: {distances[start][end]}"

def get_example_graph():
    return {
        'A': {'B': 4, 'C': 6, 'D': 2},
        'B': {'A': 4, 'C': 3, 'D': 1},
        'C': {'A': 6, 'B': 3, 'D': 1},
        'D': {'A': 2, 'B': 1, 'C': 1}
    }
