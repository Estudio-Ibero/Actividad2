import networkx as nx
import matplotlib.pyplot as plt
import heapq

def a_estrella(mapa, inicio, destino):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio)) 
    costos = {inicio: 0}  
    rutas = {inicio: None} 
    
    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == destino:
            ruta = []
            while nodo_actual:
                ruta.append(nodo_actual)
                nodo_actual = rutas[nodo_actual]
            return ruta[::-1]  
        
        for vecino, costo in mapa[nodo_actual].items():
            nuevo_costo = costos[nodo_actual] + costo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                rutas[vecino] = nodo_actual

    return None 

mapa_transporte = {
    'A': {'B': 5, 'C': 2, 'E': 7, 'J': 3},
    'B': {'A': 5, 'D': 3, 'F': 1, 'C': 6},  
    'C': {'A': 2, 'D': 8, 'G': 4, 'L': 6, 'F': 5},  
    'D': {'B': 3, 'C': 8, 'H': 5, 'M': 4, 'G': 2},  
    'E': {'A': 7, 'F': 2, 'N': 10, 'J': 5},  
    'F': {'B': 1, 'E': 2, 'G': 3, 'O': 7, 'C': 5}, 
    'G': {'C': 4, 'F': 3, 'H': 6, 'P': 3, 'D': 2}, 
    'H': {'D': 5, 'G': 6, 'I': 4, 'Q': 8, 'F': 4}, 
    'I': {'H': 4, 'R': 9, 'P': 6}, 
    'J': {'A': 3, 'K': 7, 'E': 5},  
    'K': {'J': 7, 'M': 2, 'L': 4},  
    'L': {'C': 6, 'J': 8, 'N': 5, 'K': 4}, 
    'M': {'D': 4, 'K': 2, 'O': 3, 'P': 6}, 
    'N': {'E': 10, 'L': 5, 'P': 4, 'O': 8},  
    'O': {'F': 7, 'M': 3, 'Q': 6, 'N': 8},  
    'P': {'G': 3, 'N': 4, 'R': 5, 'I': 6, 'M': 6},  
    'Q': {'H': 8, 'O': 6, 'R': 2, 'P': 5}, 
    'R': {'I': 9, 'P': 5, 'Q': 2}
}

inicio = 'R'   # Nodo de inicio
destino = 'A'   # Nodo de destino

ruta_optima = a_estrella(mapa_transporte, inicio, destino)

print(f'Ruta Óptima: {ruta_optima}')

G = nx.Graph()

for nodo, vecinos in mapa_transporte.items():
    for vecino, costo in vecinos.items():
        G.add_edge(nodo, vecino, weight=costo)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

if ruta_optima:
    edges_optima = [(ruta_optima[i], ruta_optima[i+1]) for i in range(len(ruta_optima)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_optima, edge_color='red', width=3)

plt.title(f'Ruta Óptima desde {inicio} hasta {destino}')
plt.suptitle(f'Ruta Óptima: {ruta_optima}')
plt.show()
print('Fin del programa')
