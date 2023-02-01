from .base_undirected_big_graph import BaseUnDirectedBigGraph
import urllib.request
import random


class StringUnDirectedBigGraph(BaseUnDirectedBigGraph):
    def generate_data(self, num_nodes, num_edges):
        """Generate data for a graph with a given number of nodes and edges"""
        word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        words = long_txt.splitlines()
        
        nodes = [random.choice(words) for i in range(num_nodes)]
        for node in nodes:
            self.graph[node] = []

        edges = 0
        while edges < num_edges:
            node1 = random.choice(nodes)
            node2 = random.choice(nodes)

            if node1 == node2:
                continue  # ignore self-loops
            if node2 in self.graph[node1]:  # already have edge
                continue

            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

            edges += 1

        for node in self.graph:
            self.graph[node].sort()

    def load_graph(self, file_path):
        """
        Load a graph from a file
        Format file: node, then the rest is neighbor nodes
        """
        self.graph = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split()
                node = line[0]

                if node not in self.graph:
                    self.graph[node] = []

                for neighbor in line[1:]:
                    if neighbor not in self.graph[node]:
                        self.graph[node].append(neighbor)

                    if neighbor not in self.graph:
                        self.graph[neighbor] = []

                    if node not in self.graph[neighbor]:
                        self.graph[neighbor].append(node)

        for node in self.graph:
            self.graph[node].sort()
