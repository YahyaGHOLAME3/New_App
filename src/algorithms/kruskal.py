"""
Algorithme de Kruskal
--------------------
Trouve l'arbre couvrant minimal (MST) dans un graphe pondéré.

Fonctionnement:
1. Trie les arêtes par poids croissant
2. Ajoute chaque arête si elle ne crée pas de cycle
3. Utilise Union-Find pour détecter les cycles

Complexité: O(E log E) où E est le nombre d'arêtes
"""

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if (v, u, weight) not in edges:
                edges.append((u, v, weight))

    edges.sort(key=lambda x: x[2])
    uf = UnionFind()

    for vertex in graph:
        uf.make_set(vertex)

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v))
            total_weight += weight

    return mst, total_weight

def get_example_graph():
    return {
        'A': {'B': 4, 'C': 6},
        'B': {'A': 4, 'C': 2, 'D': 3},
        'C': {'A': 6, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }

def main(graph=None, start=None, end=None):
    if graph is None:
        return "Erreur: Graphe non fourni"

    mst, total_weight = kruskal(graph)
    path_str = ' → '.join([f"{u}-{v}" for u, v in mst])

    return f"""
Résultat de l'algorithme de Kruskal:
-----------------------------------
Poids total de l'arbre: {total_weight}
Arêtes sélectionnées: {path_str}
"""

def get_result_path():
    return [edge for edge in _last_result] if '_last_result' in globals() else []

if __name__ == "__main__":
    print(main(get_example_graph()))
