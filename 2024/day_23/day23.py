from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 7
expected_output_part_two = "co,de,ka,ta"

def parse_input(input_data):
    lines = input_as_lines(input_data)
    graph = {}

    for line in lines:
        a, b = line.strip().split('-')
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph

def find_triangles(graph):
    groups = set()
    for node in graph:
        for neighbor in graph[node]:
            intersection = list(set(graph[neighbor]).intersection(set(graph[node])))
            for i in intersection:
                g = [node, neighbor, i]
                groups.add(tuple(sorted(g)))
    return groups

def bron_kerbosch(R, P, X, G, output):
    if len(P) == 0 and len(X) == 0:
        output.append(sorted(R))
        return

    for v in P.copy():
        bron_kerbosch(R.union({v}), P.intersection(G[v]), X.intersection(G[v]), G, output)
        P.remove(v)
        X.add(v)

def solve_part_one(input_data):
    graph = parse_input(input_data)
    groups = find_triangles(graph)
    return sum(1 for g in groups if any(i.startswith('t') for i in g))
    
def solve_part_two(input_data):
    graph = parse_input(input_data)

    output = []
    bron_kerbosch(set([]), set(graph.keys()), set([]), graph, output)
    return ','.join(max(output, key=len))

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 23, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 23, solve_part_one, solve_part_two)

