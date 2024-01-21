from collections import defaultdict

def count_nodes(node, graph, visited):
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += count_nodes(neighbor, graph, visited)
    return count

def solution(n, wires):
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    min_difference = float('inf')

    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])

        visited = [False] * (n + 1)
        count1 = count_nodes(wire[0], graph, visited)
        count2 = count_nodes(wire[1], graph, visited)

        difference = abs(count1 - count2)
        min_difference = min(min_difference, difference)

        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    return min_difference