import tkinter as tk
import math

class GraphCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.nodes = {}
        self.edges = {}

    def draw_graph(self, graph):
        self.delete("all")  # Clear canvas
        self.nodes.clear()
        self.edges.clear()

        # Calculate positions
        center_x = self.winfo_width() / 2
        center_y = self.winfo_height() / 2
        radius = min(center_x, center_y) - 50
        nodes = list(graph.keys())
        n = len(nodes)

        # Draw edges first
        for i, node in enumerate(nodes):
            angle = 2 * math.pi * i / n
            x1 = center_x + radius * math.cos(angle)
            y1 = center_y + radius * math.sin(angle)
            self.nodes[node] = (x1, y1)

            # Draw edges
            for neighbor, weight in graph[node].items():
                if neighbor > node:  # Draw each edge only once
                    x2, y2 = self.get_node_position(neighbor, nodes, n, center_x, center_y, radius)
                    line_id = self.create_line(x1, y1, x2, y2, fill='gray', width=2)
                    self.edges[(node, neighbor)] = line_id

                    # Draw weight
                    wx = (x1 + x2) / 2
                    wy = (y1 + y2) / 2
                    self.create_text(wx, wy, text=str(weight), fill='white')

        # Draw nodes
        for node, (x, y) in self.nodes.items():
            self.create_oval(x-20, y-20, x+20, y+20, fill='#F28F38', outline='white')
            self.create_text(x, y, text=node, fill='white', font=('Helvetica', 12, 'bold'))

    def get_node_position(self, node, nodes, n, center_x, center_y, radius):
        i = nodes.index(node)
        angle = 2 * math.pi * i / n
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        return x, y

    def highlight_path(self, path):
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            edge_id = self.edges.get((min(u, v), max(u, v)))
            if edge_id:
                self.itemconfig(edge_id, fill='#4CAF50', width=3)
