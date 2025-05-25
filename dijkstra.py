import heapq

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

    # Reconstrucción del camino
    ruta = []
    actual = fin
    while actual:
        ruta.insert(0, actual)
        actual = anterior[actual]

    return ruta, distancias[fin]
