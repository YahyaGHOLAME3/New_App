from .kruskal import main as kruskal
from .prim import main as prim
from .dijkstra import main as dijkstra
from .bfs import main as bfs
from .dfs import main as dfs
from .floyd_warshall import main as floyd_warshall

ALGORITHMS = {
    "Kruskal": kruskal,
    "Prim": prim,
    "Dijkstra": dijkstra,
    "BFS": bfs,
    "DFS": dfs,
    "Floyd-Warshall": floyd_warshall,
}

__all__ = [
    "kruskal",
    "prim",
    "dijkstra",
    "bfs",
    "dfs",
    "floyd_warshall",
    "ALGORITHMS",
]
