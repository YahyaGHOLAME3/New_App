"""
Algorithme BFS (Breadth-First Search)
-----------------------------------
Parcours en largeur d'un graphe.
Explore tous les nœuds voisins avant
d'aller plus profondément dans le graphe.

Exemple de graphe:
1 --- 2 --- 5
|     |     |
3 --- 4 --- 6
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            path.append(vertex)
            visited.add(vertex)
            queue.extend(n for n in graph[vertex] if n not in visited)

    return path

def main():
    graph = {
        '1': ['2', '3'],
        '2': ['1', '4', '5'],
        '3': ['1', '4'],
        '4': ['2', '3', '6'],
        '5': ['2', '6'],
        '6': ['4', '5']
    }

    result = bfs(graph, '1')
    return f"Parcours BFS depuis le nœud '1': {' -> '.join(result)}"

if __name__ == "__main__":
    print(main())
