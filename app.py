from flask import Flask, render_template, request, jsonify
import json
import heapq

app = Flask(__name__)

# Cargar el grafo y las coordenadas desde el JSON
with open('graph_data.json') as f:
    data = json.load(f)
    graph = data['grafo']
    coordenadas = data['coordenadas']  # Si las necesitas luego

# Algoritmo de Dijkstra
def dijkstra(graph, inicio, fin):
    distancias = {nodo: float('inf') for nodo in graph}
    distancias[inicio] = 0
    anterior = {nodo: None for nodo in graph}
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual == fin:
            break

        for vecino, peso in graph[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anterior[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    # Reconstruir el camino
    camino = []
    nodo = fin
    while nodo:
        camino.insert(0, nodo)
        nodo = anterior[nodo]

    return camino

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ruta', methods=['POST'])
def ruta():
    datos = request.get_json()
    origen = datos['origen']
    destino = datos['destino']
    ruta = dijkstra(graph, origen, destino)
    return jsonify({'ruta': ruta})

if __name__ == '__main__':
    app.run(debug=True)
