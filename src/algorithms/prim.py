"""
Algorithme de Prim
-----------------
Trouve l'arbre couvrant minimal dans un graphe pondéré.
Commence par un sommet et étend l'arbre en choisissant
l'arête de poids minimal à chaque étape.

Exemple de graphe:
  A --4-- B
  |      /|
  |    /  |
  6  2    3
  |/      |
  C --1-- D
"""

from heapq import heappush, heappop

def prim(graph, start):
    mst = []
    visited = {start}
    edges = []

    # Ajouter toutes les arêtes du nœud de départ
    for neighbor, weight in graph[start].items():
        heappush(edges, (weight, start, neighbor))

    while edges:
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            # Ajouter les nouvelles arêtes
            for next_vertex, next_weight in graph[v].items():
                if next_vertex not in visited:
                    heappush(edges, (next_weight, v, next_vertex))

    return mst

def main():
    graph = {
        'A': {'B': 4, 'C': 6},
        'B': {'A': 4, 'C': 2, 'D': 3},
        'C': {'A': 6, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }

    result = prim(graph, 'A')
    total_weight = sum(weight for _, _, weight in result)
    path = ', '.join(f"{u}-{v}" for u, v, _ in result)

    return f"Prim MST Cost: {total_weight}\nChemin: {path}"

if __name__ == "__main__":
    print(main())
