import bisect
from abc import abstractmethod
from .base_big_graph import BaseBigGraph


class BaseUnDirectedBigGraph(BaseBigGraph):
    """
    This is abstract base class to allow reuse common methods
    """

    def __init__(self):
        # Key is node
        # Value is list of neighbor nodes
        self.graph = {}

    @abstractmethod
    def generate_data(self, num_nodes, num_edges):
        """Generate data for a graph with a given number of nodes and edges"""
        pass

    def load_graph(self, file_path):
        """
        Load a graph from a file
        Format file: node, then the rest is neighbor nodes
        """
        pass

    def save_graph(self, file_path):
        """Save a graph to a file"""
        with open(file_path, 'w') as file:
            for node in self.graph:
                file.write(str(node) + ' ' + ' '.join(map(str, self.graph[node])) + '\n')

    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = []

    def get_node(self, node):
        """Return neighbors of a given node"""
        if node in self.graph:
            return self.graph[node]
        else:
            raise ValueError(f"{node} is not in the graph")

    def remove_node(self, node):
        """Remove a node and all its edges from the graph"""
        if node not in self.graph:
            print(f'Error: node {node} not in the graph')
            return

        # Remove node from neighbor nodes
        for neighbor in self.graph[node]:
            self.graph[neighbor].remove(node)
            self.graph[neighbor].sort()

        # remove the node from the graph
        del self.graph[node]

    def add_edge(self, node1, node2):
        """Add an directed edge from node1 to node2"""
        self.add_node(node1)
        self.add_node(node2)

        bisect.insort(self.graph[node1], node2)
        bisect.insort(self.graph[node2], node1)

    def is_edge(self, node1, node2):
        """Check if an edge exists between two nodes"""
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                return True
            else:
                return False
        else:
            raise ValueError(f"Either {node1} or {node2} is not in the graph")

    def remove_edge(self, node1, node2):
        """Remove an edge from the graph"""
        if node1 not in self.graph:
            print(f'Error: node {node1} not in the graph')
            return

        if node2 not in self.graph:
            print(f'Error: node {node2} not in the graph')
            return

        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)

    def dfs(self, start_node):
        if start_node not in self.graph:
            raise ValueError(f"{start_node} not exists in graph")

        visited = set()
        stack = [start_node]
        path = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                path.append(node)

                for neighbor in self.graph[node]:
                    stack.append(neighbor)

        return path
