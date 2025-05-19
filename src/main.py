import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from algorithms import kruskal, prim, dijkstra, bfs, dfs
import random
from visualization import GraphCanvas

THEME = {
    "bg": "#16324F",
    "fg": "#FFFFFF",
    "button_bg": "#F28F38",
    "button_hover": "#FF9F45",
    "canvas_bg": "#1E1E1E",
    "highlight": "#4CAF50"
}

class AlgorithmeGraphe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algorithmes de Graphes - Projet Interface")
        self.geometry("900x700")
        self.configure(bg=THEME["bg"])

        # Style configuration
        style = ttk.Style()
        style.configure("Custom.TButton",
                       background=THEME["button_bg"],
                       foreground=THEME["fg"],
                       padding=10,
                       font=("Helvetica", 11))

        self.create_widgets()

    def create_widgets(self):
        # Identification de l'étudiant
        header_frame = ttk.Frame(self)
        header_frame.pack(pady=20, padx=20, fill="x")

        ttk.Label(header_frame,
                 text="Interface Éducative des Algorithmes de Graphe",
                 font=("Helvetica", 18, "bold"),
                 background=THEME["bg"],
                 foreground=THEME["fg"]).pack()

        # Paramètres du graphe
        param_frame = ttk.LabelFrame(self, text="Paramètres du Graphe", padding=15)
        param_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(param_frame, text="Nombre de sommets:").grid(row=0, column=0, padx=5)
        self.vertices_var = tk.StringVar(value="5")
        self.vertices_entry = ttk.Entry(param_frame, textvariable=self.vertices_var, width=10)
        self.vertices_entry.grid(row=0, column=1, padx=5)

        # Algorithmes disponibles
        algo_frame = ttk.LabelFrame(self, text="Algorithmes Disponibles", padding=15)
        algo_frame.pack(pady=20, padx=20, fill="x")

        algorithms = [
            ("Kruskal - Arbre couvrant minimal", self.run_kruskal),
            ("Prim - Arbre couvrant minimal", self.run_prim),
            ("Dijkstra - Plus court chemin", self.run_dijkstra),
            ("BFS - Parcours en largeur", self.run_bfs),
            ("DFS - Parcours en profondeur", self.run_dfs)
        ]

        for i, (name, command) in enumerate(algorithms):
            btn = ttk.Button(algo_frame, text=name, command=command, style="Custom.TButton")
            btn.pack(pady=8, padx=20, fill="x")

    def generate_random_graph(self):
        try:
            n = int(self.vertices_entry.get())
            if n < 2:
                raise ValueError("Le nombre de sommets doit être >= 2")

            graph = {}
            vertices = [chr(65 + i) for i in range(n)]  # A, B, C, ...

            for v in vertices:
                graph[v] = {}
                for u in vertices:
                    if u > v:  # Avoid duplicates
                        if random.random() < 0.7:  # 70% chance of edge
                            weight = random.randint(1, 10)
                            graph[v][u] = weight
                            graph.setdefault(u, {})[v] = weight

            return graph
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
            return None

    def open_algorithm_window(self, title, algo_module, start_node=None, end_node=None):
        graph = self.generate_random_graph()
        if not graph:
            return

        win = tk.Toplevel(self)
        win.title(f"Algorithme {title}")
        win.geometry("1000x800")
        win.configure(bg=THEME["bg"])

        # Canvas pour visualisation
        canvas = GraphCanvas(win, width=800, height=400, bg=THEME["canvas_bg"])
        canvas.pack(pady=20, padx=20)

        # Explication de l'algorithme
        explanation = scrolledtext.ScrolledText(win, width=80, height=10,
                                              bg=THEME["canvas_bg"],
                                              fg=THEME["fg"],
                                              font=("Courier", 11))
        explanation.pack(pady=10, padx=20)
        explanation.insert(tk.END, algo_module.__doc__)
        explanation.config(state="disabled")

        # Résultat
        result_text = algo_module.main(graph, start_node, end_node)
        canvas.draw_graph(graph)
        if hasattr(algo_module, 'get_result_path'):
            canvas.highlight_path(algo_module.get_result_path())

        result_label = ttk.Label(win, text=result_text,
                                background=THEME["bg"],
                                foreground=THEME["fg"],
                                font=("Helvetica", 11))
        result_label.pack(pady=20)

    def run_kruskal(self):
        self.open_algorithm_window("Kruskal", kruskal)

    def run_prim(self):
        self.open_algorithm_window("Prim", prim)

    def run_dijkstra(self):
        self.open_algorithm_window("Dijkstra", dijkstra, start_node="A", end_node="D")

    def run_bfs(self):
        self.open_algorithm_window("BFS", bfs, start_node="A")

    def run_dfs(self):
        self.open_algorithm_window("DFS", dfs, start_node="A")

if __name__ == "__main__":
    app = AlgorithmeGraphe()
    app.mainloop()
