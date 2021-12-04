from typing import Dict, List


class CoursePlan:
    def __init__(self):
        self.G: Dict[str, List[str]] = {}

    def add_course(self, course: str):
        self.G[course] = []

    def add_requisite(self, course1: str, course2: str):
        self.G[course1].append(course2)

    def find(self):
        self.cycle = False
        self.done = {}
        self.result = []
        for node in self.G:
            if self.cycle:
                return None

            self.traverse(node)

        if any(x not in self.result for x in self.G):
            return None

        return list(reversed(self.result))

    def traverse(self, node):
        processed = self.done.get(node) == True

        self.done[node] = False
        for neighbour in self.G[node]:
            if self.done.get(neighbour) == False:
                self.cycle = True
                return

            self.traverse(neighbour)

        if not processed:
            self.result.append(node)

        self.done[node] = True


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find())  # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find())  # None
