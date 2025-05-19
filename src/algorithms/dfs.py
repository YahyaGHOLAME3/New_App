"""
Algorithme DFS (Depth-First Search)
----------------------------------
Parcours en profondeur d'un graphe.

Exemple de graphe:
A --- B --- C
|     |     |
D --- E --- F
|     |     |
G --- H --- I

Le parcours commence au nœud 'A' et explore aussi loin que
possible le long de chaque branche avant de revenir en arrière.
"""

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    path = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            path.extend(dfs_recursive(graph, neighbor, visited))

    return path

def main():
    # Exemple de graphe non orienté
    graph = {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['B', 'F'],
        'D': ['A', 'E', 'G'],
        'E': ['B', 'D', 'F', 'H'],
        'F': ['C', 'E', 'I'],
        'G': ['D', 'H'],
        'H': ['G', 'E', 'I'],
        'I': ['F', 'H']
    }

    result = dfs_recursive(graph, 'A')
    return f"Parcours DFS depuis le nœud 'A': {' -> '.join(result)}"

if __name__ == "__main__":
    print(main())
