class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, value):
       # Agrega un nuevo nodo al final de la lista
        new_node = DoublyNode(value)
        if not self.head:
            self.head = self.tail = self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.current = new_node  # Mover el puntero actual al nuevo nodo

    def delete(self):
        #Elimina el nodo actual  
        if not self.current:
            return

        if self.current.prev:
            self.current.prev.next = self.current.next
        if self.current.next:
            self.current.next.prev = self.current.prev

        if self.current == self.head:
            self.head = self.current.next
        if self.current == self.tail:
            self.tail = self.current.prev

        self.current = self.current.prev if self.current.prev else self.head

    def move_forward(self):
        #Mover al siguiente estado en la lista
        if self.current and self.current.next:
            self.current = self.current.next

    def move_backward(self):
        # Mover al estado anterior en la lista
        if self.current and self.current.prev:
            self.current = self.current.prev

    def get_current(self):
        # Obtener el estado actual
        return self.current.value if self.current else ""
import tkinter as tk
from tkinter import ttk

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BLOCK DE NOTAS 2")

        self.history = DoublyLinkedList()

        self.text_area = tk.Text(root, height=50, width=70)
        self.text_area.pack(pady=10)

        # Botones de acción
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.save_button = ttk.Button(button_frame, text="Guardar estado", command=self.save_state)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.undo_button = ttk.Button(button_frame, text="Deshacer", command=self.undo)
        self.undo_button.pack(side=tk.LEFT, padx=5)

        self.redo_button = ttk.Button(button_frame, text="Rehacer", command=self.redo)
        self.redo_button.pack(side=tk.LEFT, padx=5)

    def save_state(self):
        #Guarda el estado actual del texto en la lista doblemente enlazada
        text = self.text_area.get("1.0", tk.END).strip()
        self.history.append(text)

    def undo(self):
        #Mueve al estado anterior y lo muestra en el área de texto
        self.history.move_backward()
        self.update_text_area()

    def redo(self):
        #Mueve al estado siguiente y lo muestra en el área de texto
        self.history.move_forward()
        self.update_text_area()

    def update_text_area(self):
        #Actualiza el área de texto con el estado actual
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", self.history.get_current())

# Ejecutar la aplicación
root = tk.Tk()
app = TextEditorApp(root)
root.mainloop()
