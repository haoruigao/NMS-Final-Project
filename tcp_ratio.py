import heapq
import random
import math

# Example graph
THROUGHPUT_DICT = {
    'US-EAST-1': {'US-EAST-1': 32100, 'EU-CENTRAL-1': 67.5, 'US-WEST-1': 74.3, 'AP-NORTHEAST-1': 50.9},
    'EU-CENTRAL-1': {'US-EAST-1': 75.1, 'EU-CENTRAL-1': 30300, 'US-WEST-1': 71.1, 'AP-NORTHEAST-1': 32.9},
    'US-WEST-1': {'US-EAST-1': 66, 'EU-CENTRAL-1': 51.9, 'US-WEST-1': 32700, 'AP-NORTHEAST-1': 71.8},
    'AP-NORTHEAST-1': {'US-EAST-1': 57.4, 'EU-CENTRAL-1': 43.7, 'US-WEST-1': 74.7, 'AP-NORTHEAST-1': 30400}
}

def dijkstra_max(graph, start, end):
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
    print("dijkstra max result path:")
    print(result_path)
    return distances[end], result_path


def dijkstra_min(graph: dict, start: str, end: str):
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
    return distances[end], result_path



def cost_graph(throughput_graph: dict):    
    cost_dict = {}

    for outer_key in throughput_graph:
        cost_dict[outer_key] = {}
        for inner_key in throughput_graph[outer_key]:
            cost_dict[outer_key][inner_key] = round(random.uniform(0.01, 0.3), 2)
    
    return cost_dict


def write_to_file(result_dict: dict):
    file_path = 'result_dict.txt'

    with open(file_path, 'w') as file:
        for outer_key, inner_dict in result_dict.items():
            for inner_key, value in inner_dict.items():
                file.write(f"{outer_key},{inner_key},{value}\n")


def cost_throughput_ratio_graph(throughput_dict: dict, cost_dict: dict):
    ratio_dict = {}

    for outer_key in throughput_dict:
        ratio_dict[outer_key] = {}
        for inner_key in throughput_dict[outer_key]:
            ratio_dict[outer_key][inner_key] = cost_dict[outer_key][inner_key] / throughput_dict[outer_key][inner_key]
    
    return ratio_dict


def negate_dict_val(dic: dict):
    negated_dict = {}
    for key, inner_dict in dic.items():
        negated_dict[key] = {}
        for inner_key, value in inner_dict.items():
            negated_dict[key][inner_key] = -value
    return negated_dict


def path_total_cost(result_path: list, cost_dict: dict):
    total_cost = 0
    start = None
    end = None
    for i in range(len(result_path) - 1):
        start = result_path[i]
        end = result_path[i + 1]
        total_cost += cost_dict[start][end]
    return total_cost


cost_dict = {
    'US-EAST-1': {'US-EAST-1': 0.01, 'EU-CENTRAL-1': 0.2, 'US-WEST-1': 0.10, 'AP-NORTHEAST-1': 0.35},
    'EU-CENTRAL-1': {'US-EAST-1': 0.2, 'EU-CENTRAL-1': 0.01, 'US-WEST-1': 0.17, 'AP-NORTHEAST-1': 0.56},
    'US-WEST-1': {'US-EAST-1': 0.10, 'EU-CENTRAL-1': 0.17, 'US-WEST-1': 0.01, 'AP-NORTHEAST-1': 0.22},
    'AP-NORTHEAST-1': {'US-EAST-1': 0.35, 'EU-CENTRAL-1': 0.56, 'US-WEST-1': 0.28, 'AP-NORTHEAST-1': 0.01}
}


ratio_dict = cost_throughput_ratio_graph(THROUGHPUT_DICT, cost_dict)

improvement = []
for start_node in ratio_dict.keys():
    for end_node in ratio_dict.keys():
        if start_node != end_node:
            distances = dijkstra_min(ratio_dict, start_node, end_node)[0]
            print(f"The direct ratio from {start_node} to {end_node} is {ratio_dict[start_node][end_node]}")
            print(f"The min ratio from {start_node} to {end_node} is {distances}")
            improvement.append((ratio_dict[start_node][end_node] - distances) / ratio_dict[start_node][end_node] * 100)

print(improvement)
print(max(improvement))
print(sum(improvement)/len(improvement))