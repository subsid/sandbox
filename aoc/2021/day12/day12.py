from collections import defaultdict, Counter


def get_input(mock=False):
    mock_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip().split(
        "\n"
    )
    for line in mock_input if mock else open("./input.txt", "r"):
        yield line.strip()


class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(lambda: [])

        for edge in edges:
            s, e = edge.split("-")
            self.graph[s].append(e)
            self.graph[e].append(s)

    def edges(self, n):
        return self.graph.get(n)

    def is_small(self, n: str):
        return n.islower()


def find_paths(graph, node, curr_path, seen: Counter, allow_twice=False):
    can_use_twice = lambda x: allow_twice and x != "start"
    paths = []

    if node == "end":
        # paths.append("-".join(curr_path))
        return ["-".join(curr_path)]
    else:
        for n in graph.edges(node):
            if graph.is_small(n):
                if seen[n] == 0:
                    seen[n] += 1
                    paths.extend(
                        find_paths(graph, n, curr_path + [n], seen, allow_twice)
                    )
                    seen[n] -= 1
                # If a node can be used twice in this path, do it!
                elif can_use_twice(n):
                    seen[n] += 1
                    paths.extend(find_paths(graph, n, curr_path + [n], seen, False))
                    seen[n] -= 1
            else:
                paths.extend(find_paths(graph, n, curr_path + [n], seen, allow_twice))

    return paths


def part1(graph):
    start = "start"
    paths = find_paths(graph, start, [start], Counter([start]))

    return len(paths)


def part2(graph):
    start = "start"
    paths = find_paths(graph, start, [start], Counter([start]), allow_twice=True)

    return len(paths)


if __name__ == "__main__":
    assert part1(Graph(get_input(mock=True))) == 10
    print(f"Unique paths: {part1(Graph(get_input(mock=False)))}")
    print(f"Unique paths (one small cave twice): {part2(Graph(get_input(mock=False)))}")
