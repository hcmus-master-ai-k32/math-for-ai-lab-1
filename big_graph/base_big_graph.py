import bisect
from abc import ABC, abstractmethod


class BaseBigGraph(ABC):
    """
    This is abstract base class to define common methods for big graph
    """

    @abstractmethod
    def generate_data(self, num_nodes, num_edges):
        """Generate data for a graph with a given number of nodes and edges"""
        pass

    @abstractmethod
    def load_graph(self, file_path):
        """
        Load a graph from a file
        Format file: node, then the rest is neighbor nodes
        """
        pass

    @abstractmethod
    def save_graph(self, file_path):
        """Save a graph to a file"""
        pass

    @abstractmethod
    def add_node(self, node):
        """Add a node to the graph"""
        pass

    @abstractmethod
    def get_node(self, node):
        """Return neighbors of a given node"""
        pass

    def remove_node(self, node):
        """Remove a node and all its edges from the graph"""
        pass

    @abstractmethod
    def add_edge(self, node1, node2):
        """Add an directed edge from node1 to node2"""
        pass

    @abstractmethod
    def is_edge(self, node1, node2):
        """Check if an edge exists between two nodes"""
        pass

    @abstractmethod
    def remove_edge(self, node1, node2):
        """Remove an edge from the graph"""
        pass

    @abstractmethod
    def dfs(self, start_node):
        pass
