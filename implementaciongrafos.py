import tkinter as tk
from tkinter import messagebox
import random

class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_user(self, user):
        if user not in self.adjacency:
            self.adjacency[user] = []

    def add_friendship(self, user1, user2):
        if user1 in self.adjacency and user2 in self.adjacency:
            if user2 not in self.adjacency[user1]:
                self.adjacency[user1].append(user2)
            if user1 not in self.adjacency[user2]:
                self.adjacency[user2].append(user1)

    def get_friends(self, user):
        return self.adjacency.get(user, [])

    def bfs_level_2(self, user):
        visited = set()
        queue = [(user, 0)]
        suggestions = set()

        while queue:
            current, level = queue.pop(0)
            if current not in visited:
                visited.add(current)
                if level == 2:
                    suggestions.add(current)
                elif level < 2:
                    for neighbor in self.adjacency.get(current, []):
                        queue.append((neighbor, level + 1))

        suggestions.discard(user)
        suggestions -= set(self.adjacency.get(user, []))
        return list(suggestions)

class SocialGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Red Social (Grafo)")
        self.graph = Graph()
        self.node_positions = {}

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.setup_controls()

    def setup_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        user_frame = tk.Frame(frame)
        user_frame.pack(pady=5)

        tk.Label(user_frame, text="Nuevo usuario:").pack(side=tk.LEFT)
        self.entry_user = tk.Entry(user_frame, width=15)
        self.entry_user.pack(side=tk.LEFT, padx=5)
        tk.Button(user_frame, text="Agregar", command=self.add_user).pack(side=tk.LEFT)

        connect_frame = tk.Frame(frame)
        connect_frame.pack(pady=5)

        tk.Label(connect_frame, text="Conectar:").pack(side=tk.LEFT)
        self.entry_user1 = tk.Entry(connect_frame, width=10)
        self.entry_user1.pack(side=tk.LEFT, padx=2)
        tk.Label(connect_frame, text="↔").pack(side=tk.LEFT)
        self.entry_user2 = tk.Entry(connect_frame, width=10)
        self.entry_user2.pack(side=tk.LEFT, padx=2)
        tk.Button(connect_frame, text="Conectar", command=self.connect_users).pack(side=tk.LEFT)

        suggest_frame = tk.Frame(frame)
        suggest_frame.pack(pady=5)

        tk.Label(suggest_frame, text="Ver sugerencias para:").pack(side=tk.LEFT)
        self.entry_suggest_user = tk.Entry(suggest_frame, width=15)
        self.entry_suggest_user.pack(side=tk.LEFT, padx=5)
        tk.Button(suggest_frame, text="Sugerencias", command=self.show_suggestions).pack(side=tk.LEFT)

    def add_user(self):
        user = self.entry_user.get().strip()
        if user == "":
            messagebox.showwarning("Entrada invAlida", "Por favor escribe un nombre de usuario.")
            return
        if user in self.graph.adjacency:
            messagebox.showinfo("Usuario existente", f"El usuario '{user}' ya existe.")
            return

        self.graph.add_user(user)
        self.node_positions[user] = (random.randint(50, 550), random.randint(50, 350))
        self.draw_graph()
        self.entry_user.delete(0, tk.END)

    def connect_users(self):
        u1 = self.entry_user1.get().strip()
        u2 = self.entry_user2.get().strip()

        if not u1 or not u2:
            messagebox.showwarning("Entrada inválida", "Debes escribir ambos usuarios.")
            return
        if u1 == u2:
            messagebox.showwarning("Entrada inválida", "No puedes conectar un usuario consigo mismo.")
            return
        if u1 not in self.graph.adjacency or u2 not in self.graph.adjacency:
            messagebox.showerror("Error", "Ambos usuarios deben existir en la red.")
            return

        self.graph.add_friendship(u1, u2)
        self.draw_graph()
        self.entry_user1.delete(0, tk.END)
        self.entry_user2.delete(0, tk.END)

    def show_suggestions(self):
        user = self.entry_suggest_user.get().strip()
        if user not in self.graph.adjacency:
            messagebox.showerror("Error", f"El usuario '{user}' no existe.")
            return

        suggestions = self.graph.bfs_level_2(user)
        if suggestions:
            messagebox.showinfo("Sugerencias", f"Sugerencias para '{user}': {', '.join(suggestions)}")
        else:
            messagebox.showinfo("Sugerencias", f"No hay sugerencias de amistad para '{user}'.")

    def draw_graph(self):
        self.canvas.delete("all")
        # Dibujar aristas
        drawn = set()
        for user, friends in self.graph.adjacency.items():
            for friend in friends:
                if (user, friend) not in drawn and (friend, user) not in drawn:
                    x1, y1 = self.node_positions[user]
                    x2, y2 = self.node_positions[friend]
                    self.canvas.create_line(x1, y1, x2, y2)
                    drawn.add((user, friend))
        #NODOS DIBUJADOS 
        for user, (x, y) in self.node_positions.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="skyblue")
            self.canvas.create_text(x, y, text=user)

#INICIAR 
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialGraphApp(root)
    root.mainloop()
