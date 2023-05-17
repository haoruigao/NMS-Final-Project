import heapq

def dijkstra(graph, start, end):
    # +
    distances = {vertex: 0 for vertex in graph}
    path = {vertex: None for vertex in graph}
    distances[start] = - graph[start][start]
    # -
    pq = [(graph[start][start], start)]
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
    'US-EAST-1': {'US-EAST-1': 13000, 'EU-CENTRAL-1': 334, 'US-WEST-1': 307, 'AP-NORTHEAST-1': 325},
    'EU-CENTRAL-1': {'US-EAST-1': 316, 'EU-CENTRAL-1': 12800, 'US-WEST-1': 271, 'AP-NORTHEAST-1': 266},
    'US-WEST-1': {'US-EAST-1': 303, 'EU-CENTRAL-1': 297, 'US-WEST-1': 13000, 'AP-NORTHEAST-1': 331},
    'AP-NORTHEAST-1': {'US-EAST-1': 218, 'EU-CENTRAL-1': 259, 'US-WEST-1': 275, 'AP-NORTHEAST-1': 12700}
}

graph_o = {
    'US-EAST-1': {'US-EAST-1': -13000, 'EU-CENTRAL-1': -334, 'US-WEST-1': -307, 'AP-NORTHEAST-1': -325},
    'EU-CENTRAL-1': {'US-EAST-1': -316, 'EU-CENTRAL-1': -12800, 'US-WEST-1': -271, 'AP-NORTHEAST-1': -266},
    'US-WEST-1': {'US-EAST-1': -303, 'EU-CENTRAL-1': -297, 'US-WEST-1': -13000, 'AP-NORTHEAST-1': -331},
    'AP-NORTHEAST-1': {'US-EAST-1': -218, 'EU-CENTRAL-1': -259, 'US-WEST-1': -275, 'AP-NORTHEAST-1': -12700}
}
improvement = []
for start_node in graph.keys():
    for end_node in graph.keys():
        if start_node != end_node:
            shortest_path_distance = dijkstra(graph_o, start_node, end_node)
            print(f"The best path distance between {start_node} and {end_node} is {shortest_path_distance}.")
            print(f"The direct path distance between {start_node} and {end_node} is {graph[start_node][end_node]}.")
            print(f"The improvement of best path is {(shortest_path_distance - graph[start_node][end_node]) / graph[start_node][end_node] * 100} %.")
            improvement.append((shortest_path_distance - graph[start_node][end_node]) / graph[start_node][end_node] * 100)

print(improvement)
print(max(improvement))
print(sum(improvement)/len(improvement))