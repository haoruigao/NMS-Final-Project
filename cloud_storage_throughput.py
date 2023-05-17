import heapq
import math

def dijkstra(graph, start, end):
    # +
    distances = {vertex: 0 for vertex in graph}
    path = {vertex: None for vertex in graph}
    distances[start] = math.inf
    # -
    pq = [(-math.inf, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        current_distance = - current_distance
        if current_distance < distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            # +
            distance = min(current_distance, - weight)
            if distance > distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(pq, (-distance, neighbor))
    result_path = []
    next = end
    while path[next] is not None:
        result_path.append(next)
        next = path[next]
    result_path.append(next)
    result_path.reverse()
    print(result_path)
    return distances[end]

# Example graph
graph = {
    'AWS - US': {'GCP - US': 654.26, 'GCP - EU': 448.83, 'GCP- ASIA': 454.15},
    'AWS - EU': {'GCP - US': 447.14, 'GCP - EU': 624.32, 'GCP- ASIA': 325.83},
    'AWS - ASIA': {'GCP - US': 331.27, 'GCP - EU': 324.18, 'GCP- ASIA': 584.71},
    'GCP - US': {'GCP - US': 679.46, 'GCP - EU': 670.32, 'GCP- ASIA': 682.65},
    'GCP - EU': {'GCP - US': 643.64, 'GCP - EU': 657.06, 'GCP- ASIA': 619.33},
    'GCP- ASIA': {'GCP - US': 634.85, 'GCP - EU': 635.4, 'GCP- ASIA': 622.12},
}

graph_o = {
    'AWS - US': {'GCP - US': -654.26, 'GCP - EU': -448.83, 'GCP- ASIA': -454.15},
    'AWS - EU': {'GCP - US': -447.14, 'GCP - EU': -624.32, 'GCP- ASIA': -325.83},
    'AWS - ASIA': {'GCP - US': -331.27, 'GCP - EU': -324.18, 'GCP- ASIA': -584.71},
    'GCP - US': {'GCP - US': -679.46, 'GCP - EU': -670.32, 'GCP- ASIA': -682.65},
    'GCP - EU': {'GCP - US': -643.64, 'GCP - EU': -657.06, 'GCP- ASIA': -619.33},
    'GCP- ASIA': {'GCP - US': -634.85, 'GCP - EU': -635.4, 'GCP- ASIA': -622.12},
}

improvement = []
for start_node in ['AWS - US', 'AWS - EU', 'AWS - ASIA']:
    for end_node in ['GCP - US', 'GCP - EU', 'GCP- ASIA']:
        if start_node != end_node:
            shortest_path_distance = dijkstra(graph_o, start_node, end_node)
            print(f"The best path distance between {start_node} and {end_node} is {shortest_path_distance}.")
            print(f"The direct path distance between {start_node} and {end_node} is {graph[start_node][end_node]}.")
            print(f"The improvement of best path is {(shortest_path_distance - graph[start_node][end_node]) / graph[start_node][end_node] * 100} %.")
            improvement.append((shortest_path_distance - graph[start_node][end_node]) / graph[start_node][end_node] * 100)

print(improvement)
print(max(improvement))
print(sum(improvement)/len(improvement))