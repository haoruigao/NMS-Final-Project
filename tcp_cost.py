import heapq
import math


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    path = {vertex: None for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                path[neighbor] = current_vertex
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    result_path = []
    next = end
    while path[next] is not None:
        result_path.append(next)
        next = path[next]
    result_path.append(next)
    result_path.reverse()
    print(result_path)
    return distances[end]


graph = {
    'US-EAST-1': {'US-EAST-1': 0.01, 'EU-CENTRAL-1': 0.2, 'US-WEST-1': 0.10, 'AP-NORTHEAST-1': 0.35},
    'EU-CENTRAL-1': {'US-EAST-1': 0.2, 'EU-CENTRAL-1': 0.01, 'US-WEST-1': 0.17, 'AP-NORTHEAST-1': 0.56},
    'US-WEST-1': {'US-EAST-1': 0.10, 'EU-CENTRAL-1': 0.17, 'US-WEST-1': 0.01, 'AP-NORTHEAST-1': 0.22},
    'AP-NORTHEAST-1': {'US-EAST-1': 0.35, 'EU-CENTRAL-1': 0.56, 'US-WEST-1': 0.28, 'AP-NORTHEAST-1': 0.01}
}

graph_o = {
    'US-EAST-1': {'US-EAST-1': 0.001, 'EU-CENTRAL-1': 0.02, 'US-WEST-1': 0.02, 'AP-NORTHEAST-1': 0.09},
    'EU-CENTRAL-1': {'US-EAST-1': 0.02, 'EU-CENTRAL-1': 0.001, 'US-WEST-1': 0.02, 'AP-NORTHEAST-1': 0.09},
    'US-WEST-1': {'US-EAST-1': 0.02, 'EU-CENTRAL-1': 0.02, 'US-WEST-1': 0.001, 'AP-NORTHEAST-1': 0.09},
    'AP-NORTHEAST-1': {'US-EAST-1': 0.09, 'EU-CENTRAL-1': 0.09, 'US-WEST-1': 0.09, 'AP-NORTHEAST-1': 0.001}
}
improvement = []
for start_node in graph.keys():
    for end_node in graph.keys():
        if start_node != end_node:
            distances = dijkstra(graph, start_node, end_node)
            print(f"The direct cost from {start_node} to {end_node} is {graph[start_node][end_node]}")
            print(f"The min cost from {start_node} to {end_node} is {distances}")
            improvement.append((graph[start_node][end_node] - distances) / graph[start_node][end_node] * 100)

print(improvement)
print(max(improvement))
print(sum(improvement)/len(improvement))

# start = input("Start: ")
# end = input("End: ")
#
# if start not in graph:
#     start = 'US-WEST-1'
#
# if end not in graph:
#     end = 'EU-CENTRAL-1'

# distances = dijkstra(graph, start, end)

#print(f"The direct cost from {start} to {end} is {graph[start][end]}")
#print(f"The min cost from {start} to {end} is {distances}")