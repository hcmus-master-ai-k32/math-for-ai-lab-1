import random
from .base_directed_big_graph import BaseDirectedBigGraph


class IntDirectedBigGraph(BaseDirectedBigGraph):
    def generate_data(self, num_nodes, num_edges):
        nodes = [i for i in range(num_nodes)]
        for node in nodes:
            self.graph[node] = ([], [])  # initialize in-neighbors and out-neighbors for each node

        edges = 0
        while edges < num_edges:
            node1 = random.choice(nodes)
            node2 = random.choice(nodes)

            if node1 == node2:
                continue  # ignore self-loops
            if node2 in self.out_neighbors(node1):
                continue

            self.out_neighbors(node1).append(node2)

            edges += 1

    def load_graph(self, file_path):
        self.graph = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split()
                node = int(line[0])
                if node not in self.graph:
                    self.graph[node] = [[], []]
                for neighbor in line[1:]:
                    neighbor = int(neighbor)
                    self.out_neighbors(node).append(neighbor)

                    if neighbor not in self.graph:
                        self.graph[neighbor] = [[], []]

                    self.in_neighbors(neighbor).append(node)

        for node in self.graph:
            self.in_neighbors(node).sort()
            self.out_neighbors(node).sort()
