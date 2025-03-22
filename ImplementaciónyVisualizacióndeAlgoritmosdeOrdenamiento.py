import tkinter as tk
import random
import time

WIDTH = 600
HEIGHT = 400
BAR_WIDTH = 20
num_elements = WIDTH // BAR_WIDTH
paused = False
delay = 0.5

root = tk.Tk()
root.title("Visualización Interactiva de Algoritmos de Ordenamiento")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

array = []

def generate_array():
    global array
    array = [random.randint(10, 300) for _ in range(num_elements)]
    draw_array(array)

def draw_array(arr, colors=None):
    canvas.delete("all")
    if colors is None:
        colors = ["blue"] * len(arr)
    for i, value in enumerate(arr):
        x0 = i * BAR_WIDTH
        y0 = HEIGHT - value
        x1 = (i + 1) * BAR_WIDTH
        y1 = HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
    root.update()

def pause_sorting():
    global paused
    paused = not paused
    btn_pause.config(text="Reanudar" if paused else "Pausar")

def wait():
    while paused:
        root.update()
        time.sleep(0.1)
    time.sleep(delay)

def bubble_sort():
    global array
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                draw_array(array, ["red" if x == j or x == j + 1 else "blue" for x in range(n)])
                wait()
        if not swapped:
            break
    draw_array(array, ["green"] * n)

def selection_sort():
    global array
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array, ["red" if x == i or x == min_idx else "blue" for x in range(n)])
        wait()
    draw_array(array, ["green"] * n)

btn_generate = tk.Button(root, text="Generar Lista", command=generate_array)
btn_generate.pack(side=tk.LEFT, padx=5)

btn_bubble = tk.Button(root, text="Bubble Sort", command=bubble_sort)
btn_bubble.pack(side=tk.LEFT, padx=5)

btn_selection = tk.Button(root, text="Selection Sort", command=selection_sort)
btn_selection.pack(side=tk.LEFT, padx=5)

btn_pause = tk.Button(root, text="Pausar", command=pause_sorting)
btn_pause.pack(side=tk.LEFT, padx=5)

generate_array()

root.mainloop()
