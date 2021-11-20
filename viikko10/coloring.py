from collections import deque
from typing import Dict, List


class Coloring:
    def __init__(self, n: int):
        self.neighbours = {i: [] for i in range(1, n + 1)}

    def add_edge(self, a: int, b: int):
        self.neighbours[a].append(b)
        self.neighbours[b].append(a)

    def check(self):
        visited = set()
        for node, neighbours in self.neighbours.items():
            if node in visited:
                continue

            component = {}
            queue = deque(neighbours)
            while queue:
                current_node = queue.popleft()
                if current_node in visited:
                    continue

                visited.add(current_node)
                queue.extend(self.neighbours[current_node])
                component[current_node] = self.neighbours[current_node]

            if not self._check_component(component):
                return False

        return True

    def _check_component(self, component: Dict[int, List[int]]):
        if not component:
            return True

        first_node = list(component.keys())[0]
        seen = set()
        colors = {first_node: False}
        queue = deque([first_node])
        while queue:
            node = queue.popleft()
            if node in seen:
                continue
            if node not in colors:
                raise RuntimeError(f"Node {node} not in {colors}")

            adjacent_colors = set(
                colors[neighbour]
                for neighbour in component[node]
                if neighbour in colors
            )
            if len(adjacent_colors) > 1:
                return False
            if len(adjacent_colors) == 1 and adjacent_colors.pop() == colors[node]:
                return False

            for neighbour in component[node]:
                if neighbour not in colors:
                    colors[neighbour] = not colors[node]

            seen.add(node)
            queue.extend(component[node])

        return True


if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check())  # True
    c.add_edge(2, 4)
    print(c.check())  # False

    c = Coloring(5)
    c.add_edge(2, 3)
    c.add_edge(1, 2)
    c.add_edge(1, 4)
    print(c.check())  # True
    print(c.check())  # True
    c.add_edge(4, 5)
    c.add_edge(1, 5)
    print(c.check())  # False
    c.add_edge(2, 4)
    c.add_edge(2, 3)

    c = Coloring(5)
    c.add_edge(4, 5)
    print(c.check())  # True
    print(c.check())  # True
    c.add_edge(2, 3)
    print(c.check())  # True
    c.add_edge(3, 5)
    c.add_edge(1, 3)
    print(c.check())  # True
    c.add_edge(3, 4)
    print(c.check())  # False
